from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceConfig:
	"""Описание одного проверяемого сервиса"""

	name: str
	url: str