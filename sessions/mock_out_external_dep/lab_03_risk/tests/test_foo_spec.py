import mock

from sessions.mock_out_external_dep.lab_03_risk import foo

patch_object = "sessions.mock_out_external_dep.lab_03_risk.foo.add_one"


@mock.patch(patch_object, spec=True)
def test_add_one_and_mul_two_wrong_param(mock_add_one):
    mock_add_one.return_value = 5
    result = foo.add_one(1, 2)
    mock_add_one.assert_called_once_with(1, 2)
    print(result)


@mock.patch(patch_object, spec=True)
def test_add_one_and_mul_two_wrong_method(mock_add_one):
    mock_add_one.return_value = 5
    result = foo.add_one(1)
    mock_add_one.sasert_called_once_with(1)
    print(result)
