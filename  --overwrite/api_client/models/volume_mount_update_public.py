from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VolumeMountUpdatePublic")


@_attrs_define
class VolumeMountUpdatePublic:
    """
    Attributes:
        mount_path (Union[None, Unset, str]):
    """

    mount_path: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_path: Union[None, Unset, str]
        if isinstance(self.mount_path, Unset):
            mount_path = UNSET
        else:
            mount_path = self.mount_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mount_path is not UNSET:
            field_dict["mount_path"] = mount_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_mount_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mount_path = _parse_mount_path(d.pop("mount_path", UNSET))

        volume_mount_update_public = cls(
            mount_path=mount_path,
        )

        volume_mount_update_public.additional_properties = d
        return volume_mount_update_public

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
