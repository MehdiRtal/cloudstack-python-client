from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metrics_cpu_type_0_item import MetricsCpuType0Item
    from ..models.metrics_memory_type_0_item import MetricsMemoryType0Item


T = TypeVar("T", bound="Metrics")


@_attrs_define
class Metrics:
    """
    Attributes:
        cpu (Union[None, Unset, list['MetricsCpuType0Item']]):
        memory (Union[None, Unset, list['MetricsMemoryType0Item']]):
    """

    cpu: Union[None, Unset, list["MetricsCpuType0Item"]] = UNSET
    memory: Union[None, Unset, list["MetricsMemoryType0Item"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.cpu, Unset):
            cpu = UNSET
        elif isinstance(self.cpu, list):
            cpu = []
            for cpu_type_0_item_data in self.cpu:
                cpu_type_0_item = cpu_type_0_item_data.to_dict()
                cpu.append(cpu_type_0_item)

        else:
            cpu = self.cpu

        memory: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.memory, Unset):
            memory = UNSET
        elif isinstance(self.memory, list):
            memory = []
            for memory_type_0_item_data in self.memory:
                memory_type_0_item = memory_type_0_item_data.to_dict()
                memory.append(memory_type_0_item)

        else:
            memory = self.memory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_cpu_type_0_item import MetricsCpuType0Item
        from ..models.metrics_memory_type_0_item import MetricsMemoryType0Item

        d = dict(src_dict)

        def _parse_cpu(data: object) -> Union[None, Unset, list["MetricsCpuType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cpu_type_0 = []
                _cpu_type_0 = data
                for cpu_type_0_item_data in _cpu_type_0:
                    cpu_type_0_item = MetricsCpuType0Item.from_dict(cpu_type_0_item_data)

                    cpu_type_0.append(cpu_type_0_item)

                return cpu_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MetricsCpuType0Item"]], data)

        cpu = _parse_cpu(d.pop("cpu", UNSET))

        def _parse_memory(data: object) -> Union[None, Unset, list["MetricsMemoryType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                memory_type_0 = []
                _memory_type_0 = data
                for memory_type_0_item_data in _memory_type_0:
                    memory_type_0_item = MetricsMemoryType0Item.from_dict(memory_type_0_item_data)

                    memory_type_0.append(memory_type_0_item)

                return memory_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MetricsMemoryType0Item"]], data)

        memory = _parse_memory(d.pop("memory", UNSET))

        metrics = cls(
            cpu=cpu,
            memory=memory,
        )

        metrics.additional_properties = d
        return metrics

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
