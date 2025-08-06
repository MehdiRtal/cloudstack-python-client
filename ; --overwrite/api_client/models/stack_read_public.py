from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_region import ServiceRegion
from ..models.stack_status import StackStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="StackReadPublic")


@_attrs_define
class StackReadPublic:
    """
    Attributes:
        name (str):
        id (UUID):
        status (StackStatus):
        user_id (UUID):
        region (Union[Unset, ServiceRegion]):
    """

    name: str
    id: UUID
    status: StackStatus
    user_id: UUID
    region: Union[Unset, ServiceRegion] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = str(self.id)

        status = self.status.value

        user_id = str(self.user_id)

        region: Union[Unset, str] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "status": status,
                "user_id": user_id,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = UUID(d.pop("id"))

        status = StackStatus(d.pop("status"))

        user_id = UUID(d.pop("user_id"))

        _region = d.pop("region", UNSET)
        region: Union[Unset, ServiceRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = ServiceRegion(_region)

        stack_read_public = cls(
            name=name,
            id=id,
            status=status,
            user_id=user_id,
            region=region,
        )

        stack_read_public.additional_properties = d
        return stack_read_public

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
