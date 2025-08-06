from enum import Enum


class ServiceBuilder(str, Enum):
    DOCKERFILE = "dockerfile"
    NIXPACKS = "nixpacks"

    def __str__(self) -> str:
        return str(self.value)
