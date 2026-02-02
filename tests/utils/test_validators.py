import pytest
from werkzeug.exceptions import BadRequest

from app.utils.validators import (
    validate_order,
    validate_order_by,
    validate_filters
)

# validate_order
def test_validate_order_default():
    assert validate_order(None) == "asc"


def test_validate_order_valid_asc():
    assert validate_order("asc") == "asc"


def test_validate_order_valid_desc():
    assert validate_order("DESC") == "desc"


def test_validate_order_invalid():
    with pytest.raises(BadRequest):
        validate_order("banana")


# validate_order_by
def test_validate_order_by_none():
    allowed = ["name", "height"]
    assert validate_order_by(None, allowed) is None


def test_validate_order_by_valid():
    allowed = ["name", "height"]
    assert validate_order_by("name", allowed) == "name"


def test_validate_order_by_invalid():
    allowed = ["name", "height"]
    with pytest.raises(BadRequest):
        validate_order_by("banana", allowed)

# validate_filters
def test_validate_filters_valid():
    query_params = {"name": "Luke"}
    allowed = ["name", "gender"]

    # não deve levantar exceção
    validate_filters(query_params, allowed)


def test_validate_filters_ignore_technical_params():
    query_params = {
        "order": "asc",
        "order_by": "name",
        "limit": "10"
    }
    allowed = ["name"]

    validate_filters(query_params, allowed)


def test_validate_filters_invalid():
    query_params = {"banana": "Luke"}
    allowed = ["name", "gender"]

    with pytest.raises(BadRequest):
        validate_filters(query_params, allowed)
