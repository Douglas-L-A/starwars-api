from app.utils.filters import filter_characters


# filter_characters
def test_filter_characters_by_name():
    data = [
        {"name": "Luke Skywalker", "gender": "male"},
        {"name": "Leia Organa", "gender": "female"},
    ]

    query_params = {"name": "Luke"}

    result = filter_characters(data, query_params)

    assert len(result) == 1
    assert result[0]["name"] == "Luke Skywalker"


def test_filter_characters_by_gender():
    data = [
        {"name": "Luke", "gender": "male"},
        {"name": "Leia", "gender": "female"},
        {"name": "Han", "gender": "male"},
    ]

    query_params = {"gender": "male"}

    result = filter_characters(data, query_params)

    assert len(result) == 2
    assert all(c["gender"] == "male" for c in result)


def test_filter_characters_multiple_filters():
    data = [
        {"name": "Luke Skywalker", "gender": "male"},
        {"name": "Luke Clone", "gender": "female"},
    ]

    query_params = {
        "name": "Luke",
        "gender": "male"
    }

    result = filter_characters(data, query_params)

    assert len(result) == 1
    assert result[0]["gender"] == "male"


def test_filter_characters_no_filters():
    data = [
        {"name": "Luke", "gender": "male"},
        {"name": "Leia", "gender": "female"},
    ]

    query_params = {}

    result = filter_characters(data, query_params)

    assert len(result) == 2



def test_filter_characters_ignore_technical_params():
    data = [
        {"name": "Luke", "gender": "male"},
        {"name": "Leia", "gender": "female"},
    ]

    query_params = {
        "order": "asc",
        "order_by": "name",
        "limit": "1"
    }

    result = filter_characters(data, query_params)

    assert len(result) == 2


# filter_films
from app.utils.filters import filter_films


def test_filter_films_by_title():
    data = [
        {"title": "A New Hope"},
        {"title": "The Empire Strikes Back"},
    ]

    query_params = {"title": "Hope"}

    result = filter_films(data, query_params)

    assert len(result) == 1
    assert result[0]["title"] == "A New Hope"
