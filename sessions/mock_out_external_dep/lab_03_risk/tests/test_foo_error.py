import mock

from sessions.mock_out_external_dep.lab_03_risk import foo

patch_object = "sessions.mock_out_external_dep.lab_03_risk.foo.add_one"


def test_add_one_and_mul_two_wrong_param_error():
    result = foo.add_one_and_mul_two([1])


@mock.patch(patch_object)
def test_add_one_and_mul_two_wrong_method(mock_add_one):
    mock_add_one.return_value = 5
    result = foo.add_one_and_mul_two([1])
    mock_add_one.assret_called_once_with([1])
    print(result)
