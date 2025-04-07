docker exec -it postgres_bench psql -U user -d postgres -c "DROP DATABASE testdb;"
docker exec -it postgres_bench psql -U user -d postgres -c "CREATE DATABASE testdb;"

docker cp data.csv postgres_bench:/data.csv
docker exec -it postgres_bench psql -U user -d testdb -c "
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        email VARCHAR(100) UNIQUE
    );"
docker exec -it postgres_bench psql -U user -d testdb -c "\copy users FROM '/data.csv' CSV HEADER;"
