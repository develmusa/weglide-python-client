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
from weglide_client.models.airport_flight import AirportFlight
from weglide_client.models.club import Club
from weglide_client.models.device import Device
from weglide_client.models.flight_collection import FlightCollection
from weglide_client.models.gender import Gender
from weglide_client.models.travel import Travel
from weglide_client.models.user_group_simple import UserGroupSimple
from weglide_client.models.waypoint_collection import WaypointCollection
from typing import Optional, Set
from typing_extensions import Self

class UserInDB(BaseModel):
    """
    UserInDB
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
    flight_collection: List[FlightCollection]
    waypoint_collection: List[WaypointCollection]
    travel: List[Travel]
    achievement_count: Optional[StrictInt] = None
    message_enabled: StrictBool
    email: StrictStr
    date_of_birth: date
    is_active: StrictBool
    is_early_bird: StrictBool
    is_live_banned: StrictBool
    is_superuser: StrictBool
    skysight_email: Optional[StrictStr] = None
    frontend_subscription: Optional[Dict[str, Any]] = None
    xcsoar_token: Optional[StrictStr] = None
    trial_available: Optional[StrictBool] = None
    flight_notification: StrictBool
    comment_notification: StrictBool
    follower_notification: StrictBool
    magazine_notification: StrictBool
    live_competition_create: Optional[StrictInt] = None
    ssa_id: Optional[StrictInt] = None
    copilot_status: Optional[StrictInt] = None
    unit: StrictStr
    language: StrictStr
    custom_filter: Optional[List[Dict[str, Any]]] = None
    user_group: List[UserGroupSimple]
    newsletter_language: Optional[StrictStr] = None
    magazine_language: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "name", "image", "badge", "open_in_seeyou", "comments_allowed", "second_club", "gender", "date_joined", "bio", "is_junior", "flight_count", "story_count", "total_free_distance", "total_flight_duration", "home_airport", "club", "avg_speed", "avg_glide_speed", "avg_glide_detour", "copilot_uid", "first_device", "flight_collection", "waypoint_collection", "travel", "achievement_count", "message_enabled", "email", "date_of_birth", "is_active", "is_early_bird", "is_live_banned", "is_superuser", "skysight_email", "frontend_subscription", "xcsoar_token", "trial_available", "flight_notification", "comment_notification", "follower_notification", "magazine_notification", "live_competition_create", "ssa_id", "copilot_status", "unit", "language", "custom_filter", "user_group", "newsletter_language", "magazine_language"]

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
        """Create an instance of UserInDB from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in flight_collection (list)
        _items = []
        if self.flight_collection:
            for _item_flight_collection in self.flight_collection:
                if _item_flight_collection:
                    _items.append(_item_flight_collection.to_dict())
            _dict['flight_collection'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in waypoint_collection (list)
        _items = []
        if self.waypoint_collection:
            for _item_waypoint_collection in self.waypoint_collection:
                if _item_waypoint_collection:
                    _items.append(_item_waypoint_collection.to_dict())
            _dict['waypoint_collection'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in travel (list)
        _items = []
        if self.travel:
            for _item_travel in self.travel:
                if _item_travel:
                    _items.append(_item_travel.to_dict())
            _dict['travel'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in user_group (list)
        _items = []
        if self.user_group:
            for _item_user_group in self.user_group:
                if _item_user_group:
                    _items.append(_item_user_group.to_dict())
            _dict['user_group'] = _items
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

        # set to None if skysight_email (nullable) is None
        # and model_fields_set contains the field
        if self.skysight_email is None and "skysight_email" in self.model_fields_set:
            _dict['skysight_email'] = None

        # set to None if frontend_subscription (nullable) is None
        # and model_fields_set contains the field
        if self.frontend_subscription is None and "frontend_subscription" in self.model_fields_set:
            _dict['frontend_subscription'] = None

        # set to None if xcsoar_token (nullable) is None
        # and model_fields_set contains the field
        if self.xcsoar_token is None and "xcsoar_token" in self.model_fields_set:
            _dict['xcsoar_token'] = None

        # set to None if trial_available (nullable) is None
        # and model_fields_set contains the field
        if self.trial_available is None and "trial_available" in self.model_fields_set:
            _dict['trial_available'] = None

        # set to None if live_competition_create (nullable) is None
        # and model_fields_set contains the field
        if self.live_competition_create is None and "live_competition_create" in self.model_fields_set:
            _dict['live_competition_create'] = None

        # set to None if ssa_id (nullable) is None
        # and model_fields_set contains the field
        if self.ssa_id is None and "ssa_id" in self.model_fields_set:
            _dict['ssa_id'] = None

        # set to None if copilot_status (nullable) is None
        # and model_fields_set contains the field
        if self.copilot_status is None and "copilot_status" in self.model_fields_set:
            _dict['copilot_status'] = None

        # set to None if custom_filter (nullable) is None
        # and model_fields_set contains the field
        if self.custom_filter is None and "custom_filter" in self.model_fields_set:
            _dict['custom_filter'] = None

        # set to None if newsletter_language (nullable) is None
        # and model_fields_set contains the field
        if self.newsletter_language is None and "newsletter_language" in self.model_fields_set:
            _dict['newsletter_language'] = None

        # set to None if magazine_language (nullable) is None
        # and model_fields_set contains the field
        if self.magazine_language is None and "magazine_language" in self.model_fields_set:
            _dict['magazine_language'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserInDB from a dict"""
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
            "flight_collection": [FlightCollection.from_dict(_item) for _item in obj["flight_collection"]] if obj.get("flight_collection") is not None else None,
            "waypoint_collection": [WaypointCollection.from_dict(_item) for _item in obj["waypoint_collection"]] if obj.get("waypoint_collection") is not None else None,
            "travel": [Travel.from_dict(_item) for _item in obj["travel"]] if obj.get("travel") is not None else None,
            "achievement_count": obj.get("achievement_count"),
            "message_enabled": obj.get("message_enabled"),
            "email": obj.get("email"),
            "date_of_birth": obj.get("date_of_birth"),
            "is_active": obj.get("is_active"),
            "is_early_bird": obj.get("is_early_bird"),
            "is_live_banned": obj.get("is_live_banned"),
            "is_superuser": obj.get("is_superuser"),
            "skysight_email": obj.get("skysight_email"),
            "frontend_subscription": obj.get("frontend_subscription"),
            "xcsoar_token": obj.get("xcsoar_token"),
            "trial_available": obj.get("trial_available"),
            "flight_notification": obj.get("flight_notification"),
            "comment_notification": obj.get("comment_notification"),
            "follower_notification": obj.get("follower_notification"),
            "magazine_notification": obj.get("magazine_notification"),
            "live_competition_create": obj.get("live_competition_create"),
            "ssa_id": obj.get("ssa_id"),
            "copilot_status": obj.get("copilot_status"),
            "unit": obj.get("unit"),
            "language": obj.get("language"),
            "custom_filter": obj.get("custom_filter"),
            "user_group": [UserGroupSimple.from_dict(_item) for _item in obj["user_group"]] if obj.get("user_group") is not None else None,
            "newsletter_language": obj.get("newsletter_language"),
            "magazine_language": obj.get("magazine_language")
        })
        return _obj


