
import json
from fastapi.testclient import TestClient

from app.main import app
from app.models.llm_response import LLMResponse

client = TestClient(app)


def test_invoke_success(monkeypatch):
    # setup
    def mock_invoke_llm_provider(self, *, llm_request):
        return LLMResponse(
            llm_request=llm_request,
            raw_response={
                "model": "llama3",
                "response": "mocked answer"
            },
            success=True
        )

    monkeypatch.setattr(
        "app.services.llm_service.LLMService.invoke_llm_provider",
        mock_invoke_llm_provider
    )

    request_body = {
        "requestId": "1",
        "queryKind": "reroute_passengers",
        "llmQuery": {
            "model": "llama3",
            "prompt": "Why is the sky blue?",
            "stream": False
        }
    }

    # invocation
    response = client.post("/invoke", json=request_body)

    # assertions
    assert response.status_code == 200

    response_json = response.json()
    assert response_json["success"] is True
    assert response_json["rawResponse"] is not None
    assert response_json["llmRequest"]["requestId"] == "1"


def test_invoke_bad_request_when_request_id_missing():
    # setup
    request_body = {
        "queryKind": "reroute_passengers",
        "llmQuery": {
            "model": "llama3",
            "prompt": "Why is the sky blue?",
            "stream": False
        }
    }

    # invocation
    response = client.post("/invoke", json=request_body)

    # assertions
    assert response.status_code == 400

    response_json = response.json()
    assert response_json["message"] == "bad_request"


def test_invoke_bad_request_when_query_kind_missing():
    # setup
    request_body = {
        "requestId": "1",
        "llmQuery": {
            "model": "llama3",
            "prompt": "Why is the sky blue?",
            "stream": False
        }
    }

    # invocation
    response = client.post("/invoke", json=request_body)

    # assertions
    assert response.status_code == 400

    response_json = response.json()
    assert response_json["message"] == "bad_request"


def test_invoke_bad_request_when_llm_query_missing():
    # setup
    request_body = {
        "requestId": "1",
        "queryKind": "reroute_passengers"
    }

    # invocation
    response = client.post("/invoke", json=request_body)

    # assertions
    assert response.status_code == 400

    response_json = response.json()
    assert response_json["message"] == "bad_request"
