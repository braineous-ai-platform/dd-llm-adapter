#

import json
import urllib.request
from app.models.llm_request import LLMRequest
from app.models.llm_response import LLMResponse


class LLMService:
    def __init__(self):
        pass

    def invoke_llm_provider(self, *, llm_request):
        if (llm_request is None):
            raise ValueError("llm_request cannot be null")

        # TODO: pull from config service components
        url = "http://localhost:11434/api/generate"

        payload = llm_request.llm_query
        data = json.dumps(payload).encode("utf-8")

        request = urllib.request.Request(
            url=url,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        with urllib.request.urlopen(request) as response:
            status = response.status
            body = response.read().decode("utf-8")

            raw_response = json.loads(body)

            success = False
            if status >= 200 and status < 300:
                success = True

        llm_response = LLMResponse(
            llm_request=llm_request, raw_response=raw_response, success=success)

        return llm_response
