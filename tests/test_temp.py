import pytest

from action_python_poetry.constants import HELLO_NAME, REPEATS


@pytest.mark.skip("Add some tests!")
def test_add_tests():
    assert False


def test_constants():
    """
    A placeholder test to generate a coverage report.
    """
    assert HELLO_NAME == "k2bd"
    assert REPEATS == 3
