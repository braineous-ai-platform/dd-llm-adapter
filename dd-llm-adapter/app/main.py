from fastapi import FastAPI, Request
from app.apis.invoke import router as invoke_router

app = FastAPI(title="dd-llm-adapter")
app.include_router(invoke_router)


@app.get("/health")
def health():
    return {"status": "ok"}
