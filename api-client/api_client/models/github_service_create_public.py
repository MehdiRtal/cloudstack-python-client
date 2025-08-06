from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_builder import ServiceBuilder
from ..models.service_region import ServiceRegion
from ..models.service_runtime import ServiceRuntime
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubServiceCreatePublic")


@_attrs_define
class GithubServiceCreatePublic:
    """
    Attributes:
        name (str):
        type_ (Literal['github']):
        resources_limit_cpu (float):
        resources_limit_memory (int):
        repo (str):
        branch (str):
        region (Union[Unset, ServiceRegion]):
        runtime (Union[Unset, ServiceRuntime]):
        serverless (Union[Unset, bool]):  Default: False.
        private_networking (Union[Unset, bool]):  Default: True.
        builder (Union[Unset, ServiceBuilder]):
        watch_paths (Union[Unset, list[str]]):
        build_path (Union[Unset, str]):  Default: './'.
        start_command (Union[None, Unset, str]):
        build_command (Union[None, Unset, str]):
        replicas (Union[Unset, int]):  Default: 1.
        github_installation_id (Union[None, Unset, int]):
    """

    name: str
    type_: Literal["github"]
    resources_limit_cpu: float
    resources_limit_memory: int
    repo: str
    branch: str
    region: Union[Unset, ServiceRegion] = UNSET
    runtime: Union[Unset, ServiceRuntime] = UNSET
    serverless: Union[Unset, bool] = False
    private_networking: Union[Unset, bool] = True
    builder: Union[Unset, ServiceBuilder] = UNSET
    watch_paths: Union[Unset, list[str]] = UNSET
    build_path: Union[Unset, str] = "./"
    start_command: Union[None, Unset, str] = UNSET
    build_command: Union[None, Unset, str] = UNSET
    replicas: Union[Unset, int] = 1
    github_installation_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        resources_limit_cpu = self.resources_limit_cpu

        resources_limit_memory = self.resources_limit_memory

        repo = self.repo

        branch = self.branch

        region: Union[Unset, str] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        runtime: Union[Unset, str] = UNSET
        if not isinstance(self.runtime, Unset):
            runtime = self.runtime.value

        serverless = self.serverless

        private_networking = self.private_networking

        builder: Union[Unset, str] = UNSET
        if not isinstance(self.builder, Unset):
            builder = self.builder.value

        watch_paths: Union[Unset, list[str]] = UNSET
        if not isinstance(self.watch_paths, Unset):
            watch_paths = self.watch_paths

        build_path = self.build_path

        start_command: Union[None, Unset, str]
        if isinstance(self.start_command, Unset):
            start_command = UNSET
        else:
            start_command = self.start_command

        build_command: Union[None, Unset, str]
        if isinstance(self.build_command, Unset):
            build_command = UNSET
        else:
            build_command = self.build_command

        replicas = self.replicas

        github_installation_id: Union[None, Unset, int]
        if isinstance(self.github_installation_id, Unset):
            github_installation_id = UNSET
        else:
            github_installation_id = self.github_installation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "resources_limit_cpu": resources_limit_cpu,
                "resources_limit_memory": resources_limit_memory,
                "repo": repo,
                "branch": branch,
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
        if builder is not UNSET:
            field_dict["builder"] = builder
        if watch_paths is not UNSET:
            field_dict["watch_paths"] = watch_paths
        if build_path is not UNSET:
            field_dict["build_path"] = build_path
        if start_command is not UNSET:
            field_dict["start_command"] = start_command
        if build_command is not UNSET:
            field_dict["build_command"] = build_command
        if replicas is not UNSET:
            field_dict["replicas"] = replicas
        if github_installation_id is not UNSET:
            field_dict["github_installation_id"] = github_installation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = cast(Literal["github"], d.pop("type"))
        if type_ != "github":
            raise ValueError(f"type must match const 'github', got '{type_}'")

        resources_limit_cpu = d.pop("resources_limit_cpu")

        resources_limit_memory = d.pop("resources_limit_memory")

        repo = d.pop("repo")

        branch = d.pop("branch")

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

        _builder = d.pop("builder", UNSET)
        builder: Union[Unset, ServiceBuilder]
        if isinstance(_builder, Unset):
            builder = UNSET
        else:
            builder = ServiceBuilder(_builder)

        watch_paths = cast(list[str], d.pop("watch_paths", UNSET))

        build_path = d.pop("build_path", UNSET)

        def _parse_start_command(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        start_command = _parse_start_command(d.pop("start_command", UNSET))

        def _parse_build_command(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        build_command = _parse_build_command(d.pop("build_command", UNSET))

        replicas = d.pop("replicas", UNSET)

        def _parse_github_installation_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        github_installation_id = _parse_github_installation_id(d.pop("github_installation_id", UNSET))

        github_service_create_public = cls(
            name=name,
            type_=type_,
            resources_limit_cpu=resources_limit_cpu,
            resources_limit_memory=resources_limit_memory,
            repo=repo,
            branch=branch,
            region=region,
            runtime=runtime,
            serverless=serverless,
            private_networking=private_networking,
            builder=builder,
            watch_paths=watch_paths,
            build_path=build_path,
            start_command=start_command,
            build_command=build_command,
            replicas=replicas,
            github_installation_id=github_installation_id,
        )

        github_service_create_public.additional_properties = d
        return github_service_create_public

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
