import pytest

import sys
sys.path.append('C:\\workspace\\local-tools\\comic-completion\\comic_completion')
import pprint
pprint.pprint(sys.path)
from comic_completion.domain.model.comic import Comic


# @pytest.fixture(scope="function", autouse=True)
@pytest.fixture()
def setup():
    print("setup")
    yield


def test_main():
    assert True


def test_main2():
    comic = Comic("aaa", None)
    assert True

