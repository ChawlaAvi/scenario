from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiScenarioEventsBodyType2MessagesItemType2ToolCallsItemFunction")


@_attrs_define
class PostApiScenarioEventsBodyType2MessagesItemType2ToolCallsItemFunction:
    """
    Attributes:
        name (str):
        arguments (str):
    """

    name: str
    arguments: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        arguments = self.arguments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "arguments": arguments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        arguments = d.pop("arguments")

        post_api_scenario_events_body_type_2_messages_item_type_2_tool_calls_item_function = cls(
            name=name,
            arguments=arguments,
        )

        post_api_scenario_events_body_type_2_messages_item_type_2_tool_calls_item_function.additional_properties = d
        return post_api_scenario_events_body_type_2_messages_item_type_2_tool_calls_item_function

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
