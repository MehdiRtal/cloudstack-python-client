from enum import Enum


class ManagedCredentialsServiceType(str, Enum):
    POSTGRES = "postgres"

    def __str__(self) -> str:
        return str(self.value)
