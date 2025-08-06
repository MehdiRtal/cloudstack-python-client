from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.self_managed_service_type import SelfManagedServiceType
from ...types import Response


def _get_kwargs(
    stack_id: UUID,
    service_type: SelfManagedServiceType,
    service_id: UUID,
    private_registry_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/users/me/stacks/{stack_id}/services/{service_type}/{service_id}/private_registries/{private_registry_id}",
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
    service_type: SelfManagedServiceType,
    service_id: UUID,
    private_registry_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError]]:
    """Delete Current User Stack Service Private Registry

    Args:
        stack_id (UUID):
        service_type (SelfManagedServiceType):
        service_id (UUID):
        private_registry_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        stack_id=stack_id,
        service_type=service_type,
        service_id=service_id,
        private_registry_id=private_registry_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stack_id: UUID,
    service_type: SelfManagedServiceType,
    service_id: UUID,
    private_registry_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Delete Current User Stack Service Private Registry

    Args:
        stack_id (UUID):
        service_type (SelfManagedServiceType):
        service_id (UUID):
        private_registry_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        stack_id=stack_id,
        service_type=service_type,
        service_id=service_id,
        private_registry_id=private_registry_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    stack_id: UUID,
    service_type: SelfManagedServiceType,
    service_id: UUID,
    private_registry_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError]]:
    """Delete Current User Stack Service Private Registry

    Args:
        stack_id (UUID):
        service_type (SelfManagedServiceType):
        service_id (UUID):
        private_registry_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        stack_id=stack_id,
        service_type=service_type,
        service_id=service_id,
        private_registry_id=private_registry_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stack_id: UUID,
    service_type: SelfManagedServiceType,
    service_id: UUID,
    private_registry_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Delete Current User Stack Service Private Registry

    Args:
        stack_id (UUID):
        service_type (SelfManagedServiceType):
        service_id (UUID):
        private_registry_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            stack_id=stack_id,
            service_type=service_type,
            service_id=service_id,
            private_registry_id=private_registry_id,
            client=client,
        )
    ).parsed
