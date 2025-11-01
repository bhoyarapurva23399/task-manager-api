# app.py
# --------------------------------------
# Task Manager API using Flask RESTful
# Created by Apurva Bhoyar
# --------------------------------------

from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# In-memory "database"
tasks = []

# Task Resource Class
class Task(Resource):
    def get(self):
        """Get all tasks"""
        return jsonify(tasks)

    def post(self):
        """Add a new task"""
        data = request.get_json()
        if not data or 'title' not in data:
            return {"error": "Title is required"}, 400
        new_task = {
            "id": len(tasks) + 1,
            "title": data["title"],
            "completed": False
        }
        tasks.append(new_task)
        return new_task, 201

class SingleTask(Resource):
    def put(self, task_id):
        """Update a task's completion status"""
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                return task, 200
        return {"error": "Task not found"}, 404

    def delete(self, task_id):
        """Delete a task"""
        global tasks
        tasks = [t for t in tasks if t["id"] != task_id]
        return {"message": "Task deleted"}, 200

# Adding resources
api.add_resource(Task, "/tasks")
api.add_resource(SingleTask, "/tasks/<int:task_id>")

if __name__ == "__main__":
    app.run(debug=True)
