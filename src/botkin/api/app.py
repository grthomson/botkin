from fastapi import FastAPI

app = FastAPI(title="Botkin API")

@app.get("/health")
def health():
    return {"status": "ok"}
