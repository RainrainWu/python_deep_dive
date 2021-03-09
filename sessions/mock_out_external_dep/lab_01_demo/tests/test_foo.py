import math

import mock
import pytest

from sessions.mock_out_external_dep.lab_01_demo import foo


@pytest.mark.parametrize(
    "num",
    [
        (-2147483648),
        (0),
        pytest.param(-math.inf, marks=pytest.mark.xfail),
        pytest.param("6", marks=pytest.mark.xfail),
    ],
)
@mock.patch("sessions.mock_out_external_dep.lab_01_demo.foo.my_database", autospec=True)
def test_append_num_mock(mock_db, num):
    mock_db.add.return_value = True
    assert foo.store_num(num) == True
    mock_db.add.assert_called()
    print(foo.my_database.get_all())


@mock.patch("sessions.mock_out_external_dep.lab_01_demo.foo.my_database", autospec=True)
def test_append_num_mock_full(mock_db):
    mock_db.add.side_effect = OverflowError("storage is already full.")
    with pytest.raises(OverflowError):
        foo.store_num(5)
    mock_db.add.assert_called()
