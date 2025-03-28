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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from weglide_client.models.app_schemas_task_score_task_flight import AppSchemasTaskScoreTaskFlight
from typing import Optional, Set
from typing_extensions import Self

class TaskScoreFlight(BaseModel):
    """
    TaskScoreFlight
    """ # noqa: E501
    id: StrictInt
    flight_id: StrictInt
    distance: Union[StrictFloat, StrictInt]
    points: Union[StrictFloat, StrictInt]
    c_points: Optional[Union[StrictFloat, StrictInt]] = None
    gp_points: Optional[StrictInt] = None
    speed: Union[StrictFloat, StrictInt]
    start_time: datetime
    end_time: datetime
    start_alt: StrictInt
    end_alt: StrictInt
    declared: StrictBool
    rank: Optional[StrictInt] = None
    personal_rank: Optional[StrictInt] = None
    wind_speed: Optional[Union[StrictFloat, StrictInt]] = None
    wind_direction: Optional[StrictInt] = None
    path: List[datetime]
    task: AppSchemasTaskScoreTaskFlight
    __properties: ClassVar[List[str]] = ["id", "flight_id", "distance", "points", "c_points", "gp_points", "speed", "start_time", "end_time", "start_alt", "end_alt", "declared", "rank", "personal_rank", "wind_speed", "wind_direction", "path", "task"]

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
        """Create an instance of TaskScoreFlight from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of task
        if self.task:
            _dict['task'] = self.task.to_dict()
        # set to None if c_points (nullable) is None
        # and model_fields_set contains the field
        if self.c_points is None and "c_points" in self.model_fields_set:
            _dict['c_points'] = None

        # set to None if gp_points (nullable) is None
        # and model_fields_set contains the field
        if self.gp_points is None and "gp_points" in self.model_fields_set:
            _dict['gp_points'] = None

        # set to None if rank (nullable) is None
        # and model_fields_set contains the field
        if self.rank is None and "rank" in self.model_fields_set:
            _dict['rank'] = None

        # set to None if personal_rank (nullable) is None
        # and model_fields_set contains the field
        if self.personal_rank is None and "personal_rank" in self.model_fields_set:
            _dict['personal_rank'] = None

        # set to None if wind_speed (nullable) is None
        # and model_fields_set contains the field
        if self.wind_speed is None and "wind_speed" in self.model_fields_set:
            _dict['wind_speed'] = None

        # set to None if wind_direction (nullable) is None
        # and model_fields_set contains the field
        if self.wind_direction is None and "wind_direction" in self.model_fields_set:
            _dict['wind_direction'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TaskScoreFlight from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "flight_id": obj.get("flight_id"),
            "distance": obj.get("distance"),
            "points": obj.get("points"),
            "c_points": obj.get("c_points"),
            "gp_points": obj.get("gp_points"),
            "speed": obj.get("speed"),
            "start_time": obj.get("start_time"),
            "end_time": obj.get("end_time"),
            "start_alt": obj.get("start_alt"),
            "end_alt": obj.get("end_alt"),
            "declared": obj.get("declared"),
            "rank": obj.get("rank"),
            "personal_rank": obj.get("personal_rank"),
            "wind_speed": obj.get("wind_speed"),
            "wind_direction": obj.get("wind_direction"),
            "path": obj.get("path"),
            "task": AppSchemasTaskScoreTaskFlight.from_dict(obj["task"]) if obj.get("task") is not None else None
        })
        return _obj


