from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="dd-llm-adapter")

# -------- request / response schemas --------


class InvokeRequest(BaseModel):
    prompt: Dict[str, Any]


class InvokeResponse(BaseModel):
    rawResponse: Dict[str, Any]

# -------- endpoints --------


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/invoke", response_model=InvokeResponse)
def invoke(req: InvokeRequest):
    # v0: deterministic mock that matches your Java-side contract shape
    return {
        "rawResponse": {
            "result": {
                "ok": True,
                "code": "response.contract.ok",
                "message": "mock",
                "stage": "llm_response_validation",
                "anchorId": "mock",
                "metadata": {}
            }
        }
    }
