import mock

from sessions.mock_out_external_dep.lab_02_scope import foo

patch_object = "sessions.mock_out_external_dep.lab_02_scope.foo.add_one"


def test_add_one_and_mul_two_context_manager():
    with mock.patch(patch_object) as mock_add_one:
        mock_add_one.return_value = 5
        result = foo.add_one_and_mul_two(1)
        mock_add_one.assert_called_once_with(1)
    print(result)


@mock.patch(patch_object)
def test_add_one_and_mul_two_function_decorator(mock_add_one):
    mock_add_one.return_value = 5
    result = foo.add_one_and_mul_two(1)
    mock_add_one.assert_called_once_with(1)
    print(result)


@mock.patch(patch_object)
class TestClassMockFoo:
    def test_add_one_and_mul_two_class_decorator(self, mock_add_one):
        mock_add_one.return_value = 5
        result = foo.add_one_and_mul_two(1)
        mock_add_one.assert_called_once_with(1)
        print(result)
