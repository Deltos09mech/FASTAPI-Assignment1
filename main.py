from fastapi import FastAPI

app = FastAPI()


# 1. Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to my first FastAPI assignment"
    }


# 2. About API
@app.get("/about")
def about():
    return {
        "student_name": "Mandeep Singh",
        "course": "FastAPI",
        "topic": "First API Assignment",
        "status": "Learning"
    }


# 3. Trainer API
@app.get("/trainer")
def trainer():
    return {
        "name": "Hemanth",
        "role": "Trainer",
        "subject": "FastAPI"
    }


# 4. Courses API
@app.get("/courses")
def courses():
    return [
        {
            "id": 1,
            "name": "Python Basics",
            "duration": "1 Week"
        },
        {
            "id": 2,
            "name": "FastAPI",
            "duration": "2 Weeks"
        },
        {
            "id": 3,
            "name": "SQL Basics",
            "duration": "1 Week"
        }
    ]


# 5. Students API
@app.get("/students")
def students():
    return [
        {
            "id": 1,
            "name": "Mandeep Singh",
            "course": "Python",
            "city": "Jammu"
        },
        {
            "id": 2,
            "name": "Rahul",
            "course": "FastAPI",
            "city": "Delhi"
        },
        {
            "id": 3,
            "name": "Priya",
            "course": "SQL",
            "city": "Mumbai"
        },
        {
            "id": 4,
            "name": "Ankit",
            "course": "Python",
            "city": "Chandigarh"
        },
        {
            "id": 5,
            "name": "Simran",
            "course": "FastAPI",
            "city": "Amritsar"
        }
    ]


# 6. College API
@app.get("/college")
def college():
    return {
        "college_name": "Model Institute of Engineering and Technology",
        "location": "Jammu",
        "department": "Computer Science and Engineering (AI & ML)",
        "current_module": "FastAPI Basics"
    }


# 7. Technologies API
@app.get("/technologies")
def technologies():
    return [
        "Python",
        "FastAPI",
        "JSON",
        "HTTP",
        "REST API"
    ]