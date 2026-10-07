from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Panel de Sesiones y Ocupación",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "mensaje": "¡Tu Panel de Sesiones y Ocupación está funcionando perfectamente!",
        "estado": "Conectado y listo para usar"
    }

@app.get("/api/health")
def health_check():
    return {"status": "ok", "base_de_datos": "conectada"}
