from fastapi import FastAPI
from pydantic import BaseModel
from db import db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


app = FastAPI(title="nAI Authentication Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Request model
# --------------------------------------------------

class LoginRequest(BaseModel):
    username: str
    password: str


# --------------------------------------------------
# Login API
# --------------------------------------------------


@app.post("/login")
def login(request: LoginRequest):

    # Get login credentials from auth database
    user = db.fetch_one(
        """
        SELECT id, username, password_hash, status
        FROM login_users
        WHERE username = %s
        """,
        (request.username,)
    )

    # Username does not exist
    if user is None:
        return JSONResponse(
            status_code=401,
            content={
                "success": False,
                "message": "Invalid username or password"
            }
        )

    user_id, username, password_hash, status = user

    # Check account status
    if status != "ACTIVE":
        return JSONResponse(
            status_code=401,
            content={
                "success": False,
                "message": "User account is inactive"
            }
        )

    # Temporary password validation
    if request.password != password_hash:
        return JSONResponse(
            status_code=401,
            content={
                "success": False,
                "message": "Invalid username or password"
            }
        )

    # Login successful
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "message": "Login successful",
            "user_id": user_id,
            "username": username
        }
    )


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/health") 
def health(): 
    result = db.fetch_one("SELECT 1;") 
    return { 
        "status": "ok", 
        "database": "connected" if result else "error" 
        }
