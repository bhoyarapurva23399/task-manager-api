import requests

BASE = "http://127.0.0.1:5000"

def get_tasks():
    r = requests.get(f"{BASE}/tasks")
    print("GET /tasks ->", r.status_code, r.text)

if __name__ == "__main__":
    get_tasks()
