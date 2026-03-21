
import json
from fastapi import FastAPI, Request, APIRouter, Body, Response, status
from app.models.llm_request import LLMRequest
from app.models.llm_response import LLMResponse
from app.services.llm_service import LLMService

router = APIRouter()


@router.post("/invoke")
async def invoke(body: dict = Body(...)):
    request_id = body.get("requestId")
    query_kind = body.get("queryKind")
    llm_query = body.get("llmQuery")

    if not request_id or not query_kind or not llm_query:
        return fail_response()

    llm_request = LLMRequest(request_id=request_id,
                             query_kind=query_kind, llm_query=llm_query)

    llm_service = LLMService()
    llm_response = llm_service.invoke_llm_provider(llm_request=llm_request)

    return success_response(llm_response)


def success_response(llm_response):
    response_str = json.dumps(llm_response.to_json()).encode("utf-8")

    return Response(
        content=response_str,
        status_code=status.HTTP_200_OK,
        media_type="application/json"
    )


def fail_response():
    json_body = {}
    json_body["message"] = "bad_request"
    response_str = json.dumps(
        json_body
    ).encode("utf-8")

    return Response(
        content=response_str,
        status_code=status.HTTP_400_BAD_REQUEST,
        media_type="application/json"
    )
