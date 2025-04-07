time docker exec -it postgres_bench psql -U user -d testdb -c "SELECT * FROM users WHERE id = 500000;"
time docker exec -it mongo_bench mongosh testdb --eval "db.users.findOne({_id: 500000})"
time docker exec -it redis_bench redis-cli HGETALL user:500000
