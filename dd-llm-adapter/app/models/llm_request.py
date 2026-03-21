# LLMRequest is an upstream-owned technical execution envelope carrying correlation metadata,
# execution classification, and an opaque provider-ready JSON payload.

import json


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

    def to_json(self):
        json_obj = {}

        json_obj["requestId"] = self.request_id
        json_obj["queryKind"] = self.query_kind
        json_obj["llmQuery"] = self.llm_query

        return json_obj


# --------------drivers-----------------------------------------------
llm_request = LLMRequest(
    request_id="uuid", query_kind="query_kind", llm_query="llm_query")
print(llm_request.to_json())
