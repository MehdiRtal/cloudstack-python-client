from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.email_preference import EmailPreference
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUpdatePublic")


@_attrs_define
class UserUpdatePublic:
    """
    Attributes:
        email_preferences (Union[None, Unset, list[EmailPreference]]):
    """

    email_preferences: Union[None, Unset, list[EmailPreference]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_preferences: Union[None, Unset, list[str]]
        if isinstance(self.email_preferences, Unset):
            email_preferences = UNSET
        elif isinstance(self.email_preferences, list):
            email_preferences = []
            for email_preferences_type_0_item_data in self.email_preferences:
                email_preferences_type_0_item = email_preferences_type_0_item_data.value
                email_preferences.append(email_preferences_type_0_item)

        else:
            email_preferences = self.email_preferences

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_preferences is not UNSET:
            field_dict["email_preferences"] = email_preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_email_preferences(data: object) -> Union[None, Unset, list[EmailPreference]]:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(Union[None, Unset, list[EmailPreference]], data)

        email_preferences = _parse_email_preferences(d.pop("email_preferences", UNSET))

        user_update_public = cls(
            email_preferences=email_preferences,
        )

        user_update_public.additional_properties = d
        return user_update_public

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
