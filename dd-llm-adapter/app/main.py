from fastapi import FastAPI, Request

app = FastAPI(title="dd-llm-adapter")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/invoke")
async def invoke(request: Request):
    body_bytes = await request.body()
    body_str = body_bytes.decode("utf-8")

    # optional: print for sanity
    print("RAW BODY:", body_str)

    return {
        "rawResponse": {
            "result": {
                "ok": True,
                "code": "response.contract.ok",
                "message": "mock",
                "stage": "llm_response_validation",
                "anchorId": "mock",
                "metadata": {
                    "echo": body_str
                }
            }
        }
    }
