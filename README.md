# Database comparison
This project aims to compare the performance, features, and use cases of different database systems. It includes benchmarks, feature analysis, and recommendations based on specific scenarios.

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
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. **Docker**  
    For this to work, three docker containers must be running. Run the docker-compose.yaml config
    ```bash
    docker-compose up -d
    ```

5. **Run Initial Tests**  
    Verify the setup by running the initial tests:
    ```bash
    python main.py
    ```
    The results will be in `results.csv`.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
