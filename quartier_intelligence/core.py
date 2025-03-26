from quartier_intelligence.settings import Settings


class Agent:
    def __init__(self, agent_id: str, tenant_id: str | None = None): ...


class QI:
    def __init__(
        self,
        api_key: str | None = None,
    ):
        self._api_key = api_key
        self._settings = Settings()

    async def get_config(self): ...
