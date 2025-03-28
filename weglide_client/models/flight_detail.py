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
from weglide_client.models.achievement_with_badge_no_user import AchievementWithBadgeNoUser
from weglide_client.models.aircraft_flight import AircraftFlight
from weglide_client.models.airport_flight import AirportFlight
from weglide_client.models.airspace_violation import AirspaceViolation
from weglide_client.models.app_schemas_task_task_flight import AppSchemasTaskTaskFlight
from weglide_client.models.club_flight import ClubFlight
from weglide_client.models.igc_file_flight import IGCFileFlight
from weglide_client.models.rule_set import RuleSet
from weglide_client.models.segment_score_flight import SegmentScoreFlight
from weglide_client.models.task_score_flight import TaskScoreFlight
from weglide_client.models.user_flight_detail import UserFlightDetail
from weglide_client.models.user_with_image import UserWithImage
from typing import Optional, Set
from typing_extensions import Self

class FlightDetail(BaseModel):
    """
    FlightDetail
    """ # noqa: E501
    id: StrictInt
    user: UserFlightDetail
    co_user: Optional[UserWithImage] = None
    co_user_name: Optional[StrictStr] = None
    custom_takeoff_airport: Dict[str, Any]
    aircraft: Optional[AircraftFlight] = None
    club: Optional[ClubFlight] = None
    media_info: Optional[StrictStr] = None
    takeoff_time: datetime
    landing_time: datetime
    scoring_date: date
    bbox: List[Union[StrictFloat, StrictInt]]
    junior: StrictBool
    dmst_index: Optional[StrictInt] = None
    igc_file: IGCFileFlight
    landing_airport: Optional[AirportFlight] = None
    airspace_violation: List[AirspaceViolation]
    sorted_contest: List[Dict[str, Any]]
    segment_score: List[SegmentScoreFlight]
    task_score: List[TaskScoreFlight]
    meeting: List[Dict[str, Any]]
    achievement: List[AchievementWithBadgeNoUser]
    task: Optional[AppSchemasTaskTaskFlight] = None
    task_ruleset: Optional[RuleSet] = None
    edit_allowed_until: datetime
    valid: StrictBool
    sc_class: StrictStr
    comment: Optional[StrictStr] = None
    audio_url: Optional[StrictStr] = None
    score_club_class: StrictBool
    analysed: StrictBool
    active_errors: Optional[List[Any]] = None
    notes: Optional[StrictStr] = None
    registration: Optional[StrictStr] = None
    competition_id: Optional[StrictStr] = None
    total_seconds: StrictInt
    scoring_times: Optional[List[datetime]] = None
    engine_scoring_times: Optional[List[datetime]] = None
    fes_scoring_times: Optional[List[datetime]] = None
    fes_energy_total: Optional[Union[StrictFloat, StrictInt]] = None
    fes_battery_takeoff: Optional[Union[StrictFloat, StrictInt]] = None
    fes_battery_landing: Optional[Union[StrictFloat, StrictInt]] = None
    fes_max_power: Optional[Union[StrictFloat, StrictInt]] = None
    mass: Optional[StrictInt] = None
    launch_kind: Optional[StrictStr] = None
    launch_gain: Optional[StrictInt] = None
    launch_time: Optional[StrictInt] = None
    launch_vario: Optional[Union[StrictFloat, StrictInt]] = None
    takeoff_distance: Optional[StrictInt] = None
    ground_roll_distance: Optional[StrictInt] = None
    task_achieved: StrictBool
    takeoff_point: Dict[str, Any]
    task_result: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "user", "co_user", "co_user_name", "custom_takeoff_airport", "aircraft", "club", "media_info", "takeoff_time", "landing_time", "scoring_date", "bbox", "junior", "dmst_index", "igc_file", "landing_airport", "airspace_violation", "sorted_contest", "segment_score", "task_score", "meeting", "achievement", "task", "task_ruleset", "edit_allowed_until", "valid", "sc_class", "comment", "audio_url", "score_club_class", "analysed", "active_errors", "notes", "registration", "competition_id", "total_seconds", "scoring_times", "engine_scoring_times", "fes_scoring_times", "fes_energy_total", "fes_battery_takeoff", "fes_battery_landing", "fes_max_power", "mass", "launch_kind", "launch_gain", "launch_time", "launch_vario", "takeoff_distance", "ground_roll_distance", "task_achieved", "takeoff_point", "task_result"]

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
        """Create an instance of FlightDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of igc_file
        if self.igc_file:
            _dict['igc_file'] = self.igc_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of landing_airport
        if self.landing_airport:
            _dict['landing_airport'] = self.landing_airport.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in airspace_violation (list)
        _items = []
        if self.airspace_violation:
            for _item_airspace_violation in self.airspace_violation:
                if _item_airspace_violation:
                    _items.append(_item_airspace_violation.to_dict())
            _dict['airspace_violation'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in segment_score (list)
        _items = []
        if self.segment_score:
            for _item_segment_score in self.segment_score:
                if _item_segment_score:
                    _items.append(_item_segment_score.to_dict())
            _dict['segment_score'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in task_score (list)
        _items = []
        if self.task_score:
            for _item_task_score in self.task_score:
                if _item_task_score:
                    _items.append(_item_task_score.to_dict())
            _dict['task_score'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in achievement (list)
        _items = []
        if self.achievement:
            for _item_achievement in self.achievement:
                if _item_achievement:
                    _items.append(_item_achievement.to_dict())
            _dict['achievement'] = _items
        # override the default output from pydantic by calling `to_dict()` of task
        if self.task:
            _dict['task'] = self.task.to_dict()
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

        # set to None if landing_airport (nullable) is None
        # and model_fields_set contains the field
        if self.landing_airport is None and "landing_airport" in self.model_fields_set:
            _dict['landing_airport'] = None

        # set to None if task (nullable) is None
        # and model_fields_set contains the field
        if self.task is None and "task" in self.model_fields_set:
            _dict['task'] = None

        # set to None if task_ruleset (nullable) is None
        # and model_fields_set contains the field
        if self.task_ruleset is None and "task_ruleset" in self.model_fields_set:
            _dict['task_ruleset'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if audio_url (nullable) is None
        # and model_fields_set contains the field
        if self.audio_url is None and "audio_url" in self.model_fields_set:
            _dict['audio_url'] = None

        # set to None if active_errors (nullable) is None
        # and model_fields_set contains the field
        if self.active_errors is None and "active_errors" in self.model_fields_set:
            _dict['active_errors'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if registration (nullable) is None
        # and model_fields_set contains the field
        if self.registration is None and "registration" in self.model_fields_set:
            _dict['registration'] = None

        # set to None if competition_id (nullable) is None
        # and model_fields_set contains the field
        if self.competition_id is None and "competition_id" in self.model_fields_set:
            _dict['competition_id'] = None

        # set to None if scoring_times (nullable) is None
        # and model_fields_set contains the field
        if self.scoring_times is None and "scoring_times" in self.model_fields_set:
            _dict['scoring_times'] = None

        # set to None if engine_scoring_times (nullable) is None
        # and model_fields_set contains the field
        if self.engine_scoring_times is None and "engine_scoring_times" in self.model_fields_set:
            _dict['engine_scoring_times'] = None

        # set to None if fes_scoring_times (nullable) is None
        # and model_fields_set contains the field
        if self.fes_scoring_times is None and "fes_scoring_times" in self.model_fields_set:
            _dict['fes_scoring_times'] = None

        # set to None if fes_energy_total (nullable) is None
        # and model_fields_set contains the field
        if self.fes_energy_total is None and "fes_energy_total" in self.model_fields_set:
            _dict['fes_energy_total'] = None

        # set to None if fes_battery_takeoff (nullable) is None
        # and model_fields_set contains the field
        if self.fes_battery_takeoff is None and "fes_battery_takeoff" in self.model_fields_set:
            _dict['fes_battery_takeoff'] = None

        # set to None if fes_battery_landing (nullable) is None
        # and model_fields_set contains the field
        if self.fes_battery_landing is None and "fes_battery_landing" in self.model_fields_set:
            _dict['fes_battery_landing'] = None

        # set to None if fes_max_power (nullable) is None
        # and model_fields_set contains the field
        if self.fes_max_power is None and "fes_max_power" in self.model_fields_set:
            _dict['fes_max_power'] = None

        # set to None if mass (nullable) is None
        # and model_fields_set contains the field
        if self.mass is None and "mass" in self.model_fields_set:
            _dict['mass'] = None

        # set to None if launch_kind (nullable) is None
        # and model_fields_set contains the field
        if self.launch_kind is None and "launch_kind" in self.model_fields_set:
            _dict['launch_kind'] = None

        # set to None if launch_gain (nullable) is None
        # and model_fields_set contains the field
        if self.launch_gain is None and "launch_gain" in self.model_fields_set:
            _dict['launch_gain'] = None

        # set to None if launch_time (nullable) is None
        # and model_fields_set contains the field
        if self.launch_time is None and "launch_time" in self.model_fields_set:
            _dict['launch_time'] = None

        # set to None if launch_vario (nullable) is None
        # and model_fields_set contains the field
        if self.launch_vario is None and "launch_vario" in self.model_fields_set:
            _dict['launch_vario'] = None

        # set to None if takeoff_distance (nullable) is None
        # and model_fields_set contains the field
        if self.takeoff_distance is None and "takeoff_distance" in self.model_fields_set:
            _dict['takeoff_distance'] = None

        # set to None if ground_roll_distance (nullable) is None
        # and model_fields_set contains the field
        if self.ground_roll_distance is None and "ground_roll_distance" in self.model_fields_set:
            _dict['ground_roll_distance'] = None

        # set to None if task_result (nullable) is None
        # and model_fields_set contains the field
        if self.task_result is None and "task_result" in self.model_fields_set:
            _dict['task_result'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlightDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "user": UserFlightDetail.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "co_user": UserWithImage.from_dict(obj["co_user"]) if obj.get("co_user") is not None else None,
            "co_user_name": obj.get("co_user_name"),
            "custom_takeoff_airport": obj.get("custom_takeoff_airport"),
            "aircraft": AircraftFlight.from_dict(obj["aircraft"]) if obj.get("aircraft") is not None else None,
            "club": ClubFlight.from_dict(obj["club"]) if obj.get("club") is not None else None,
            "media_info": obj.get("media_info"),
            "takeoff_time": obj.get("takeoff_time"),
            "landing_time": obj.get("landing_time"),
            "scoring_date": obj.get("scoring_date"),
            "bbox": obj.get("bbox"),
            "junior": obj.get("junior"),
            "dmst_index": obj.get("dmst_index"),
            "igc_file": IGCFileFlight.from_dict(obj["igc_file"]) if obj.get("igc_file") is not None else None,
            "landing_airport": AirportFlight.from_dict(obj["landing_airport"]) if obj.get("landing_airport") is not None else None,
            "airspace_violation": [AirspaceViolation.from_dict(_item) for _item in obj["airspace_violation"]] if obj.get("airspace_violation") is not None else None,
            "sorted_contest": obj.get("sorted_contest"),
            "segment_score": [SegmentScoreFlight.from_dict(_item) for _item in obj["segment_score"]] if obj.get("segment_score") is not None else None,
            "task_score": [TaskScoreFlight.from_dict(_item) for _item in obj["task_score"]] if obj.get("task_score") is not None else None,
            "meeting": obj.get("meeting"),
            "achievement": [AchievementWithBadgeNoUser.from_dict(_item) for _item in obj["achievement"]] if obj.get("achievement") is not None else None,
            "task": AppSchemasTaskTaskFlight.from_dict(obj["task"]) if obj.get("task") is not None else None,
            "task_ruleset": obj.get("task_ruleset"),
            "edit_allowed_until": obj.get("edit_allowed_until"),
            "valid": obj.get("valid"),
            "sc_class": obj.get("sc_class"),
            "comment": obj.get("comment"),
            "audio_url": obj.get("audio_url"),
            "score_club_class": obj.get("score_club_class"),
            "analysed": obj.get("analysed"),
            "active_errors": obj.get("active_errors"),
            "notes": obj.get("notes"),
            "registration": obj.get("registration"),
            "competition_id": obj.get("competition_id"),
            "total_seconds": obj.get("total_seconds"),
            "scoring_times": obj.get("scoring_times"),
            "engine_scoring_times": obj.get("engine_scoring_times"),
            "fes_scoring_times": obj.get("fes_scoring_times"),
            "fes_energy_total": obj.get("fes_energy_total"),
            "fes_battery_takeoff": obj.get("fes_battery_takeoff"),
            "fes_battery_landing": obj.get("fes_battery_landing"),
            "fes_max_power": obj.get("fes_max_power"),
            "mass": obj.get("mass"),
            "launch_kind": obj.get("launch_kind"),
            "launch_gain": obj.get("launch_gain"),
            "launch_time": obj.get("launch_time"),
            "launch_vario": obj.get("launch_vario"),
            "takeoff_distance": obj.get("takeoff_distance"),
            "ground_roll_distance": obj.get("ground_roll_distance"),
            "task_achieved": obj.get("task_achieved"),
            "takeoff_point": obj.get("takeoff_point"),
            "task_result": obj.get("task_result")
        })
        return _obj


