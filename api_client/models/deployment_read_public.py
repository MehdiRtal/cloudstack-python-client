from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deployment_status import DeploymentStatus

T = TypeVar("T", bound="DeploymentReadPublic")


@_attrs_define
class DeploymentReadPublic:
    """
    Attributes:
        id (UUID):
        status (DeploymentStatus):
        service_id (UUID):
    """

    id: UUID
    status: DeploymentStatus
    service_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        service_id = str(self.service_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "service_id": service_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = DeploymentStatus(d.pop("status"))

        service_id = UUID(d.pop("service_id"))

        deployment_read_public = cls(
            id=id,
            status=status,
            service_id=service_id,
        )

        deployment_read_public.additional_properties = d
        return deployment_read_public

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
