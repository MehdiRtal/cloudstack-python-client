from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_type import DomainType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainReadPublic")


@_attrs_define
class DomainReadPublic:
    """
    Attributes:
        type_ (DomainType):
        name (str):
        port (int):
        id (UUID):
        service_id (UUID):
        path (Union[Unset, str]):  Default: '/'.
    """

    type_: DomainType
    name: str
    port: int
    id: UUID
    service_id: UUID
    path: Union[Unset, str] = "/"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        port = self.port

        id = str(self.id)

        service_id = str(self.service_id)

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "port": port,
                "id": id,
                "service_id": service_id,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = DomainType(d.pop("type"))

        name = d.pop("name")

        port = d.pop("port")

        id = UUID(d.pop("id"))

        service_id = UUID(d.pop("service_id"))

        path = d.pop("path", UNSET)

        domain_read_public = cls(
            type_=type_,
            name=name,
            port=port,
            id=id,
            service_id=service_id,
            path=path,
        )

        domain_read_public.additional_properties = d
        return domain_read_public

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
