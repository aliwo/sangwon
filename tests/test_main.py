from app.main import my_service


def test_obvious() -> None:
    assert 1 + 1 == 2


def test_my_service() -> None:
    my_service()
