from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    stack_id: UUID,
    volume_id: UUID,
    backup_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/users/me/stacks/{stack_id}/volumes/{volume_id}/backups/{backup_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    stack_id: UUID,
    volume_id: UUID,
    backup_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError]]:
    """Delete Current User Stack Volume Backup

    Args:
        stack_id (UUID):
        volume_id (UUID):
        backup_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        stack_id=stack_id,
        volume_id=volume_id,
        backup_id=backup_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stack_id: UUID,
    volume_id: UUID,
    backup_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Delete Current User Stack Volume Backup

    Args:
        stack_id (UUID):
        volume_id (UUID):
        backup_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        stack_id=stack_id,
        volume_id=volume_id,
        backup_id=backup_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    stack_id: UUID,
    volume_id: UUID,
    backup_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError]]:
    """Delete Current User Stack Volume Backup

    Args:
        stack_id (UUID):
        volume_id (UUID):
        backup_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        stack_id=stack_id,
        volume_id=volume_id,
        backup_id=backup_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stack_id: UUID,
    volume_id: UUID,
    backup_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Delete Current User Stack Volume Backup

    Args:
        stack_id (UUID):
        volume_id (UUID):
        backup_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            stack_id=stack_id,
            volume_id=volume_id,
            backup_id=backup_id,
            client=client,
        )
    ).parsed
