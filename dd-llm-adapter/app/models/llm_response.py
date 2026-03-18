
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

# --------------driver----------------------------------------
