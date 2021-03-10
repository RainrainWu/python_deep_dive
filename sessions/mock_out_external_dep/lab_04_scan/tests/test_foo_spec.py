import mock

patch_object = "sessions.mock_out_external_dep.lab_04_scan.foo.Ticker"


@mock.patch(patch_object)
def test_add_one_mock_free_spec(mock_ticker):
    for i in dir(mock_ticker):
        print(i)
    print(mock_ticker.unknow_attr())
    assert mock_ticker.unknow_attr()


@mock.patch(patch_object, spec=True)
def test_add_one_mock_fixed_spec(mock_ticker):
    for i in dir(mock_ticker):
        print(i)
    assert mock_ticker.unknow_attr()
