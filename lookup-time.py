import sys
import subprocess

def run_query(db_name):
    if db_name == "Postgres":
        # Ensure the `id` column is indexed for faster lookups
        index_command = [
            "docker", "exec", "-i", "postgres_bench",
            "psql", "-U", "user", "-d", "testdb", "-c", "CREATE INDEX IF NOT EXISTS idx_users_id ON users (id);"
        ]
        subprocess.run(index_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Run the lookup query
        command = [
            "docker", "exec", "-i", "postgres_bench",
            "psql", "-U", "user", "-d", "testdb", "-c", "SELECT * FROM users WHERE id = 5000;"
        ]
    elif db_name == "MongoDB":
        # Use the correct field for lookup (e.g., `id` instead of `_id`)
        command = [
            "docker", "exec", "-i", "mongo_bench",
            "mongosh", "testdb", "--eval", "db.users.findOne({id: 5000})"
        ]
    elif db_name == "Redis":
        # Use the correct key format for lookup
        command = [
            "docker", "exec", "-i", "redis_bench",
            "redis-cli", "HGETALL", "user:5000"
        ]
    else:
        print(f"Unknown database: {db_name}", file=sys.stderr)
        sys.exit(1)

    # Run the command and capture output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    print(result.stdout.strip())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 lookup-time.py <database_name>", file=sys.stderr)
        sys.exit(1)

    db_name = sys.argv[1]
    run_query(db_name)