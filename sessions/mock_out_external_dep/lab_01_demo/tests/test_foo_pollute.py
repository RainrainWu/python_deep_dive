import math

import mock
import pytest

from sessions.mock_out_external_dep.lab_01_demo import foo


def test_store_num():
    assert foo.store_num(5) == True
    print(foo.my_database.get_all())


@pytest.mark.parametrize(
    "num",
    [
        (-2147483648),
        (0),
        pytest.param(-math.inf, marks=pytest.mark.xfail),
        pytest.param("6", marks=pytest.mark.xfail),
    ],
)
def test_store_num_parameterized(num):
    assert foo.store_num(num) == True
    print(foo.my_database.get_all())
