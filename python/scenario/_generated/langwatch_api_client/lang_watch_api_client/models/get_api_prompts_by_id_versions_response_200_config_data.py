from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_prompts_by_id_versions_response_200_config_data_demonstrations import (
        GetApiPromptsByIdVersionsResponse200ConfigDataDemonstrations,
    )
    from ..models.get_api_prompts_by_id_versions_response_200_config_data_inputs_item import (
        GetApiPromptsByIdVersionsResponse200ConfigDataInputsItem,
    )
    from ..models.get_api_prompts_by_id_versions_response_200_config_data_messages_item import (
        GetApiPromptsByIdVersionsResponse200ConfigDataMessagesItem,
    )
    from ..models.get_api_prompts_by_id_versions_response_200_config_data_outputs_item import (
        GetApiPromptsByIdVersionsResponse200ConfigDataOutputsItem,
    )
    from ..models.get_api_prompts_by_id_versions_response_200_config_data_prompting_technique import (
        GetApiPromptsByIdVersionsResponse200ConfigDataPromptingTechnique,
    )


T = TypeVar("T", bound="GetApiPromptsByIdVersionsResponse200ConfigData")


@_attrs_define
class GetApiPromptsByIdVersionsResponse200ConfigData:
    """
    Attributes:
        prompt (str):
        messages (list['GetApiPromptsByIdVersionsResponse200ConfigDataMessagesItem']):
        inputs (list['GetApiPromptsByIdVersionsResponse200ConfigDataInputsItem']):
        outputs (list['GetApiPromptsByIdVersionsResponse200ConfigDataOutputsItem']):
        model (str):
        demonstrations (GetApiPromptsByIdVersionsResponse200ConfigDataDemonstrations):
        version (Union[Unset, float]):
        temperature (Union[Unset, float]):
        max_tokens (Union[Unset, float]):
        prompting_technique (Union[Unset, GetApiPromptsByIdVersionsResponse200ConfigDataPromptingTechnique]):
    """

    prompt: str
    messages: list["GetApiPromptsByIdVersionsResponse200ConfigDataMessagesItem"]
    inputs: list["GetApiPromptsByIdVersionsResponse200ConfigDataInputsItem"]
    outputs: list["GetApiPromptsByIdVersionsResponse200ConfigDataOutputsItem"]
    model: str
    demonstrations: "GetApiPromptsByIdVersionsResponse200ConfigDataDemonstrations"
    version: Union[Unset, float] = UNSET
    temperature: Union[Unset, float] = UNSET
    max_tokens: Union[Unset, float] = UNSET
    prompting_technique: Union[Unset, "GetApiPromptsByIdVersionsResponse200ConfigDataPromptingTechnique"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)

        outputs = []
        for outputs_item_data in self.outputs:
            outputs_item = outputs_item_data.to_dict()
            outputs.append(outputs_item)

        model = self.model

        demonstrations = self.demonstrations.to_dict()

        version = self.version

        temperature = self.temperature

        max_tokens = self.max_tokens

        prompting_technique: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prompting_technique, Unset):
            prompting_technique = self.prompting_technique.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
                "messages": messages,
                "inputs": inputs,
                "outputs": outputs,
                "model": model,
                "demonstrations": demonstrations,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if prompting_technique is not UNSET:
            field_dict["prompting_technique"] = prompting_technique

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_prompts_by_id_versions_response_200_config_data_demonstrations import (
            GetApiPromptsByIdVersionsResponse200ConfigDataDemonstrations,
        )
        from ..models.get_api_prompts_by_id_versions_response_200_config_data_inputs_item import (
            GetApiPromptsByIdVersionsResponse200ConfigDataInputsItem,
        )
        from ..models.get_api_prompts_by_id_versions_response_200_config_data_messages_item import (
            GetApiPromptsByIdVersionsResponse200ConfigDataMessagesItem,
        )
        from ..models.get_api_prompts_by_id_versions_response_200_config_data_outputs_item import (
            GetApiPromptsByIdVersionsResponse200ConfigDataOutputsItem,
        )
        from ..models.get_api_prompts_by_id_versions_response_200_config_data_prompting_technique import (
            GetApiPromptsByIdVersionsResponse200ConfigDataPromptingTechnique,
        )

        d = dict(src_dict)
        prompt = d.pop("prompt")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = GetApiPromptsByIdVersionsResponse200ConfigDataMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in _inputs:
            inputs_item = GetApiPromptsByIdVersionsResponse200ConfigDataInputsItem.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        outputs = []
        _outputs = d.pop("outputs")
        for outputs_item_data in _outputs:
            outputs_item = GetApiPromptsByIdVersionsResponse200ConfigDataOutputsItem.from_dict(outputs_item_data)

            outputs.append(outputs_item)

        model = d.pop("model")

        demonstrations = GetApiPromptsByIdVersionsResponse200ConfigDataDemonstrations.from_dict(d.pop("demonstrations"))

        version = d.pop("version", UNSET)

        temperature = d.pop("temperature", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        _prompting_technique = d.pop("prompting_technique", UNSET)
        prompting_technique: Union[Unset, GetApiPromptsByIdVersionsResponse200ConfigDataPromptingTechnique]
        if isinstance(_prompting_technique, Unset):
            prompting_technique = UNSET
        else:
            prompting_technique = GetApiPromptsByIdVersionsResponse200ConfigDataPromptingTechnique.from_dict(
                _prompting_technique
            )

        get_api_prompts_by_id_versions_response_200_config_data = cls(
            prompt=prompt,
            messages=messages,
            inputs=inputs,
            outputs=outputs,
            model=model,
            demonstrations=demonstrations,
            version=version,
            temperature=temperature,
            max_tokens=max_tokens,
            prompting_technique=prompting_technique,
        )

        get_api_prompts_by_id_versions_response_200_config_data.additional_properties = d
        return get_api_prompts_by_id_versions_response_200_config_data

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
