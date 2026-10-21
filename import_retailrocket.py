
import argparse
import os
import sys
import math

import pandas as pd
from tqdm import tqdm
from neo4j import GraphDatabase


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Impor dataset RetailRocket ke Neo4j."
    )
    parser.add_argument("-u", "--user", default="neo4j")
    parser.add_argument("-p", "--password", default="REZAUTSGSD2026")
    parser.add_argument(
        "-b", "--bolt", default="bolt://127.0.0.1:7687"
    )
    parser.add_argument("-s", "--source", default="retailrocket")
    parser.add_argument("--batch-size", type=int, default=1000)
    return parser.parse_args()

# ADA PENYESUAIAN
def create_constraints(session):
    session.run(
        "CREATE CONSTRAINT visitor_id_unique IF NOT EXISTS "
        "FOR (v:Visitor) REQUIRE v.visitorId IS UNIQUE"
    )
    session.run(
        "CREATE CONSTRAINT item_id_unique IF NOT EXISTS "
        "FOR (i:Item) REQUIRE i.itemId IS UNIQUE"
    )


def import_batch(tx, batch):
    cypher_query = """
    UNWIND $batch AS row
    MERGE (v:Visitor {visitorId: row.visitorid})
    MERGE (i:Item {itemId: row.itemid})

    FOREACH (_ IN CASE
        WHEN row.event = 'view' THEN [1] ELSE [] END |
        CREATE (v)-[:VIEWED {timestamp: row.timestamp}]->(i)
    )

    FOREACH (_ IN CASE
        WHEN row.event = 'addtocart' THEN [1] ELSE [] END |
        CREATE (v)-[:ADDED_TO_CART {timestamp: row.timestamp}]->(i)
    )

    FOREACH (_ IN CASE
        WHEN row.event = 'transaction' THEN [1] ELSE [] END |
        CREATE (v)-[:BOUGHT {
            timestamp: row.timestamp,
            transactionId: row.transactionid
        }]->(i)
    )
    """
    tx.run(cypher_query, batch=batch)


def main():
    args = parse_arguments()

    if args.batch_size < 1:
        print("Error: batch-size harus lebih besar dari 0.")
        sys.exit(1)

    csv_file_path = os.path.join(args.source, "events.csv")

    if not os.path.exists(csv_file_path):
        print(f"Error: File '{csv_file_path}' tidak ditemukan!")
        sys.exit(1)

    try:
        driver = GraphDatabase.driver(
            args.bolt,
            auth=(args.user, args.password)
        )
        driver.verify_connectivity()
    except Exception as error:
        print(f"Gagal terhubung ke database: {error}")
        sys.exit(1)

    try:
        print(f"Membaca file: {csv_file_path}")

        with open(csv_file_path, encoding="utf-8") as file:
            total_rows = sum(1 for _ in file) - 1

        total_chunks = math.ceil(total_rows / args.batch_size)

        with driver.session(database="retailrocket") as session:
            create_constraints(session)

            chunks = pd.read_csv(
                csv_file_path,
                chunksize=args.batch_size
            )

            print("Memulai proses impor ke Neo4j...")

            for chunk in tqdm(
                chunks,
                total=total_chunks,
                desc="Mengimpor batch"
            ):
                chunk["transactionid"] = chunk[
                    "transactionid"
                ].apply(
                    lambda value: int(value)
                    if pd.notna(value) else None
                )

                records = chunk.to_dict(orient="records")
                session.write_transaction(import_batch, records)

        print("Proses impor berhasil.")

    except Exception as error:
        print(f"Proses impor gagal: {error}")
        sys.exit(1)

    finally:
        driver.close()


if __name__ == "__main__":
    main()
