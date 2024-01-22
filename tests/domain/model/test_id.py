import pprint
import sys

import pytest

from comic_completion.domain.model.id import Id

pprint.pprint(sys.path)


# @pytest.fixture(scope="function", autouse=True)
@pytest.fixture()
def setup() -> None:
    print("setup")
    yield


def test_main() -> None:
    assert True


def test_main2() -> None:
    id = Id("AAAA")
    assert id.value == "AAAA"


# def test_main2():
#     main.main()
#     assert True


# class TestMain(TestCase):
#     def test_main
