from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_region import ServiceRegion
from ..models.service_status import ServiceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostgresServiceReadCreatePublic")


@_attrs_define
class PostgresServiceReadCreatePublic:
    """
    Attributes:
        name (str):
        id (UUID):
        stack_id (UUID):
        status (ServiceStatus):
        connection_string (str):
        region (Union[Unset, ServiceRegion]):
        type_ (Union[Literal['postgres'], Unset]):  Default: 'postgres'.
    """

    name: str
    id: UUID
    stack_id: UUID
    status: ServiceStatus
    connection_string: str
    region: Union[Unset, ServiceRegion] = UNSET
    type_: Union[Literal["postgres"], Unset] = "postgres"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = str(self.id)

        stack_id = str(self.stack_id)

        status = self.status.value

        connection_string = self.connection_string

        region: Union[Unset, str] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "stack_id": stack_id,
                "status": status,
                "connection_string": connection_string,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = UUID(d.pop("id"))

        stack_id = UUID(d.pop("stack_id"))

        status = ServiceStatus(d.pop("status"))

        connection_string = d.pop("connection_string")

        _region = d.pop("region", UNSET)
        region: Union[Unset, ServiceRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = ServiceRegion(_region)

        type_ = cast(Union[Literal["postgres"], Unset], d.pop("type", UNSET))
        if type_ != "postgres" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'postgres', got '{type_}'")

        postgres_service_read_create_public = cls(
            name=name,
            id=id,
            stack_id=stack_id,
            status=status,
            connection_string=connection_string,
            region=region,
            type_=type_,
        )

        postgres_service_read_create_public.additional_properties = d
        return postgres_service_read_create_public

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
