import subprocess
import time
import csv

# Number of iterations for each test
ITERATIONS = 3

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

def run_test(script, test_name, db_name):
    """Run a test script for a specific database and measure execution time."""
    for i in range(1, ITERATIONS + 1):
        print(f"Running {test_name} for {db_name} (Iteration {i})...")
        start_time = time.time()

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

            # Check for errors
            if result.returncode != 0:
                print(f"Error: {script} failed for {db_name} on iteration {i}")
                print(f"Stderr: {result.stderr}")
                elapsed_time = "N/A"
            else:
                print(f"Output: {result.stdout.strip()}")

        except subprocess.TimeoutExpired:
            print(f"Error: {script} timed out for {db_name} on iteration {i}")
            elapsed_time = "N/A"

        # Append the result to the CSV file
        with open(OUTPUT_FILE, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([test_name, db_name, i, elapsed_time])

def main():
    # Initialize the CSV file with headers
    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Test", "Database", "Iteration", "Time (s)"])

    # Run all tests
    for script, test_name in TEST_SCRIPTS:
        for db_name in DATABASES:
            run_test(script, test_name, db_name)

    print(f"All tests completed. Results saved to {OUTPUT_FILE}.")

if __name__ == "__main__":
    main()