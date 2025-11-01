# curl examples

## Get tasks
curl -X GET http://127.0.0.1:5000/tasks

## Create task
curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'

## Update task
curl -X PUT http://127.0.0.1:5000/tasks/1

## Delete task
curl -X DELETE http://127.0.0.1:5000/tasks/1
