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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from weglide_client.models.filter import Filter
from weglide_client.models.gender import Gender
from weglide_client.models.unit import Unit
from typing import Optional, Set
from typing_extensions import Self

class UserUpdate(BaseModel):
    """
    UserUpdate
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=6, strict=True, max_length=60)]] = None
    skysight_email: Optional[StrictStr] = None
    skysight_password: Optional[StrictStr] = None
    newsletter_language: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=2)]] = None
    magazine_language: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=2)]] = None
    bio: Optional[Annotated[str, Field(strict=True, max_length=160)]] = None
    ssa_id: Optional[StrictInt] = None
    password: Optional[Annotated[str, Field(min_length=6, strict=True, max_length=60)]] = None
    old_password: Optional[Annotated[str, Field(min_length=6, strict=True, max_length=60)]] = None
    date_of_birth: Optional[date] = None
    gender: Optional[Gender] = None
    club_id: Optional[StrictInt] = None
    second_club_id: Optional[StrictInt] = None
    unit: Optional[Unit] = None
    language: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=2)]] = None
    open_in_seeyou: Optional[StrictBool] = None
    comments_allowed: Optional[StrictBool] = None
    filter: Optional[Annotated[List[Filter], Field(max_length=5)]] = None
    flight_notification: Optional[StrictBool] = None
    comment_notification: Optional[StrictBool] = None
    follower_notification: Optional[StrictBool] = None
    magazine_notification: Optional[StrictBool] = None
    message_enabled: Optional[StrictBool] = None
    copilot_password: Optional[StrictStr] = None
    copilot_email: Optional[StrictStr] = None
    badge: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["name", "skysight_email", "skysight_password", "newsletter_language", "magazine_language", "bio", "ssa_id", "password", "old_password", "date_of_birth", "gender", "club_id", "second_club_id", "unit", "language", "open_in_seeyou", "comments_allowed", "filter", "flight_notification", "comment_notification", "follower_notification", "magazine_notification", "message_enabled", "copilot_password", "copilot_email", "badge"]

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
        """Create an instance of UserUpdate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in filter (list)
        _items = []
        if self.filter:
            for _item_filter in self.filter:
                if _item_filter:
                    _items.append(_item_filter.to_dict())
            _dict['filter'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if skysight_email (nullable) is None
        # and model_fields_set contains the field
        if self.skysight_email is None and "skysight_email" in self.model_fields_set:
            _dict['skysight_email'] = None

        # set to None if skysight_password (nullable) is None
        # and model_fields_set contains the field
        if self.skysight_password is None and "skysight_password" in self.model_fields_set:
            _dict['skysight_password'] = None

        # set to None if newsletter_language (nullable) is None
        # and model_fields_set contains the field
        if self.newsletter_language is None and "newsletter_language" in self.model_fields_set:
            _dict['newsletter_language'] = None

        # set to None if magazine_language (nullable) is None
        # and model_fields_set contains the field
        if self.magazine_language is None and "magazine_language" in self.model_fields_set:
            _dict['magazine_language'] = None

        # set to None if bio (nullable) is None
        # and model_fields_set contains the field
        if self.bio is None and "bio" in self.model_fields_set:
            _dict['bio'] = None

        # set to None if ssa_id (nullable) is None
        # and model_fields_set contains the field
        if self.ssa_id is None and "ssa_id" in self.model_fields_set:
            _dict['ssa_id'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if old_password (nullable) is None
        # and model_fields_set contains the field
        if self.old_password is None and "old_password" in self.model_fields_set:
            _dict['old_password'] = None

        # set to None if date_of_birth (nullable) is None
        # and model_fields_set contains the field
        if self.date_of_birth is None and "date_of_birth" in self.model_fields_set:
            _dict['date_of_birth'] = None

        # set to None if gender (nullable) is None
        # and model_fields_set contains the field
        if self.gender is None and "gender" in self.model_fields_set:
            _dict['gender'] = None

        # set to None if club_id (nullable) is None
        # and model_fields_set contains the field
        if self.club_id is None and "club_id" in self.model_fields_set:
            _dict['club_id'] = None

        # set to None if second_club_id (nullable) is None
        # and model_fields_set contains the field
        if self.second_club_id is None and "second_club_id" in self.model_fields_set:
            _dict['second_club_id'] = None

        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if open_in_seeyou (nullable) is None
        # and model_fields_set contains the field
        if self.open_in_seeyou is None and "open_in_seeyou" in self.model_fields_set:
            _dict['open_in_seeyou'] = None

        # set to None if comments_allowed (nullable) is None
        # and model_fields_set contains the field
        if self.comments_allowed is None and "comments_allowed" in self.model_fields_set:
            _dict['comments_allowed'] = None

        # set to None if filter (nullable) is None
        # and model_fields_set contains the field
        if self.filter is None and "filter" in self.model_fields_set:
            _dict['filter'] = None

        # set to None if flight_notification (nullable) is None
        # and model_fields_set contains the field
        if self.flight_notification is None and "flight_notification" in self.model_fields_set:
            _dict['flight_notification'] = None

        # set to None if comment_notification (nullable) is None
        # and model_fields_set contains the field
        if self.comment_notification is None and "comment_notification" in self.model_fields_set:
            _dict['comment_notification'] = None

        # set to None if follower_notification (nullable) is None
        # and model_fields_set contains the field
        if self.follower_notification is None and "follower_notification" in self.model_fields_set:
            _dict['follower_notification'] = None

        # set to None if magazine_notification (nullable) is None
        # and model_fields_set contains the field
        if self.magazine_notification is None and "magazine_notification" in self.model_fields_set:
            _dict['magazine_notification'] = None

        # set to None if message_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.message_enabled is None and "message_enabled" in self.model_fields_set:
            _dict['message_enabled'] = None

        # set to None if copilot_password (nullable) is None
        # and model_fields_set contains the field
        if self.copilot_password is None and "copilot_password" in self.model_fields_set:
            _dict['copilot_password'] = None

        # set to None if copilot_email (nullable) is None
        # and model_fields_set contains the field
        if self.copilot_email is None and "copilot_email" in self.model_fields_set:
            _dict['copilot_email'] = None

        # set to None if badge (nullable) is None
        # and model_fields_set contains the field
        if self.badge is None and "badge" in self.model_fields_set:
            _dict['badge'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "skysight_email": obj.get("skysight_email"),
            "skysight_password": obj.get("skysight_password"),
            "newsletter_language": obj.get("newsletter_language"),
            "magazine_language": obj.get("magazine_language"),
            "bio": obj.get("bio"),
            "ssa_id": obj.get("ssa_id"),
            "password": obj.get("password"),
            "old_password": obj.get("old_password"),
            "date_of_birth": obj.get("date_of_birth"),
            "gender": obj.get("gender"),
            "club_id": obj.get("club_id"),
            "second_club_id": obj.get("second_club_id"),
            "unit": obj.get("unit"),
            "language": obj.get("language"),
            "open_in_seeyou": obj.get("open_in_seeyou"),
            "comments_allowed": obj.get("comments_allowed"),
            "filter": [Filter.from_dict(_item) for _item in obj["filter"]] if obj.get("filter") is not None else None,
            "flight_notification": obj.get("flight_notification"),
            "comment_notification": obj.get("comment_notification"),
            "follower_notification": obj.get("follower_notification"),
            "magazine_notification": obj.get("magazine_notification"),
            "message_enabled": obj.get("message_enabled"),
            "copilot_password": obj.get("copilot_password"),
            "copilot_email": obj.get("copilot_email"),
            "badge": obj.get("badge")
        })
        return _obj


