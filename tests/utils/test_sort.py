from app.utils.sort import sort_results


def test_sort_without_order_by():
    data = [
        {"name": "B"},
        {"name": "A"},
    ]

    result = sort_results(data, order_by=None, order="asc")

    assert result == data


def test_sort_string_asc():
    data = [
        {"name": "Leia"},
        {"name": "Luke"},
        {"name": "Anakin"},
    ]

    result = sort_results(data, order_by="name", order="asc")

    names = [item["name"] for item in result]

    assert names == ["Anakin", "Leia", "Luke"]


def test_sort_string_desc():
    data = [
        {"name": "Leia"},
        {"name": "Luke"},
        {"name": "Anakin"},
    ]

    result = sort_results(data, order_by="name", order="desc")

    names = [item["name"] for item in result]

    assert names == ["Luke", "Leia", "Anakin"]


def test_sort_numeric_field():
    data = [
        {"name": "A", "height": "180"},
        {"name": "B", "height": "170"},
        {"name": "C", "height": "190"},
    ]

    result = sort_results(data, order_by="height", order="asc")

    heights = [item["height"] for item in result]

    assert heights == ["170", "180", "190"]


def test_sort_unknown():
    data = [
        {"name": "A", "height": "unknown"},
        {"name": "B", "height": "170"},
        {"name": "C", "height": "180"},
    ]

    result = sort_results(data, order_by="height", order="asc")

    heights = [item["height"] for item in result]

    assert heights[-1] == "unknown"
