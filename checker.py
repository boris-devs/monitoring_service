from __future__ import annotations

import asyncio
from datetime import datetime

import aiohttp

from models import CheckResult
from services import ServiceConfig
from settings import settings


class Checker:
    """Асинхронно опрашивает сервис через переданную aiohttp сессию."""

    def __init__(self, session: aiohttp.ClientSession) -> None:
        self.session = session
        self.timeout = aiohttp.ClientTimeout(total=settings.REQUEST_TIMEOUT)

    async def check(self, service: ServiceConfig) -> CheckResult:
        checked_at = datetime.now()
        try:
            async with self.session.get(
                service.url, headers=settings.REQUEST_HEADERS, timeout=self.timeout
            ) as response:
                ok = response.status == 200
                error = None if ok else (response.reason or "неуспешный код ответа")
                return CheckResult(
                    service=service,
                    checked_at=checked_at,
                    ok=ok,
                    status_code=response.status,
                    error=error,
                )
        except (aiohttp.ClientError, asyncio.TimeoutError) as exc:
            return CheckResult(
                service=service,
                checked_at=checked_at,
                ok=False,
                status_code=None,
                error=str(exc) or exc.__class__.__name__,
            )
