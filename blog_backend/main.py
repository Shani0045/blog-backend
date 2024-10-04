from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import api_router
from core.middlewares.middlewares import (register_exception_handlers, register_http_exception_handlers, 
                                            register_validation_exception_handlers)
# from app.config import conf
 
API_TITLE =  "Blog Management System"
API_VERSION = "v1" #conf.API_VERSION
DESCRIPTION = "blog management system api version "+API_VERSION

DOCS_URL = "/test-apis" #if os.getenv("PYTHON_ENV") in ["dev", "development", "test"] else None
REDOC_URL = "/"  #if os.getenv("PYTHON_ENV") in ["dev", "development", "test"] else None

app = FastAPI(
        title =API_TITLE,
        description = DESCRIPTION ,
        version = API_VERSION,
        docs_url = DOCS_URL ,
        redoc_url = REDOC_URL
    )

register_exception_handlers(app)
register_validation_exception_handlers(app)
register_http_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(api_router)
