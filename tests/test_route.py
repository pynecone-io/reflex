import pytest

from reflex.route import get_route_args, catchall_in_route
from reflex import constants


@pytest.mark.parametrize(
    "route_name, expected",
    [
        ("/users/[id]", {"id": constants.RouteArgType.SINGLE}),
        ("/posts/[postId]/comments/[commentId]",
         {"postId": constants.RouteArgType.SINGLE, "commentId": constants.RouteArgType.SINGLE}),
        ("/products/...", {"": constants.RouteArgType.LIST}),
        ("/products/[...]", {"": constants.RouteArgType.LIST})
    ]
)
def test_route_args(route_name, expected):
    assert get_route_args(route_name) == expected


@pytest.mark.parametrize(
    "route_name", [
        "/products/[id]/[id]",
        "/posts/[postId]/comments/[postId]",

    ]
)
def test_invalid_route_args(route_name):
    with pytest.raises(ValueError):
        get_route_args(route_name)


@pytest.mark.parametrize(
    "route_name,expected",
    [
        ("/events/[year]/[month]/[...slug]", "[...slug]"),
        ("pages/shop/[[...slug]]", "[[...slug]]")

    ]
)
def test_catchall_in_route(route_name, expected):
    assert catchall_in_route(route_name) == expected


