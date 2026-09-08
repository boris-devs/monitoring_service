from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	LOG_DIR: Path = Path(__file__).parent / "logs"
	LOG_FILE: Path = LOG_DIR / "monitoring.log"

	REQUEST_TIMEOUT: int = 10
	REQUEST_HEADERS: dict = {"User Agent": "Mozilla/5.0 (compatible; MonitoringBot/1.0)"}


settings = Settings()
