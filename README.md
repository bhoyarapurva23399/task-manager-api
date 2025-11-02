# 🧠 Task Manager API

A Python-based **Task Manager** project built using **Flask**, which provides a simple **REST API** for managing tasks — including creating, updating, viewing, and deleting tasks.  
This project demonstrates practical backend development skills with Flask, RESTful APIs, and JSON-based communication.

---

## 🚀 Features

- Create new tasks with title and description  
- Retrieve all tasks or a single task by ID  
- Update task details (status, description, etc.)  
- Delete tasks  
- JSON-based responses for easy integration  
- Built-in testing and examples included  

---

## 🧩 Technologies Used

- **Python 3**
- **Flask**
- **Requests**
- **JSON**
- **Unit Testing (pytest)**

---

## 📂 Project Structure

task-manager-api/
│
├── app.py # Main Flask app (entry point)
├── main_api.py # Core REST API logic
├── utils.py # Helper functions
├── requirements.txt # Dependencies
│
├── tests/
│ └── test_requests.py # Basic test scripts
│
├── examples/
│ └── curl_examples.md # API request examples
│
├── screenshots/
│ └── placeholder.txt # Optional screenshots folder
│
└── README.md


---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/task-manager-api.git
   cd task-manager-api

   
2. Install Dependencies
  ```bash
     pip install -r requirements.txt
  ```

3. Run the Flask Server
   ```bash
     python app.py
   ```

5. Test the API
   ```bash
    GET http://127.0.0.1:5000/tasks
   ```


   📸 Example Output
   POST /tasks
{
  "title": "Finish GitHub project",
  "description": "Complete the Flask API integration"
}


Response:
{
  "id": 1,
  "title": "Finish GitHub project",
  "description": "Complete the Flask API integration",
  "status": "Pending"
}


📚 Learning Highlights

Practical backend design with Flask

Understanding REST APIs and HTTP methods

Structuring Python projects for GitHub portfolio

Writing clean and maintainable code

👩‍💻 Author

Apurva Bhoyar

💻 GitHub: https://github.com/YOUR_GITHUB_bhoyarapurva23399

🏷️ Tags

python flask rest-api backend-development task-manager

---




