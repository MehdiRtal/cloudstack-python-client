from enum import Enum


class DomainType(str, Enum):
    CUSTOM = "custom"
    SUBDOMAIN = "subdomain"

    def __str__(self) -> str:
        return str(self.value)
