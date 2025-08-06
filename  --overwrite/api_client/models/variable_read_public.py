from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VariableReadPublic")


@_attrs_define
class VariableReadPublic:
    """
    Attributes:
        name (str):
        id (UUID):
        service_id (UUID):
        read_only (bool):
        computed_value (str):
        sealed (Union[Unset, bool]):  Default: False.
    """

    name: str
    id: UUID
    service_id: UUID
    read_only: bool
    computed_value: str
    sealed: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = str(self.id)

        service_id = str(self.service_id)

        read_only = self.read_only

        computed_value = self.computed_value

        sealed = self.sealed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "service_id": service_id,
                "read_only": read_only,
                "computed_value": computed_value,
            }
        )
        if sealed is not UNSET:
            field_dict["sealed"] = sealed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = UUID(d.pop("id"))

        service_id = UUID(d.pop("service_id"))

        read_only = d.pop("read_only")

        computed_value = d.pop("computed_value")

        sealed = d.pop("sealed", UNSET)

        variable_read_public = cls(
            name=name,
            id=id,
            service_id=service_id,
            read_only=read_only,
            computed_value=computed_value,
            sealed=sealed,
        )

        variable_read_public.additional_properties = d
        return variable_read_public

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
