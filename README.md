# Database comparison
This project aims to compare the performance, features, and use cases of different database systems. It includes benchmarks, feature analysis, and recommendations based on specific scenarios.

## Databases
Here are quick links to the official documentation for each database used:

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)

## Features
- Performance benchmarks for various database operations.
- Analysis of supported features across databases.
- Use case recommendations for each database.

## Getting Started
1. Clone the repository:
    ```bash
    git clone https://github.com/NathanAnto/db_comparison.git
    ```
2. Navigate to the project directory:
    ```bash
    cd db_comparison
    ```

### Setting Up the Environment
To set up the environment for this project, follow these steps:

1. **Install Dependencies**  
    Ensure you have the required dependencies installed. For example:
    - Python 3.8 or higher
    - pip (Python package manager)

2. **Create a Virtual Environment**  
    Create and activate a virtual environment to isolate the project dependencies:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Required Python Packages**  
    Install the necessary Python packages listed in the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

4. **Generate Mock Data**  
    Run the `data.py` script to generate the `data.csv` file. The databases will use this data
    for the tests.
    ```bash
    python data.py
    ```

5. **Docker**  
    For this to work, three docker containers must be running. Run the docker-compose.yaml config:
    ```bash
    docker-compose up -d
    ```

6. **Run Initial Tests**  
    Verify the setup by running the initial tests:
    ```bash
    python main.py
    ```
    The results will be in `results.csv`.

## Graphs
In the `results.ipynb` file, you can see the different graphs based on the `results.csv`

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
