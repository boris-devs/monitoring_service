from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from services import ServiceConfig


@dataclass
class CheckResult:
    """Результат проверки одного сервиса."""

    service: ServiceConfig
    checked_at: datetime
    ok: bool
    status_code: Optional[int]
    error: Optional[str] = None

    def as_log_line(self) -> str:
        code = self.status_code if self.status_code is not None else "Нет ответа"
        status = "OK" if self.ok else "ERROR"
        line = (
            f"Дата={self.checked_at.isoformat(timespec='seconds')} | "
            f"Сервис={self.service.name} | url={self.service.url} | "
            f"Статус={status} | Код ответа={code}"
        )
        if self.error:
            line += f" | причина={self.error}"
        return line
