from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.volume_status import VolumeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="VolumeReadPublic")


@_attrs_define
class VolumeReadPublic:
    """
    Attributes:
        name (str):
        id (UUID):
        status (VolumeStatus):
        stack_id (UUID):
        size (Union[Unset, int]):  Default: 5.
        backup_schedule_cron (Union[None, Unset, str]):
    """

    name: str
    id: UUID
    status: VolumeStatus
    stack_id: UUID
    size: Union[Unset, int] = 5
    backup_schedule_cron: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = str(self.id)

        status = self.status.value

        stack_id = str(self.stack_id)

        size = self.size

        backup_schedule_cron: Union[None, Unset, str]
        if isinstance(self.backup_schedule_cron, Unset):
            backup_schedule_cron = UNSET
        else:
            backup_schedule_cron = self.backup_schedule_cron

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "status": status,
                "stack_id": stack_id,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if backup_schedule_cron is not UNSET:
            field_dict["backup_schedule_cron"] = backup_schedule_cron

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = UUID(d.pop("id"))

        status = VolumeStatus(d.pop("status"))

        stack_id = UUID(d.pop("stack_id"))

        size = d.pop("size", UNSET)

        def _parse_backup_schedule_cron(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_schedule_cron = _parse_backup_schedule_cron(d.pop("backup_schedule_cron", UNSET))

        volume_read_public = cls(
            name=name,
            id=id,
            status=status,
            stack_id=stack_id,
            size=size,
            backup_schedule_cron=backup_schedule_cron,
        )

        volume_read_public.additional_properties = d
        return volume_read_public

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
