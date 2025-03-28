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


class Gender(str, Enum):
    """
    Gender
    """

    """
    allowed enum values
    """
    M = 'M'
    F = 'F'
    D = 'D'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Gender from a JSON string"""
        return cls(json.loads(json_str))


