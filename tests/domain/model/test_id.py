import pytest

from comic_completion.domain.model.id import Id


# @pytest.fixture(scope="function", autouse=True)
@pytest.fixture()
def setup():
    print("setup")
    yield


def test_main():
    assert True


def test_main2():
    id = Id("AAAA")
    assert id.value == "AAAA"


# def test_main2():
#     main.main()
#     assert True


# class TestMain(TestCase):
#     def test_main
