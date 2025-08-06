from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.email_preference import EmailPreference

T = TypeVar("T", bound="UserReadPublic")


@_attrs_define
class UserReadPublic:
    """
    Attributes:
        id (UUID):
        email_preferences (Union[None, list[EmailPreference]]):
        is_active (bool):
    """

    id: UUID
    email_preferences: Union[None, list[EmailPreference]]
    is_active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        email_preferences: Union[None, list[str]]
        if isinstance(self.email_preferences, list):
            email_preferences = []
            for email_preferences_type_0_item_data in self.email_preferences:
                email_preferences_type_0_item = email_preferences_type_0_item_data.value
                email_preferences.append(email_preferences_type_0_item)

        else:
            email_preferences = self.email_preferences

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email_preferences": email_preferences,
                "is_active": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_email_preferences(data: object) -> Union[None, list[EmailPreference]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                email_preferences_type_0 = []
                _email_preferences_type_0 = data
                for email_preferences_type_0_item_data in _email_preferences_type_0:
                    email_preferences_type_0_item = EmailPreference(email_preferences_type_0_item_data)

                    email_preferences_type_0.append(email_preferences_type_0_item)

                return email_preferences_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[EmailPreference]], data)

        email_preferences = _parse_email_preferences(d.pop("email_preferences"))

        is_active = d.pop("is_active")

        user_read_public = cls(
            id=id,
            email_preferences=email_preferences,
            is_active=is_active,
        )

        user_read_public.additional_properties = d
        return user_read_public

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
