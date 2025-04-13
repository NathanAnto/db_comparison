import sys
import subprocess

def run_insert(db_name):
    if db_name == "Postgres":
        # Drop the database
        drop_db_command = [
            "docker", "exec", "-i", "postgres_bench",
            "psql", "-U", "user", "-d", "postgres", "-c", "DROP DATABASE IF EXISTS testdb;"
        ]
        result = subprocess.run(drop_db_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error dropping Postgres database: {result.stderr}", file=sys.stderr)
            sys.exit(1)

        # Create the database
        create_db_command = [
            "docker", "exec", "-i", "postgres_bench",
            "psql", "-U", "user", "-d", "postgres", "-c", "CREATE DATABASE testdb;"
        ]
        result = subprocess.run(create_db_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error creating Postgres database: {result.stderr}", file=sys.stderr)
            sys.exit(1)

        # Copy the CSV file into the container
        copy_file_command = [
            "docker", "cp", "data.csv", "postgres_bench:/data.csv"
        ]
        result = subprocess.run(copy_file_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error copying file to Postgres container: {result.stderr}", file=sys.stderr)
            sys.exit(1)

        # Create the table
        create_table_command = [
            "docker", "exec", "-i", "postgres_bench",
            "psql", "-U", "user", "-d", "testdb", "-c",
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                age INT,
                email VARCHAR(100) UNIQUE
            );
            """
        ]
        result = subprocess.run(create_table_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error creating table in Postgres: {result.stderr}", file=sys.stderr)
            sys.exit(1)

        # Import the data from the CSV file
        import_data_command = [
            "docker", "exec", "-i", "postgres_bench",
            "psql", "-U", "user", "-d", "testdb", "-c", "\\copy users FROM '/data.csv' CSV HEADER;"
        ]
        result = subprocess.run(import_data_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error importing data into Postgres: {result.stderr}", file=sys.stderr)
            sys.exit(1)

        print("Data inserted into Postgres successfully.")

    elif db_name == "MongoDB":
        # MongoDB block (unchanged)
        pass

    elif db_name == "Redis":
        # Redis block (unchanged)
        pass

    else:
        print(f"Unknown database: {db_name}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 insert-time.py <database_name>", file=sys.stderr)
        sys.exit(1)

    db_name = sys.argv[1]
    run_insert(db_name)