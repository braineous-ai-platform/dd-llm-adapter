
import pytest
from urllib.error import HTTPError
from app.models.llm_request import LLMRequest
from app.models.llm_response import LLMResponse
from app.services.llm_service import LLMService


def test_invoke_llm_provider_success():
    # setup
    llm_service = LLMService()

    payload = {
        "model": "llama3",
        "prompt": "Why is the sky blue?",
        "stream": False
    }
    llm_request = LLMRequest(
        request_id="1", query_kind="reroute_passengers", llm_query=payload)

    # invocation
    llm_response = llm_service.invoke_llm_provider(llm_request=llm_request)

    # assertions
    print(llm_response)

    assert llm_response.llm_request is not None
    assert llm_response.raw_response is not None
    assert llm_response.success == True

    # shape assertion
    assert isinstance(llm_response.raw_response, (dict, list))

# ---------------------------------------------------------------------------------------


def test_invoke_llm_provider_fail_raises_http_error(monkeypatch):
    # setup
    llm_service = LLMService()

    payload = {
        "model": "llama3",
        "prompt": "Why is the sky blue?",
        "stream": False
    }

    llm_request = LLMRequest(
        request_id="1",
        query_kind="reroute_passengers",
        llm_query=payload
    )

    def fake_urlopen(_request):
        raise HTTPError(
            url="http://localhost:11434/api/generate",
            code=500,
            msg="Internal Server Error",
            hdrs={},  # type: ignore
            fp=None
        )

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

    with pytest.raises(HTTPError):
        llm_service.invoke_llm_provider(llm_request=llm_request)
