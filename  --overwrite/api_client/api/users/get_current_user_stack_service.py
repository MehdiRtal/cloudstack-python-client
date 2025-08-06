from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.function_service_read_public import FunctionServiceReadPublic
from ...models.github_service_read_public import GithubServiceReadPublic
from ...models.http_validation_error import HTTPValidationError
from ...models.image_service_read_public import ImageServiceReadPublic
from ...models.postgres_service_read_public import PostgresServiceReadPublic
from ...types import Response


def _get_kwargs(
    stack_id: UUID,
    service_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/users/me/stacks/{stack_id}/services/{service_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        HTTPValidationError,
        Union[
            "FunctionServiceReadPublic",
            "GithubServiceReadPublic",
            "ImageServiceReadPublic",
            "PostgresServiceReadPublic",
        ],
    ]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "FunctionServiceReadPublic",
            "GithubServiceReadPublic",
            "ImageServiceReadPublic",
            "PostgresServiceReadPublic",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_service_read_public_type_0 = ImageServiceReadPublic.from_dict(data)

                return componentsschemas_service_read_public_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_service_read_public_type_1 = GithubServiceReadPublic.from_dict(data)

                return componentsschemas_service_read_public_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_service_read_public_type_2 = FunctionServiceReadPublic.from_dict(data)

                return componentsschemas_service_read_public_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_service_read_public_type_3 = PostgresServiceReadPublic.from_dict(data)

            return componentsschemas_service_read_public_type_3

        response_200 = _parse_response_200(response.json())

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
) -> Response[
    Union[
        Any,
        HTTPValidationError,
        Union[
            "FunctionServiceReadPublic",
            "GithubServiceReadPublic",
            "ImageServiceReadPublic",
            "PostgresServiceReadPublic",
        ],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    stack_id: UUID,
    service_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        Any,
        HTTPValidationError,
        Union[
            "FunctionServiceReadPublic",
            "GithubServiceReadPublic",
            "ImageServiceReadPublic",
            "PostgresServiceReadPublic",
        ],
    ]
]:
    """Get Current User Stack Service

    Args:
        stack_id (UUID):
        service_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, Union['FunctionServiceReadPublic', 'GithubServiceReadPublic', 'ImageServiceReadPublic', 'PostgresServiceReadPublic']]]
    """

    kwargs = _get_kwargs(
        stack_id=stack_id,
        service_id=service_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stack_id: UUID,
    service_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        Any,
        HTTPValidationError,
        Union[
            "FunctionServiceReadPublic",
            "GithubServiceReadPublic",
            "ImageServiceReadPublic",
            "PostgresServiceReadPublic",
        ],
    ]
]:
    """Get Current User Stack Service

    Args:
        stack_id (UUID):
        service_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, Union['FunctionServiceReadPublic', 'GithubServiceReadPublic', 'ImageServiceReadPublic', 'PostgresServiceReadPublic']]
    """

    return sync_detailed(
        stack_id=stack_id,
        service_id=service_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    stack_id: UUID,
    service_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        Any,
        HTTPValidationError,
        Union[
            "FunctionServiceReadPublic",
            "GithubServiceReadPublic",
            "ImageServiceReadPublic",
            "PostgresServiceReadPublic",
        ],
    ]
]:
    """Get Current User Stack Service

    Args:
        stack_id (UUID):
        service_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, Union['FunctionServiceReadPublic', 'GithubServiceReadPublic', 'ImageServiceReadPublic', 'PostgresServiceReadPublic']]]
    """

    kwargs = _get_kwargs(
        stack_id=stack_id,
        service_id=service_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stack_id: UUID,
    service_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        Any,
        HTTPValidationError,
        Union[
            "FunctionServiceReadPublic",
            "GithubServiceReadPublic",
            "ImageServiceReadPublic",
            "PostgresServiceReadPublic",
        ],
    ]
]:
    """Get Current User Stack Service

    Args:
        stack_id (UUID):
        service_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, Union['FunctionServiceReadPublic', 'GithubServiceReadPublic', 'ImageServiceReadPublic', 'PostgresServiceReadPublic']]
    """

    return (
        await asyncio_detailed(
            stack_id=stack_id,
            service_id=service_id,
            client=client,
        )
    ).parsed
