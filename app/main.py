from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.routes import fichajes

app = FastAPI(title="Api fichajes",description="API para control de presencia", version="1.0.0",swagger_ui_parameters={"defaultModelsExpandDepth": -1})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          
    allow_credentials=True,         
    allow_methods=["*"],             
    allow_headers=["*"],
)
app.include_router(fichajes.router, prefix="/fichajes", tags=["Fichajes"])