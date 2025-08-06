from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_builder import ServiceBuilder
from ..models.service_runtime import ServiceRuntime
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubServiceUpdatePublic")


@_attrs_define
class GithubServiceUpdatePublic:
    """
    Attributes:
        type_ (Union[Literal['github'], Unset]):  Default: 'github'.
        repo (Union[None, Unset, str]):
        branch (Union[None, Unset, str]):
        builder (Union[None, ServiceBuilder, Unset]):
        watch_paths (Union[None, Unset, list[str]]):
        build_path (Union[None, Unset, str]):
        start_command (Union[None, Unset, str]):
        build_command (Union[None, Unset, str]):
        replicas (Union[None, Unset, int]):
        github_installation_id (Union[None, Unset, int]):
        runtime (Union[None, ServiceRuntime, Unset]):
        serverless (Union[None, Unset, bool]):
        private_networking (Union[None, Unset, bool]):
        resources_limit_cpu (Union[None, Unset, float]):
        resources_limit_memory (Union[None, Unset, int]):
    """

    type_: Union[Literal["github"], Unset] = "github"
    repo: Union[None, Unset, str] = UNSET
    branch: Union[None, Unset, str] = UNSET
    builder: Union[None, ServiceBuilder, Unset] = UNSET
    watch_paths: Union[None, Unset, list[str]] = UNSET
    build_path: Union[None, Unset, str] = UNSET
    start_command: Union[None, Unset, str] = UNSET
    build_command: Union[None, Unset, str] = UNSET
    replicas: Union[None, Unset, int] = UNSET
    github_installation_id: Union[None, Unset, int] = UNSET
    runtime: Union[None, ServiceRuntime, Unset] = UNSET
    serverless: Union[None, Unset, bool] = UNSET
    private_networking: Union[None, Unset, bool] = UNSET
    resources_limit_cpu: Union[None, Unset, float] = UNSET
    resources_limit_memory: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        repo: Union[None, Unset, str]
        if isinstance(self.repo, Unset):
            repo = UNSET
        else:
            repo = self.repo

        branch: Union[None, Unset, str]
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        builder: Union[None, Unset, str]
        if isinstance(self.builder, Unset):
            builder = UNSET
        elif isinstance(self.builder, ServiceBuilder):
            builder = self.builder.value
        else:
            builder = self.builder

        watch_paths: Union[None, Unset, list[str]]
        if isinstance(self.watch_paths, Unset):
            watch_paths = UNSET
        elif isinstance(self.watch_paths, list):
            watch_paths = self.watch_paths

        else:
            watch_paths = self.watch_paths

        build_path: Union[None, Unset, str]
        if isinstance(self.build_path, Unset):
            build_path = UNSET
        else:
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

        replicas: Union[None, Unset, int]
        if isinstance(self.replicas, Unset):
            replicas = UNSET
        else:
            replicas = self.replicas

        github_installation_id: Union[None, Unset, int]
        if isinstance(self.github_installation_id, Unset):
            github_installation_id = UNSET
        else:
            github_installation_id = self.github_installation_id

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
        if repo is not UNSET:
            field_dict["repo"] = repo
        if branch is not UNSET:
            field_dict["branch"] = branch
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
        type_ = cast(Union[Literal["github"], Unset], d.pop("type", UNSET))
        if type_ != "github" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'github', got '{type_}'")

        def _parse_repo(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        repo = _parse_repo(d.pop("repo", UNSET))

        def _parse_branch(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        branch = _parse_branch(d.pop("branch", UNSET))

        def _parse_builder(data: object) -> Union[None, ServiceBuilder, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                builder_type_0 = ServiceBuilder(data)

                return builder_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ServiceBuilder, Unset], data)

        builder = _parse_builder(d.pop("builder", UNSET))

        def _parse_watch_paths(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                watch_paths_type_0 = cast(list[str], data)

                return watch_paths_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        watch_paths = _parse_watch_paths(d.pop("watch_paths", UNSET))

        def _parse_build_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        build_path = _parse_build_path(d.pop("build_path", UNSET))

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

        def _parse_replicas(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        replicas = _parse_replicas(d.pop("replicas", UNSET))

        def _parse_github_installation_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        github_installation_id = _parse_github_installation_id(d.pop("github_installation_id", UNSET))

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

        github_service_update_public = cls(
            type_=type_,
            repo=repo,
            branch=branch,
            builder=builder,
            watch_paths=watch_paths,
            build_path=build_path,
            start_command=start_command,
            build_command=build_command,
            replicas=replicas,
            github_installation_id=github_installation_id,
            runtime=runtime,
            serverless=serverless,
            private_networking=private_networking,
            resources_limit_cpu=resources_limit_cpu,
            resources_limit_memory=resources_limit_memory,
        )

        github_service_update_public.additional_properties = d
        return github_service_update_public

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
