docker exec -it mongo_bench mongosh testdb --eval "db.dropDatabase();"

docker cp data.csv mongo_bench:/data.csv
docker exec -it mongo_bench bash -c "
    mongosh testdb --eval 'db.users.drop();'
    mongoimport --db testdb --collection users --type csv --file /data.csv --headerline
"
