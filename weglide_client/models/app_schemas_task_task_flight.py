# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from weglide_client.models.rule_set import RuleSet
from weglide_client.models.task_user import TaskUser
from typing import Optional, Set
from typing_extensions import Self

class AppSchemasTaskTaskFlight(BaseModel):
    """
    AppSchemasTaskTaskFlight
    """ # noqa: E501
    id: StrictInt
    name: Optional[StrictStr] = None
    kind: StrictStr
    penalized_distance: Union[StrictFloat, StrictInt]
    min_distance: Optional[Union[StrictFloat, StrictInt]] = None
    max_distance: Optional[Union[StrictFloat, StrictInt]] = None
    start_on_leg: StrictBool
    closed: StrictBool
    bbox: List[Union[StrictFloat, StrictInt]]
    stars: StrictInt
    from_igcfile: StrictBool
    user: Optional[TaskUser] = None
    ruleset: Optional[RuleSet] = None
    private: StrictBool
    point_features: List[Any]
    __properties: ClassVar[List[str]] = ["id", "name", "kind", "penalized_distance", "min_distance", "max_distance", "start_on_leg", "closed", "bbox", "stars", "from_igcfile", "user", "ruleset", "private", "point_features"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AppSchemasTaskTaskFlight from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if min_distance (nullable) is None
        # and model_fields_set contains the field
        if self.min_distance is None and "min_distance" in self.model_fields_set:
            _dict['min_distance'] = None

        # set to None if max_distance (nullable) is None
        # and model_fields_set contains the field
        if self.max_distance is None and "max_distance" in self.model_fields_set:
            _dict['max_distance'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if ruleset (nullable) is None
        # and model_fields_set contains the field
        if self.ruleset is None and "ruleset" in self.model_fields_set:
            _dict['ruleset'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppSchemasTaskTaskFlight from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "kind": obj.get("kind"),
            "penalized_distance": obj.get("penalized_distance"),
            "min_distance": obj.get("min_distance"),
            "max_distance": obj.get("max_distance"),
            "start_on_leg": obj.get("start_on_leg"),
            "closed": obj.get("closed"),
            "bbox": obj.get("bbox"),
            "stars": obj.get("stars"),
            "from_igcfile": obj.get("from_igcfile"),
            "user": TaskUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "ruleset": obj.get("ruleset"),
            "private": obj.get("private"),
            "point_features": obj.get("point_features")
        })
        return _obj


