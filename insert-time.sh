time ./pgdb.sh      # (docker exec -it postgres_bench psql -U user -d testdb -c "\copy users FROM '/data.csv' CSV HEADER;")
time ./mongodb.sh   # (docker exec -it mongo_bench mongoimport --db testdb --collection users --type csv --file /data.csv --headerline)
time ./redisdb.sh   # (awk -F, 'NR>1 {print "HMSET user:"$1" name "$2" age "$3" email "$4}' data.csv | docker exec -i redis_bench redis-cli)
