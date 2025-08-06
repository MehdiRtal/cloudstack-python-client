from enum import Enum


class MetricsType(str, Enum):
    CPU = "cpu"
    MEMORY = "memory"

    def __str__(self) -> str:
        return str(self.value)
