from enum import Enum


class ServiceRuntime(str, Enum):
    DOCKER = "docker"
    WASM = "wasm"

    def __str__(self) -> str:
        return str(self.value)
