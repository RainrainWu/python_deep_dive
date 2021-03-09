import mock

patch_object = "sessions.mock_out_external_dep.lab_04_scan.foo.add_one"


@mock.patch(patch_object)
def test_add_one_mock_free_spec(mock_add_one):
    for i in dir(mock_add_one):
        print(i)
    print(mock_add_one.unknow_attr())
    assert mock_add_one.unknow_attr()


@mock.patch(patch_object, spec=True)
def test_add_one_mock_fixed_spec(mock_add_one):
    for i in dir(mock_add_one):
        print(i)
    assert mock_add_one.unknow_attr()
