
class LlmProviderConfig:

    def __init__(self, *, provider_name, model_name, base_url, timeout_seconds):
        self._provider_name = provider_name
        self._model_name = model_name
        self._base_url = base_url
        self._timeout_seconds = timeout_seconds

    @property
    def provider_name(self):
        return self._provider_name

    @property
    def model_name(self):
        return self._model_name

    @property
    def base_url(self):
        return self._base_url

    @property
    def timeout_seconds(self):
        return self._timeout_seconds
