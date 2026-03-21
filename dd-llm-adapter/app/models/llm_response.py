from app.models.llm_request import LLMRequest


class LLMResponse:

    def __init__(self, *, llm_request, raw_response, success):
        self._llm_request = llm_request
        self._raw_response = raw_response
        self._success = success

    @property
    def llm_request(self):
        return self._llm_request

    @property
    def raw_response(self):
        return self._raw_response

    @property
    def success(self):
        return self._success

    def __str__(self):
        return f"llm_request: {self._llm_request}, raw_response: {self._raw_response}, success: {self._success}"

    def to_json(self):
        json_object = {}
        json_object["llmRequest"] = self.llm_request.to_json()
        json_object["rawResponse"] = self.raw_response
        json_object["success"] = self.success

        return json_object


# --------------driver----------------------------------------
llm_request = LLMRequest(
    request_id="1", query_kind="reroute_passengers", llm_query="payload")

llm_response = LLMResponse(llm_request=llm_request,
                           raw_response="raw_response", success=True)

print(llm_response.to_json())
