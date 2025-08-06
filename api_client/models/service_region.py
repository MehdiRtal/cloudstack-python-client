from enum import Enum


class ServiceRegion(str, Enum):
    US_EAST_1 = "us-east-1"

    def __str__(self) -> str:
        return str(self.value)
