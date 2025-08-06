from enum import Enum


class EmailPreference(str, Enum):
    ACCOUNT = "account"
    SECURITY = "security"

    def __str__(self) -> str:
        return str(self.value)
