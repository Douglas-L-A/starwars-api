from app.utils.pagination import apply_limit


def test_apply_limit_none():
    data = list(range(10))

    result = apply_limit(data, None)

    assert result == data


def test_apply_limit_valid():
    data = list(range(10))

    result = apply_limit(data, 5)

    assert result == [0, 1, 2, 3, 4]


def test_apply_limit_greater_than_data():
    data = list(range(5))

    result = apply_limit(data, 10)

    assert result == data


def test_apply_limit_max_50():
    data = list(range(100))

    result = apply_limit(data, 80)

    assert len(result) == 50


def test_apply_limit_invalid_value():
    data = list(range(10))

    result = apply_limit(data, "abc")

    assert result == data
