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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from weglide_client.models.rule_set import RuleSet
from weglide_client.models.turnpoint_feature import TurnpointFeature
from typing import Optional, Set
from typing_extensions import Self

class TaskCreate(BaseModel):
    """
    TaskCreate
    """ # noqa: E501
    point_features: List[TurnpointFeature]
    name: Optional[StrictStr] = None
    min_time: Optional[StrictInt] = None
    ruleset: Optional[RuleSet] = None
    description: Optional[StrictStr] = None
    private: Optional[StrictBool] = False
    scoring_date: Optional[date] = None
    scoring_airport_id: Optional[StrictInt] = None
    user_group_id: Optional[StrictInt] = None
    start_time: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["point_features", "name", "min_time", "ruleset", "description", "private", "scoring_date", "scoring_airport_id", "user_group_id", "start_time"]

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
        """Create an instance of TaskCreate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in point_features (list)
        _items = []
        if self.point_features:
            for _item_point_features in self.point_features:
                if _item_point_features:
                    _items.append(_item_point_features.to_dict())
            _dict['point_features'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if min_time (nullable) is None
        # and model_fields_set contains the field
        if self.min_time is None and "min_time" in self.model_fields_set:
            _dict['min_time'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if scoring_date (nullable) is None
        # and model_fields_set contains the field
        if self.scoring_date is None and "scoring_date" in self.model_fields_set:
            _dict['scoring_date'] = None

        # set to None if scoring_airport_id (nullable) is None
        # and model_fields_set contains the field
        if self.scoring_airport_id is None and "scoring_airport_id" in self.model_fields_set:
            _dict['scoring_airport_id'] = None

        # set to None if user_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_group_id is None and "user_group_id" in self.model_fields_set:
            _dict['user_group_id'] = None

        # set to None if start_time (nullable) is None
        # and model_fields_set contains the field
        if self.start_time is None and "start_time" in self.model_fields_set:
            _dict['start_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TaskCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "point_features": [TurnpointFeature.from_dict(_item) for _item in obj["point_features"]] if obj.get("point_features") is not None else None,
            "name": obj.get("name"),
            "min_time": obj.get("min_time"),
            "ruleset": obj.get("ruleset"),
            "description": obj.get("description"),
            "private": obj.get("private") if obj.get("private") is not None else False,
            "scoring_date": obj.get("scoring_date"),
            "scoring_airport_id": obj.get("scoring_airport_id"),
            "user_group_id": obj.get("user_group_id"),
            "start_time": obj.get("start_time")
        })
        return _obj


