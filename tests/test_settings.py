import os
from quartier_intelligence.settings import Settings


def test_settings_env_variables():
    os.environ["QI_API_KEY"] = "test_api_key"
    os.environ["QI_JWT_ALGORITHM"] = "RS256"
    os.environ["QI_JWT_EXPIRATION"] = "120"

    settings = Settings()

    assert settings.API_KEY == "test_api_key"
    assert settings.JWT_ALGORITHM == "RS256"
    assert settings.JWT_EXPIRATION == 120

    del os.environ["QI_API_KEY"]
    del os.environ["QI_JWT_ALGORITHM"]
    del os.environ["QI_JWT_EXPIRATION"]
