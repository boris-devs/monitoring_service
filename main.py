"""Точка сборки приложения: связывает модули и запускает один цикл проверки."""

from __future__ import annotations

import asyncio

from loguru import logger

from logging_setup import setup_logging
from monitor import Monitor
from notifier import Notifier
from services import SERVICES


async def run() -> None:
	setup_logging()
	monitor = Monitor(services=SERVICES, notifier=Notifier())
	results = await monitor.run_once()

	total = len(results)
	failed = sum(1 for r in results if not r.ok)
	logger.info(f"Проверка завершена: всего {total}, с ошибкой {failed}.")


def app() -> None:
	asyncio.run(run())


if __name__ == "__main__":
	app()
