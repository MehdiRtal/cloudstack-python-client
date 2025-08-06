from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VolumeCreatePublic")


@_attrs_define
class VolumeCreatePublic:
    """
    Attributes:
        name (str):
        size (Union[Unset, int]):  Default: 5.
        backup_schedule_cron (Union[None, Unset, str]):
    """

    name: str
    size: Union[Unset, int] = 5
    backup_schedule_cron: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

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

        size = d.pop("size", UNSET)

        def _parse_backup_schedule_cron(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_schedule_cron = _parse_backup_schedule_cron(d.pop("backup_schedule_cron", UNSET))

        volume_create_public = cls(
            name=name,
            size=size,
            backup_schedule_cron=backup_schedule_cron,
        )

        volume_create_public.additional_properties = d
        return volume_create_public

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
