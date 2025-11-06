import pytest


def test_import_wemakesnake():
    try:
        import wemakesnake           # noqa
    except ImportError:
        pytest.fail('import wemakesnake failed')
