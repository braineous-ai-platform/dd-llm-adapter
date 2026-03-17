
class LLMExecutionTrace:

    def __init__(self, *, request_id, provider_name, model_name, raw_request, raw_response):
        self._request_id = request_id
        self._provider_name = provider_name
        self._model_name = model_name
        self._raw_request = raw_request
        self._raw_response = raw_response

    @property
    def request_id(self):
        return self._request_id

    @property
    def provider_name(self):
        return self._provider_name

    @property
    def provider_name(self):
        return self._provider_name

    @property
    def provider_name(self):
        return self._provider_name

    @property
    def provider_name(self):
        return self._provider_name
