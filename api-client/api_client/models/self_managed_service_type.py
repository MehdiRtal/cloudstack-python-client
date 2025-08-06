from enum import Enum


class SelfManagedServiceType(str, Enum):
    FUNCTION = "function"
    GITHUB = "github"
    IMAGE = "image"

    def __str__(self) -> str:
        return str(self.value)
