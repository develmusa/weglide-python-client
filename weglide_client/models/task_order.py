# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TaskOrder(str, Enum):
    """
    TaskOrder
    """

    """
    allowed enum values
    """
    DISTANCE = 'distance'
    NAME = 'name'
    USER_ID = 'user_id'
    PROXIMITY = 'proximity'
    STARS = 'stars'
    KIND = 'kind'
    MODIFIED = 'modified'
    MINUS_DISTANCE = '-distance'
    MINUS_NAME = '-name'
    MINUS_USER_ID = '-user_id'
    MINUS_PROXIMITY = '-proximity'
    MINUS_STARS = '-stars'
    MINUS_KIND = '-kind'
    MINUS_MODIFIED = '-modified'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TaskOrder from a JSON string"""
        return cls(json.loads(json_str))


