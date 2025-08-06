from enum import Enum


class VolumeStatus(str, Enum):
    ACTIVE = "active"
    FAILED = "failed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
