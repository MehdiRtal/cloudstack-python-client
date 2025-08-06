from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_region import ServiceRegion
from ..models.service_runtime import ServiceRuntime
from ..types import UNSET, Unset

T = TypeVar("T", bound="FunctionServiceCreatePublic")


@_attrs_define
class FunctionServiceCreatePublic:
    """
    Attributes:
        name (str):
        type_ (Literal['function']):
        resources_limit_cpu (float):
        resources_limit_memory (int):
        region (Union[Unset, ServiceRegion]):
        runtime (Union[Unset, ServiceRuntime]):
        serverless (Union[Unset, bool]):  Default: False.
        private_networking (Union[Unset, bool]):  Default: True.
    """

    name: str
    type_: Literal["function"]
    resources_limit_cpu: float
    resources_limit_memory: int
    region: Union[Unset, ServiceRegion] = UNSET
    runtime: Union[Unset, ServiceRuntime] = UNSET
    serverless: Union[Unset, bool] = False
    private_networking: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        resources_limit_cpu = self.resources_limit_cpu

        resources_limit_memory = self.resources_limit_memory

        region: Union[Unset, str] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        runtime: Union[Unset, str] = UNSET
        if not isinstance(self.runtime, Unset):
            runtime = self.runtime.value

        serverless = self.serverless

        private_networking = self.private_networking

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "resources_limit_cpu": resources_limit_cpu,
                "resources_limit_memory": resources_limit_memory,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if serverless is not UNSET:
            field_dict["serverless"] = serverless
        if private_networking is not UNSET:
            field_dict["private_networking"] = private_networking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = cast(Literal["function"], d.pop("type"))
        if type_ != "function":
            raise ValueError(f"type must match const 'function', got '{type_}'")

        resources_limit_cpu = d.pop("resources_limit_cpu")

        resources_limit_memory = d.pop("resources_limit_memory")

        _region = d.pop("region", UNSET)
        region: Union[Unset, ServiceRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = ServiceRegion(_region)

        _runtime = d.pop("runtime", UNSET)
        runtime: Union[Unset, ServiceRuntime]
        if isinstance(_runtime, Unset):
            runtime = UNSET
        else:
            runtime = ServiceRuntime(_runtime)

        serverless = d.pop("serverless", UNSET)

        private_networking = d.pop("private_networking", UNSET)

        function_service_create_public = cls(
            name=name,
            type_=type_,
            resources_limit_cpu=resources_limit_cpu,
            resources_limit_memory=resources_limit_memory,
            region=region,
            runtime=runtime,
            serverless=serverless,
            private_networking=private_networking,
        )

        function_service_create_public.additional_properties = d
        return function_service_create_public

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
