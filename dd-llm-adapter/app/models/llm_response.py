
class LLMResponse:

    def __init__(self, *, llm_request, raw_response):
        self._llm_request = llm_request
        self._raw_response = raw_response

    @property
    def llm_request(self):
        return self._llm_request

    @property
    def raw_response(self):
        return self._raw_response

# --------------driver----------------------------------------
