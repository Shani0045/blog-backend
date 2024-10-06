# custom middleware for handle exception 
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError

async def custom_http_exception_handler(request:Request, exc:HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "ERROR",
            "message":"Something went wrong",
            "errors": exc.detail if isinstance(exc.detail, dict) else {}
        })


# Custom Exception for validation
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Create a dictionary for detailed errors
    errors = {}
    for error in exc.errors():
        field = error['loc'][-1]  # Field name
        message = error['msg']  # Error message
        errors[field] = message
    
    return JSONResponse(
        status_code=200,
        content={
            "status": "ERROR",
            "message": "data is invalid",
            "errors": errors
        }
    )

async def internal_server_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "status": "ERROR",
            "message": "internal server error",
            "errors": {"error": str(exc)}
        }
    )

# register function for handle errors
def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(Exception, internal_server_error_handler)

def register_validation_exception_handlers(app: FastAPI):
    app.add_exception_handler(RequestValidationError, validation_exception_handler)

def register_http_exception_handlers(app: FastAPI):
    app.add_exception_handler(HTTPException, custom_http_exception_handler)
