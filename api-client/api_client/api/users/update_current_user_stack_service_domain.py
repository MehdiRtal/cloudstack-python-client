from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_read_public import DomainReadPublic
from ...models.domain_update_public import DomainUpdatePublic
from ...models.http_validation_error import HTTPValidationError
from ...models.self_managed_service_type import SelfManagedServiceType
from ...types import Response


def _get_kwargs(
    stack_id: UUID,
    service_type: SelfManagedServiceType,
    service_id: UUID,
    domain_id: UUID,
    *,
    body: DomainUpdatePublic,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/users/me/stacks/{stack_id}/services/{service_type}/{service_id}/domains/{domain_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DomainReadPublic, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = DomainReadPublic.from_dict(response.json())

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
) -> Response[Union[Any, DomainReadPublic, HTTPValidationError]]:
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
    domain_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DomainUpdatePublic,
) -> Response[Union[Any, DomainReadPublic, HTTPValidationError]]:
    """Update Current User Stack Service Domain

    Args:
        stack_id (UUID):
        service_type (SelfManagedServiceType):
        service_id (UUID):
        domain_id (UUID):
        body (DomainUpdatePublic):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainReadPublic, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        stack_id=stack_id,
        service_type=service_type,
        service_id=service_id,
        domain_id=domain_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stack_id: UUID,
    service_type: SelfManagedServiceType,
    service_id: UUID,
    domain_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DomainUpdatePublic,
) -> Optional[Union[Any, DomainReadPublic, HTTPValidationError]]:
    """Update Current User Stack Service Domain

    Args:
        stack_id (UUID):
        service_type (SelfManagedServiceType):
        service_id (UUID):
        domain_id (UUID):
        body (DomainUpdatePublic):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DomainReadPublic, HTTPValidationError]
    """

    return sync_detailed(
        stack_id=stack_id,
        service_type=service_type,
        service_id=service_id,
        domain_id=domain_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    stack_id: UUID,
    service_type: SelfManagedServiceType,
    service_id: UUID,
    domain_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DomainUpdatePublic,
) -> Response[Union[Any, DomainReadPublic, HTTPValidationError]]:
    """Update Current User Stack Service Domain

    Args:
        stack_id (UUID):
        service_type (SelfManagedServiceType):
        service_id (UUID):
        domain_id (UUID):
        body (DomainUpdatePublic):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainReadPublic, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        stack_id=stack_id,
        service_type=service_type,
        service_id=service_id,
        domain_id=domain_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stack_id: UUID,
    service_type: SelfManagedServiceType,
    service_id: UUID,
    domain_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DomainUpdatePublic,
) -> Optional[Union[Any, DomainReadPublic, HTTPValidationError]]:
    """Update Current User Stack Service Domain

    Args:
        stack_id (UUID):
        service_type (SelfManagedServiceType):
        service_id (UUID):
        domain_id (UUID):
        body (DomainUpdatePublic):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DomainReadPublic, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            stack_id=stack_id,
            service_type=service_type,
            service_id=service_id,
            domain_id=domain_id,
            client=client,
            body=body,
        )
    ).parsed
