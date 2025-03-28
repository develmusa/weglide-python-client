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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from weglide_client.models.aircraft_base import AircraftBase
from weglide_client.models.club_flight import ClubFlight
from weglide_client.models.flight_contest import FlightContest
from weglide_client.models.user_with_image import UserWithImage
from typing import Optional, Set
from typing_extensions import Self

class FlightRankList(BaseModel):
    """
    FlightRankList
    """ # noqa: E501
    id: StrictInt
    user: UserWithImage
    co_user: Optional[UserWithImage] = None
    co_user_name: Optional[StrictStr] = None
    custom_takeoff_airport: Dict[str, Any]
    aircraft: Optional[AircraftBase] = None
    club: Optional[ClubFlight] = None
    media_info: Optional[StrictStr] = None
    takeoff_time: datetime
    landing_time: datetime
    scoring_date: date
    bbox: List[Union[StrictFloat, StrictInt]]
    junior: StrictBool
    dmst_index: Optional[StrictInt] = None
    story_var_size: List[StrictStr]
    rank: StrictBool
    contest: Optional[FlightContest] = None
    __properties: ClassVar[List[str]] = ["id", "user", "co_user", "co_user_name", "custom_takeoff_airport", "aircraft", "club", "media_info", "takeoff_time", "landing_time", "scoring_date", "bbox", "junior", "dmst_index", "story_var_size", "rank", "contest"]

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
        """Create an instance of FlightRankList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of co_user
        if self.co_user:
            _dict['co_user'] = self.co_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aircraft
        if self.aircraft:
            _dict['aircraft'] = self.aircraft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of club
        if self.club:
            _dict['club'] = self.club.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contest
        if self.contest:
            _dict['contest'] = self.contest.to_dict()
        # set to None if co_user (nullable) is None
        # and model_fields_set contains the field
        if self.co_user is None and "co_user" in self.model_fields_set:
            _dict['co_user'] = None

        # set to None if co_user_name (nullable) is None
        # and model_fields_set contains the field
        if self.co_user_name is None and "co_user_name" in self.model_fields_set:
            _dict['co_user_name'] = None

        # set to None if aircraft (nullable) is None
        # and model_fields_set contains the field
        if self.aircraft is None and "aircraft" in self.model_fields_set:
            _dict['aircraft'] = None

        # set to None if club (nullable) is None
        # and model_fields_set contains the field
        if self.club is None and "club" in self.model_fields_set:
            _dict['club'] = None

        # set to None if media_info (nullable) is None
        # and model_fields_set contains the field
        if self.media_info is None and "media_info" in self.model_fields_set:
            _dict['media_info'] = None

        # set to None if dmst_index (nullable) is None
        # and model_fields_set contains the field
        if self.dmst_index is None and "dmst_index" in self.model_fields_set:
            _dict['dmst_index'] = None

        # set to None if contest (nullable) is None
        # and model_fields_set contains the field
        if self.contest is None and "contest" in self.model_fields_set:
            _dict['contest'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlightRankList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "user": UserWithImage.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "co_user": UserWithImage.from_dict(obj["co_user"]) if obj.get("co_user") is not None else None,
            "co_user_name": obj.get("co_user_name"),
            "custom_takeoff_airport": obj.get("custom_takeoff_airport"),
            "aircraft": AircraftBase.from_dict(obj["aircraft"]) if obj.get("aircraft") is not None else None,
            "club": ClubFlight.from_dict(obj["club"]) if obj.get("club") is not None else None,
            "media_info": obj.get("media_info"),
            "takeoff_time": obj.get("takeoff_time"),
            "landing_time": obj.get("landing_time"),
            "scoring_date": obj.get("scoring_date"),
            "bbox": obj.get("bbox"),
            "junior": obj.get("junior"),
            "dmst_index": obj.get("dmst_index"),
            "story_var_size": obj.get("story_var_size"),
            "rank": obj.get("rank"),
            "contest": FlightContest.from_dict(obj["contest"]) if obj.get("contest") is not None else None
        })
        return _obj


