from enum import Enum


class MetricsInterval(str, Enum):
    VALUE_0 = "1h"
    VALUE_1 = "6h"
    VALUE_2 = "1d"
    VALUE_3 = "7d"
    VALUE_4 = "30d"

    def __str__(self) -> str:
        return str(self.value)
