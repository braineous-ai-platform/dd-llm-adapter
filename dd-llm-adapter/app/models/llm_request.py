
# LLMRequest is an upstream-owned technical execution envelope carrying correlation metadata,
# execution classification, and an opaque provider-ready JSON payload.

class LLMRequest:

    def __init__(self, *, request_id, query_kind, llm_query):
        self._request_id = request_id
        self._query_kind = query_kind
        self._llm_query = llm_query

    @property
    def request_id(self):
        return self._request_id

    @property
    def query_kind(self):
        return self._query_kind

    @property
    def llm_query(self):
        return self._llm_query

    def __str__(self):
        return f"request_id: {self._request_id}, query_kind: {self._query_kind}, llm_query:{self._llm_query}"


# --------------drivers-----------------------------------------------
