"""Уведомления об ошибках. Отправка в Telegram имитируется через print()"""

from __future__ import annotations

from models import CheckResult


class Notifier:
    def notify(self, result: CheckResult) -> None:
        message = (
            f"Сервис недоступен: {result.service.name} ({result.service.url}). "
            f"{result.error or 'нет ответа'}"
        )
        print(f"Send alert to Telegram: {message}")
