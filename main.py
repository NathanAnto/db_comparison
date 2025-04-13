import subprocess
import time
import sys
import csv

# Number of iterations for each test
ITERATIONS = 5

# Output CSV file
OUTPUT_FILE = "results.csv"

# Test scripts and their corresponding names
TEST_SCRIPTS = [
    ("insert-time.py", "Insert Time"),
    ("query-time.py", "Query Time"),
    ("lookup-time.py", "Lookup Time"),
]

# Databases to test
DATABASES = ["Postgres", "MongoDB", "Redis"]
CONTAINERS = ["postgres_bench", "mongo_bench", "redis_bench"]

def run_test(script, test_name, db_name):
    """Run a test script for a specific database and measure execution time and resource usage."""
    # Set the container name based on the database
    if db_name == "Postgres":
        container_name = CONTAINERS[0]
    elif db_name == "MongoDB":
        container_name = CONTAINERS[1]
    elif db_name == "Redis":
        container_name = CONTAINERS[2]
    else:
        print(f"Unknown database: {db_name}")
        return

    for i in range(1, ITERATIONS + 1):
        print(f"Running {test_name} for {db_name} (Iteration {i})...")
        start_time = time.time()

        # Get initial resource usage
        initial_cpu, initial_memory = get_docker_stats(container_name)

        try:
            # Run the script with the database name as an argument
            result = subprocess.run(
                ["python3", script, db_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30,  # Timeout after 30 seconds
            )
            elapsed_time = time.time() - start_time

            # Get final resource usage
            final_cpu, final_memory = get_docker_stats(container_name)

            # Check for errors
            if result.returncode != 0:
                print(f"Error: {script} failed for {db_name} on iteration {i}")
                print(f"Stderr: {result.stderr}")
                elapsed_time = "N/A"
                final_cpu, final_memory = "N/A", "N/A"
            else:
                print(f"Output: {result.stdout.strip()}")

        except subprocess.TimeoutExpired:
            print(f"Error: {script} timed out for {db_name} on iteration {i}")
            elapsed_time = "N/A"
            final_cpu, final_memory = "N/A", "N/A"

        # Append the result to the CSV file
        with open(OUTPUT_FILE, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([test_name, db_name, i, elapsed_time, initial_cpu, final_cpu, initial_memory, final_memory])

def get_docker_stats(container_name):
    """Get memory and CPU usage for a Docker container."""
    try:
        result = subprocess.run(
            ["docker", "stats", container_name, "--no-stream", "--format", "{{.CPUPerc}},{{.MemUsage}}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode != 0:
            print(f"Error fetching stats for {container_name}: {result.stderr}", file=sys.stderr)
            return "N/A", "N/A"
        cpu, memory = result.stdout.strip().split(",")
        return cpu, memory
    except Exception as e:
        print(f"Error fetching Docker stats: {e}", file=sys.stderr)
        return "N/A", "N/A"

def main():
    # Initialize the CSV file with headers
    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Test", "Database", "Iteration", "Time (s)", "Initial CPU (%)", "Final CPU (%)", "Initial Memory", "Final Memory"])

    # Run all tests
    for script, test_name in TEST_SCRIPTS:
        for db_name in DATABASES:
            run_test(script, test_name, db_name)

    print(f"All tests completed. Results saved to {OUTPUT_FILE}.")

if __name__ == "__main__":
    main()