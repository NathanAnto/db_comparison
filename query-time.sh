time docker exec -it postgres_bench psql -U user -d testdb -c "SELECT COUNT(*) FROM users;"
time docker exec -it mongo_bench mongosh testdb --eval "db.users.estimatedDocumentCount();"
time docker exec -it redis_bench redis-cli dbsize