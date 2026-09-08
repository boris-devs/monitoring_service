"""Оркестрирует проверку всех сервисов: запускает Checker, логирует, зовёт Notifier."""

from __future__ import annotations

import asyncio

import aiohttp
from loguru import logger

from checker import Checker
from models import CheckResult
from notifier import Notifier
from services import ServiceConfig


class Monitor:
    def __init__(self, services: list[ServiceConfig], notifier: Notifier) -> None:
        self.services = services
        self.notifier = notifier

    async def run_once(self) -> list[CheckResult]:
        async with aiohttp.ClientSession() as session:
            checker = Checker(session)
            results = await asyncio.gather(*(checker.check(service) for service in self.services))

        for result in results:
            self._handle_result(result)
        return list(results)

    def _handle_result(self, result: CheckResult) -> None:
        if result.ok:
            logger.info(result.as_log_line())
        else:
            logger.error(result.as_log_line())
            self.notifier.notify(result)
