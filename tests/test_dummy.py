from dummy import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_failing():
    assert __version__ == '5.1.0'
