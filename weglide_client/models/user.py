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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from weglide_client.models.airport_flight import AirportFlight
from weglide_client.models.club import Club
from weglide_client.models.device import Device
from weglide_client.models.flight_collection import FlightCollection
from weglide_client.models.gender import Gender
from weglide_client.models.travel import Travel
from weglide_client.models.waypoint_collection import WaypointCollection
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    User
    """ # noqa: E501
    id: StrictInt
    name: StrictStr
    image: Optional[StrictStr] = None
    badge: Optional[StrictBool] = None
    open_in_seeyou: StrictBool
    comments_allowed: StrictBool
    second_club: Optional[Club] = None
    gender: Gender
    date_joined: datetime
    bio: Optional[StrictStr] = None
    is_junior: StrictBool
    flight_count: StrictInt
    story_count: StrictInt
    total_free_distance: Union[StrictFloat, StrictInt]
    total_flight_duration: Union[StrictFloat, StrictInt]
    home_airport: Optional[AirportFlight] = None
    club: Optional[Club] = None
    avg_speed: Union[StrictFloat, StrictInt]
    avg_glide_speed: Union[StrictFloat, StrictInt]
    avg_glide_detour: Union[StrictFloat, StrictInt]
    copilot_uid: Optional[StrictInt] = None
    first_device: Optional[Device] = None
    public_flight_collection: List[FlightCollection]
    public_waypoint_collection: List[WaypointCollection]
    travel: List[Travel]
    achievement_count: Optional[StrictInt] = None
    message_enabled: StrictBool
    __properties: ClassVar[List[str]] = ["id", "name", "image", "badge", "open_in_seeyou", "comments_allowed", "second_club", "gender", "date_joined", "bio", "is_junior", "flight_count", "story_count", "total_free_distance", "total_flight_duration", "home_airport", "club", "avg_speed", "avg_glide_speed", "avg_glide_detour", "copilot_uid", "first_device", "public_flight_collection", "public_waypoint_collection", "travel", "achievement_count", "message_enabled"]

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
        """Create an instance of User from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of second_club
        if self.second_club:
            _dict['second_club'] = self.second_club.to_dict()
        # override the default output from pydantic by calling `to_dict()` of home_airport
        if self.home_airport:
            _dict['home_airport'] = self.home_airport.to_dict()
        # override the default output from pydantic by calling `to_dict()` of club
        if self.club:
            _dict['club'] = self.club.to_dict()
        # override the default output from pydantic by calling `to_dict()` of first_device
        if self.first_device:
            _dict['first_device'] = self.first_device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in public_flight_collection (list)
        _items = []
        if self.public_flight_collection:
            for _item_public_flight_collection in self.public_flight_collection:
                if _item_public_flight_collection:
                    _items.append(_item_public_flight_collection.to_dict())
            _dict['public_flight_collection'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in public_waypoint_collection (list)
        _items = []
        if self.public_waypoint_collection:
            for _item_public_waypoint_collection in self.public_waypoint_collection:
                if _item_public_waypoint_collection:
                    _items.append(_item_public_waypoint_collection.to_dict())
            _dict['public_waypoint_collection'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in travel (list)
        _items = []
        if self.travel:
            for _item_travel in self.travel:
                if _item_travel:
                    _items.append(_item_travel.to_dict())
            _dict['travel'] = _items
        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict['image'] = None

        # set to None if badge (nullable) is None
        # and model_fields_set contains the field
        if self.badge is None and "badge" in self.model_fields_set:
            _dict['badge'] = None

        # set to None if second_club (nullable) is None
        # and model_fields_set contains the field
        if self.second_club is None and "second_club" in self.model_fields_set:
            _dict['second_club'] = None

        # set to None if bio (nullable) is None
        # and model_fields_set contains the field
        if self.bio is None and "bio" in self.model_fields_set:
            _dict['bio'] = None

        # set to None if home_airport (nullable) is None
        # and model_fields_set contains the field
        if self.home_airport is None and "home_airport" in self.model_fields_set:
            _dict['home_airport'] = None

        # set to None if club (nullable) is None
        # and model_fields_set contains the field
        if self.club is None and "club" in self.model_fields_set:
            _dict['club'] = None

        # set to None if copilot_uid (nullable) is None
        # and model_fields_set contains the field
        if self.copilot_uid is None and "copilot_uid" in self.model_fields_set:
            _dict['copilot_uid'] = None

        # set to None if first_device (nullable) is None
        # and model_fields_set contains the field
        if self.first_device is None and "first_device" in self.model_fields_set:
            _dict['first_device'] = None

        # set to None if achievement_count (nullable) is None
        # and model_fields_set contains the field
        if self.achievement_count is None and "achievement_count" in self.model_fields_set:
            _dict['achievement_count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "image": obj.get("image"),
            "badge": obj.get("badge"),
            "open_in_seeyou": obj.get("open_in_seeyou"),
            "comments_allowed": obj.get("comments_allowed"),
            "second_club": Club.from_dict(obj["second_club"]) if obj.get("second_club") is not None else None,
            "gender": obj.get("gender"),
            "date_joined": obj.get("date_joined"),
            "bio": obj.get("bio"),
            "is_junior": obj.get("is_junior"),
            "flight_count": obj.get("flight_count"),
            "story_count": obj.get("story_count"),
            "total_free_distance": obj.get("total_free_distance"),
            "total_flight_duration": obj.get("total_flight_duration"),
            "home_airport": AirportFlight.from_dict(obj["home_airport"]) if obj.get("home_airport") is not None else None,
            "club": Club.from_dict(obj["club"]) if obj.get("club") is not None else None,
            "avg_speed": obj.get("avg_speed"),
            "avg_glide_speed": obj.get("avg_glide_speed"),
            "avg_glide_detour": obj.get("avg_glide_detour"),
            "copilot_uid": obj.get("copilot_uid"),
            "first_device": Device.from_dict(obj["first_device"]) if obj.get("first_device") is not None else None,
            "public_flight_collection": [FlightCollection.from_dict(_item) for _item in obj["public_flight_collection"]] if obj.get("public_flight_collection") is not None else None,
            "public_waypoint_collection": [WaypointCollection.from_dict(_item) for _item in obj["public_waypoint_collection"]] if obj.get("public_waypoint_collection") is not None else None,
            "travel": [Travel.from_dict(_item) for _item in obj["travel"]] if obj.get("travel") is not None else None,
            "achievement_count": obj.get("achievement_count"),
            "message_enabled": obj.get("message_enabled")
        })
        return _obj


