from enum import Enum


class LogsType(str, Enum):
    BUILD = "build"
    INSTANCES = "instances"

    def __str__(self) -> str:
        return str(self.value)
