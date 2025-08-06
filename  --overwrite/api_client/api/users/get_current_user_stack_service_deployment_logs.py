import datetime
from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_current_user_stack_service_deployment_logs_response_200_item import (
    GetCurrentUserStackServiceDeploymentLogsResponse200Item,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.logs_type import LogsType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    stack_id: UUID,
    service_id: UUID,
    deployment_id: UUID,
    logs_type: LogsType,
    *,
    limit: Union[None, Unset, int] = UNSET,
    start: Union[None, Unset, datetime.datetime] = UNSET,
    end: Union[None, Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_limit: Union[None, Unset, int]
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_start: Union[None, Unset, str]
    if isinstance(start, Unset):
        json_start = UNSET
    elif isinstance(start, datetime.datetime):
        json_start = start.isoformat()
    else:
        json_start = start
    params["start"] = json_start

    json_end: Union[None, Unset, str]
    if isinstance(end, Unset):
        json_end = UNSET
    elif isinstance(end, datetime.datetime):
        json_end = end.isoformat()
    else:
        json_end = end
    params["end"] = json_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/users/me/stacks/{stack_id}/services/{service_id}/deployments/{deployment_id}/logs/{logs_type}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, list["GetCurrentUserStackServiceDeploymentLogsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetCurrentUserStackServiceDeploymentLogsResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, list["GetCurrentUserStackServiceDeploymentLogsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    stack_id: UUID,
    service_id: UUID,
    deployment_id: UUID,
    logs_type: LogsType,
    *,
    client: AuthenticatedClient,
    limit: Union[None, Unset, int] = UNSET,
    start: Union[None, Unset, datetime.datetime] = UNSET,
    end: Union[None, Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, HTTPValidationError, list["GetCurrentUserStackServiceDeploymentLogsResponse200Item"]]]:
    """Get Current User Stack Service Deployment Logs

    Args:
        stack_id (UUID):
        service_id (UUID):
        deployment_id (UUID):
        logs_type (LogsType):
        limit (Union[None, Unset, int]):
        start (Union[None, Unset, datetime.datetime]):
        end (Union[None, Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, list['GetCurrentUserStackServiceDeploymentLogsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        stack_id=stack_id,
        service_id=service_id,
        deployment_id=deployment_id,
        logs_type=logs_type,
        limit=limit,
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stack_id: UUID,
    service_id: UUID,
    deployment_id: UUID,
    logs_type: LogsType,
    *,
    client: AuthenticatedClient,
    limit: Union[None, Unset, int] = UNSET,
    start: Union[None, Unset, datetime.datetime] = UNSET,
    end: Union[None, Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, list["GetCurrentUserStackServiceDeploymentLogsResponse200Item"]]]:
    """Get Current User Stack Service Deployment Logs

    Args:
        stack_id (UUID):
        service_id (UUID):
        deployment_id (UUID):
        logs_type (LogsType):
        limit (Union[None, Unset, int]):
        start (Union[None, Unset, datetime.datetime]):
        end (Union[None, Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, list['GetCurrentUserStackServiceDeploymentLogsResponse200Item']]
    """

    return sync_detailed(
        stack_id=stack_id,
        service_id=service_id,
        deployment_id=deployment_id,
        logs_type=logs_type,
        client=client,
        limit=limit,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    stack_id: UUID,
    service_id: UUID,
    deployment_id: UUID,
    logs_type: LogsType,
    *,
    client: AuthenticatedClient,
    limit: Union[None, Unset, int] = UNSET,
    start: Union[None, Unset, datetime.datetime] = UNSET,
    end: Union[None, Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, HTTPValidationError, list["GetCurrentUserStackServiceDeploymentLogsResponse200Item"]]]:
    """Get Current User Stack Service Deployment Logs

    Args:
        stack_id (UUID):
        service_id (UUID):
        deployment_id (UUID):
        logs_type (LogsType):
        limit (Union[None, Unset, int]):
        start (Union[None, Unset, datetime.datetime]):
        end (Union[None, Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, list['GetCurrentUserStackServiceDeploymentLogsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        stack_id=stack_id,
        service_id=service_id,
        deployment_id=deployment_id,
        logs_type=logs_type,
        limit=limit,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stack_id: UUID,
    service_id: UUID,
    deployment_id: UUID,
    logs_type: LogsType,
    *,
    client: AuthenticatedClient,
    limit: Union[None, Unset, int] = UNSET,
    start: Union[None, Unset, datetime.datetime] = UNSET,
    end: Union[None, Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, list["GetCurrentUserStackServiceDeploymentLogsResponse200Item"]]]:
    """Get Current User Stack Service Deployment Logs

    Args:
        stack_id (UUID):
        service_id (UUID):
        deployment_id (UUID):
        logs_type (LogsType):
        limit (Union[None, Unset, int]):
        start (Union[None, Unset, datetime.datetime]):
        end (Union[None, Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, list['GetCurrentUserStackServiceDeploymentLogsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            stack_id=stack_id,
            service_id=service_id,
            deployment_id=deployment_id,
            logs_type=logs_type,
            client=client,
            limit=limit,
            start=start,
            end=end,
        )
    ).parsed
