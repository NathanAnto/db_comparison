docker exec -it redis_bench redis-cli FLUSHALL
docker cp data.csv redis_bench:/data.csv
awk -F, 'NR>1 {print "HMSET user:"$1" name "$2" age "$3" email "$4}' data.csv | docker exec -i redis_bench redis-cli --pipe
