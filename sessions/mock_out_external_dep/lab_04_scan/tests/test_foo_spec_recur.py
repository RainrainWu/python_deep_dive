import mock

patch_object = "sessions.mock_out_external_dep.lab_04_scan.foo.Ticker"


@mock.patch(patch_object, spec=True)
def test_add_one_mock_fixed_spec(mock_ticker):
    for i in dir(mock_ticker):
        print(i)
    print("==========[inner ticker attr]==========")
    for i in dir(mock_ticker.inner_ticker):
        print(i)


@mock.patch(patch_object, autospec=True)
def test_add_one_mock_recur_spec(mock_ticker):
    for i in dir(mock_ticker):
        print(i)
    print("==========[inner ticker attr]==========")
    for i in dir(mock_ticker.inner_ticker):
        print(i)
