from enum import Enum


class ServiceStatus(str, Enum):
    ACTIVE = "active"
    FAILED = "failed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
