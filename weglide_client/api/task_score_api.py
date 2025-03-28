# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import date
from pydantic import Field, StrictFloat, StrictInt, StrictStr
from typing import Any, List, Optional, Union
from typing_extensions import Annotated
from weglide_client.models.score_kind import ScoreKind
from weglide_client.models.task import Task
from weglide_client.models.task_score_order import TaskScoreOrder

from weglide_client.api_client import ApiClient, RequestSerialized
from weglide_client.api_response import ApiResponse
from weglide_client.rest import RESTResponseType


class TaskScoreApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_recent_task_score_v1_task_score_recent_get(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """Get Recent Task Score


        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_recent_task_score_v1_task_score_recent_get_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_recent_task_score_v1_task_score_recent_get_with_http_info(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """Get Recent Task Score


        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_recent_task_score_v1_task_score_recent_get_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_recent_task_score_v1_task_score_recent_get_without_preload_content(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get Recent Task Score


        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_recent_task_score_v1_task_score_recent_get_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_recent_task_score_v1_task_score_recent_get_serialize(
        self,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/task/score/recent',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_task_score_list_v1_task_score_get(
        self,
        competition_id_in: Optional[StrictStr] = None,
        user_id_in: Optional[StrictStr] = None,
        airport_id_in: Optional[StrictStr] = None,
        season_in: Optional[StrictStr] = None,
        distance_gt: Optional[Union[StrictFloat, StrictInt]] = None,
        distance_lt: Optional[Union[StrictFloat, StrictInt]] = None,
        order_by: Optional[TaskScoreOrder] = None,
        scoring_date_start: Optional[date] = None,
        scoring_date_end: Optional[date] = None,
        scoring_date_in: Optional[StrictStr] = None,
        score_kind: Optional[ScoreKind] = None,
        skip: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True)]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[Task]:
        """Get Task Score List


        :param competition_id_in:
        :type competition_id_in: str
        :param user_id_in:
        :type user_id_in: str
        :param airport_id_in:
        :type airport_id_in: str
        :param season_in:
        :type season_in: str
        :param distance_gt:
        :type distance_gt: float
        :param distance_lt:
        :type distance_lt: float
        :param order_by:
        :type order_by: TaskScoreOrder
        :param scoring_date_start:
        :type scoring_date_start: date
        :param scoring_date_end:
        :type scoring_date_end: date
        :param scoring_date_in:
        :type scoring_date_in: str
        :param score_kind:
        :type score_kind: ScoreKind
        :param skip:
        :type skip: int
        :param limit:
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_task_score_list_v1_task_score_get_serialize(
            competition_id_in=competition_id_in,
            user_id_in=user_id_in,
            airport_id_in=airport_id_in,
            season_in=season_in,
            distance_gt=distance_gt,
            distance_lt=distance_lt,
            order_by=order_by,
            scoring_date_start=scoring_date_start,
            scoring_date_end=scoring_date_end,
            scoring_date_in=scoring_date_in,
            score_kind=score_kind,
            skip=skip,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Task]",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_task_score_list_v1_task_score_get_with_http_info(
        self,
        competition_id_in: Optional[StrictStr] = None,
        user_id_in: Optional[StrictStr] = None,
        airport_id_in: Optional[StrictStr] = None,
        season_in: Optional[StrictStr] = None,
        distance_gt: Optional[Union[StrictFloat, StrictInt]] = None,
        distance_lt: Optional[Union[StrictFloat, StrictInt]] = None,
        order_by: Optional[TaskScoreOrder] = None,
        scoring_date_start: Optional[date] = None,
        scoring_date_end: Optional[date] = None,
        scoring_date_in: Optional[StrictStr] = None,
        score_kind: Optional[ScoreKind] = None,
        skip: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True)]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[Task]]:
        """Get Task Score List


        :param competition_id_in:
        :type competition_id_in: str
        :param user_id_in:
        :type user_id_in: str
        :param airport_id_in:
        :type airport_id_in: str
        :param season_in:
        :type season_in: str
        :param distance_gt:
        :type distance_gt: float
        :param distance_lt:
        :type distance_lt: float
        :param order_by:
        :type order_by: TaskScoreOrder
        :param scoring_date_start:
        :type scoring_date_start: date
        :param scoring_date_end:
        :type scoring_date_end: date
        :param scoring_date_in:
        :type scoring_date_in: str
        :param score_kind:
        :type score_kind: ScoreKind
        :param skip:
        :type skip: int
        :param limit:
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_task_score_list_v1_task_score_get_serialize(
            competition_id_in=competition_id_in,
            user_id_in=user_id_in,
            airport_id_in=airport_id_in,
            season_in=season_in,
            distance_gt=distance_gt,
            distance_lt=distance_lt,
            order_by=order_by,
            scoring_date_start=scoring_date_start,
            scoring_date_end=scoring_date_end,
            scoring_date_in=scoring_date_in,
            score_kind=score_kind,
            skip=skip,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Task]",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_task_score_list_v1_task_score_get_without_preload_content(
        self,
        competition_id_in: Optional[StrictStr] = None,
        user_id_in: Optional[StrictStr] = None,
        airport_id_in: Optional[StrictStr] = None,
        season_in: Optional[StrictStr] = None,
        distance_gt: Optional[Union[StrictFloat, StrictInt]] = None,
        distance_lt: Optional[Union[StrictFloat, StrictInt]] = None,
        order_by: Optional[TaskScoreOrder] = None,
        scoring_date_start: Optional[date] = None,
        scoring_date_end: Optional[date] = None,
        scoring_date_in: Optional[StrictStr] = None,
        score_kind: Optional[ScoreKind] = None,
        skip: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True)]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get Task Score List


        :param competition_id_in:
        :type competition_id_in: str
        :param user_id_in:
        :type user_id_in: str
        :param airport_id_in:
        :type airport_id_in: str
        :param season_in:
        :type season_in: str
        :param distance_gt:
        :type distance_gt: float
        :param distance_lt:
        :type distance_lt: float
        :param order_by:
        :type order_by: TaskScoreOrder
        :param scoring_date_start:
        :type scoring_date_start: date
        :param scoring_date_end:
        :type scoring_date_end: date
        :param scoring_date_in:
        :type scoring_date_in: str
        :param score_kind:
        :type score_kind: ScoreKind
        :param skip:
        :type skip: int
        :param limit:
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_task_score_list_v1_task_score_get_serialize(
            competition_id_in=competition_id_in,
            user_id_in=user_id_in,
            airport_id_in=airport_id_in,
            season_in=season_in,
            distance_gt=distance_gt,
            distance_lt=distance_lt,
            order_by=order_by,
            scoring_date_start=scoring_date_start,
            scoring_date_end=scoring_date_end,
            scoring_date_in=scoring_date_in,
            score_kind=score_kind,
            skip=skip,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Task]",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_task_score_list_v1_task_score_get_serialize(
        self,
        competition_id_in,
        user_id_in,
        airport_id_in,
        season_in,
        distance_gt,
        distance_lt,
        order_by,
        scoring_date_start,
        scoring_date_end,
        scoring_date_in,
        score_kind,
        skip,
        limit,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if competition_id_in is not None:
            
            _query_params.append(('competition_id_in', competition_id_in))
            
        if user_id_in is not None:
            
            _query_params.append(('user_id_in', user_id_in))
            
        if airport_id_in is not None:
            
            _query_params.append(('airport_id_in', airport_id_in))
            
        if season_in is not None:
            
            _query_params.append(('season_in', season_in))
            
        if distance_gt is not None:
            
            _query_params.append(('distance_gt', distance_gt))
            
        if distance_lt is not None:
            
            _query_params.append(('distance_lt', distance_lt))
            
        if order_by is not None:
            
            _query_params.append(('order_by', order_by.value))
            
        if scoring_date_start is not None:
            if isinstance(scoring_date_start, date):
                _query_params.append(
                    (
                        'scoring_date_start',
                        scoring_date_start.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('scoring_date_start', scoring_date_start))
            
        if scoring_date_end is not None:
            if isinstance(scoring_date_end, date):
                _query_params.append(
                    (
                        'scoring_date_end',
                        scoring_date_end.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('scoring_date_end', scoring_date_end))
            
        if scoring_date_in is not None:
            
            _query_params.append(('scoring_date_in', scoring_date_in))
            
        if score_kind is not None:
            
            _query_params.append(('score_kind', score_kind.value))
            
        if skip is not None:
            
            _query_params.append(('skip', skip))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/task/score',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


