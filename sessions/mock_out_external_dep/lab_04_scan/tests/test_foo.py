from sessions.mock_out_external_dep.lab_04_scan import foo


def test_add_one_raw():
    for i in dir(foo.add_one):
        print(i)
