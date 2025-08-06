from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VolumeMountReadPublic")


@_attrs_define
class VolumeMountReadPublic:
    """
    Attributes:
        mount_path (str):
        volume_id (UUID):
        id (UUID):
        service_id (UUID):
    """

    mount_path: str
    volume_id: UUID
    id: UUID
    service_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_path = self.mount_path

        volume_id = str(self.volume_id)

        id = str(self.id)

        service_id = str(self.service_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mount_path": mount_path,
                "volume_id": volume_id,
                "id": id,
                "service_id": service_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mount_path = d.pop("mount_path")

        volume_id = UUID(d.pop("volume_id"))

        id = UUID(d.pop("id"))

        service_id = UUID(d.pop("service_id"))

        volume_mount_read_public = cls(
            mount_path=mount_path,
            volume_id=volume_id,
            id=id,
            service_id=service_id,
        )

        volume_mount_read_public.additional_properties = d
        return volume_mount_read_public

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
