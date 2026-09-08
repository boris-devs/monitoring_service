from __future__ import annotations

from dto import ServiceConfig

SERVICES: list[ServiceConfig] = [
	ServiceConfig(name="FormIt", url="https://formit.fake"),
	ServiceConfig(name="LeadSync", url="https://leadsync.fake"),
	ServiceConfig(name="Ozon", url="https://www.ozon.ru"),
	ServiceConfig(name="Avito", url="https://www.avito.ru"),
]
