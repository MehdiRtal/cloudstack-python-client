from enum import Enum


class DeploymentStatus(str, Enum):
    BUILDING = "building"
    BUILD_FAILED = "build_failed"
    DEPLOYING = "deploying"
    FAILED = "failed"
    REMOVED = "removed"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
