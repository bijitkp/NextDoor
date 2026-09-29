from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="nAI User Service")


# --------------------------------------------------
# Request models
# --------------------------------------------------

class UserCreateRequest(BaseModel):
    username: str
    email: str
    phone: str


# --------------------------------------------------
# Temporary user data
# --------------------------------------------------

users = [
    {
        "id": 1,
        "username": "admin",
        "email": "admin@nextdoor.com",
        "phone": "9999999999"
    }
]


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# --------------------------------------------------
# Get all users
# --------------------------------------------------

@app.get("/users")
def get_users():
    return {
        "success": True,
        "users": users
    }


# --------------------------------------------------
# Get user by ID
# --------------------------------------------------

@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return {
                "success": True,
                "user": user
            }

    return {
        "success": False,
        "message": "User not found"
    }


# --------------------------------------------------
# Create user
# --------------------------------------------------

@app.post("/users")
def create_user(request: UserCreateRequest):

    new_user = {
        "id": len(users) + 1,
        "username": request.username,
        "email": request.email,
        "phone": request.phone
    }

    users.append(new_user)

    return {
        "success": True,
        "message": "User created successfully",
        "user": new_user
    }