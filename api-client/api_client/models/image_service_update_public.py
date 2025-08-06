from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_runtime import ServiceRuntime
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageServiceUpdatePublic")


@_attrs_define
class ImageServiceUpdatePublic:
    """
    Attributes:
        type_ (Union[Literal['image'], Unset]):  Default: 'image'.
        image (Union[None, Unset, str]):
        start_command (Union[None, Unset, str]):
        replicas (Union[None, Unset, int]):
        runtime (Union[None, ServiceRuntime, Unset]):
        serverless (Union[None, Unset, bool]):
        private_networking (Union[None, Unset, bool]):
        resources_limit_cpu (Union[None, Unset, float]):
        resources_limit_memory (Union[None, Unset, int]):
    """

    type_: Union[Literal["image"], Unset] = "image"
    image: Union[None, Unset, str] = UNSET
    start_command: Union[None, Unset, str] = UNSET
    replicas: Union[None, Unset, int] = UNSET
    runtime: Union[None, ServiceRuntime, Unset] = UNSET
    serverless: Union[None, Unset, bool] = UNSET
    private_networking: Union[None, Unset, bool] = UNSET
    resources_limit_cpu: Union[None, Unset, float] = UNSET
    resources_limit_memory: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        start_command: Union[None, Unset, str]
        if isinstance(self.start_command, Unset):
            start_command = UNSET
        else:
            start_command = self.start_command

        replicas: Union[None, Unset, int]
        if isinstance(self.replicas, Unset):
            replicas = UNSET
        else:
            replicas = self.replicas

        runtime: Union[None, Unset, str]
        if isinstance(self.runtime, Unset):
            runtime = UNSET
        elif isinstance(self.runtime, ServiceRuntime):
            runtime = self.runtime.value
        else:
            runtime = self.runtime

        serverless: Union[None, Unset, bool]
        if isinstance(self.serverless, Unset):
            serverless = UNSET
        else:
            serverless = self.serverless

        private_networking: Union[None, Unset, bool]
        if isinstance(self.private_networking, Unset):
            private_networking = UNSET
        else:
            private_networking = self.private_networking

        resources_limit_cpu: Union[None, Unset, float]
        if isinstance(self.resources_limit_cpu, Unset):
            resources_limit_cpu = UNSET
        else:
            resources_limit_cpu = self.resources_limit_cpu

        resources_limit_memory: Union[None, Unset, int]
        if isinstance(self.resources_limit_memory, Unset):
            resources_limit_memory = UNSET
        else:
            resources_limit_memory = self.resources_limit_memory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if image is not UNSET:
            field_dict["image"] = image
        if start_command is not UNSET:
            field_dict["start_command"] = start_command
        if replicas is not UNSET:
            field_dict["replicas"] = replicas
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if serverless is not UNSET:
            field_dict["serverless"] = serverless
        if private_networking is not UNSET:
            field_dict["private_networking"] = private_networking
        if resources_limit_cpu is not UNSET:
            field_dict["resources_limit_cpu"] = resources_limit_cpu
        if resources_limit_memory is not UNSET:
            field_dict["resources_limit_memory"] = resources_limit_memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Union[Literal["image"], Unset], d.pop("type", UNSET))
        if type_ != "image" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'image', got '{type_}'")

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_start_command(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        start_command = _parse_start_command(d.pop("start_command", UNSET))

        def _parse_replicas(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        replicas = _parse_replicas(d.pop("replicas", UNSET))

        def _parse_runtime(data: object) -> Union[None, ServiceRuntime, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                runtime_type_0 = ServiceRuntime(data)

                return runtime_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ServiceRuntime, Unset], data)

        runtime = _parse_runtime(d.pop("runtime", UNSET))

        def _parse_serverless(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        serverless = _parse_serverless(d.pop("serverless", UNSET))

        def _parse_private_networking(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        private_networking = _parse_private_networking(d.pop("private_networking", UNSET))

        def _parse_resources_limit_cpu(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        resources_limit_cpu = _parse_resources_limit_cpu(d.pop("resources_limit_cpu", UNSET))

        def _parse_resources_limit_memory(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        resources_limit_memory = _parse_resources_limit_memory(d.pop("resources_limit_memory", UNSET))

        image_service_update_public = cls(
            type_=type_,
            image=image,
            start_command=start_command,
            replicas=replicas,
            runtime=runtime,
            serverless=serverless,
            private_networking=private_networking,
            resources_limit_cpu=resources_limit_cpu,
            resources_limit_memory=resources_limit_memory,
        )

        image_service_update_public.additional_properties = d
        return image_service_update_public

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
