from src.config.app_settings import settings


def test_max_session_seconds_setting_exists_and_defaults_reasonably():
    assert settings.MAX_SESSION_SECONDS > 0
    assert settings.MAX_SESSION_SECONDS <= 3600  # sanity: not accidentally unlimited
