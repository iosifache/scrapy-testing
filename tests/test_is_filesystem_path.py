"""Unit tests for scrapy.utils.url._is_posix_path

Method type: Checking if a string has a correct format
N/A criteria:
- Inverse relationship: Not the case as the initial path can't be extracted
    from the resulted boolean
- Error: No exception is documented for this method.
"""

import pytest
from scrapy.utils.url import _is_posix_path


@pytest.mark.timeout(1)
def test_valid_file() -> None:
    """Tests if a valid path is recognized as valid.

    Testing principles: right, performance
    """
    assert _is_posix_path("/home/iosifache/unit/test.py")


@pytest.mark.timeout(1)
def test_root() -> None:
    """Tests if the root folder is recognized as valid.

    Testing principles: right, performance, range (with lower limit)
    """
    assert _is_posix_path("/.")


@pytest.mark.timeout(1)
def test_home() -> None:
    """Tests if the home folder is recognized as valid.

    Testing principles: right, performance, range (with lower limit)
    """
    assert _is_posix_path("~/.")


@pytest.mark.timeout(1)
def test_working_directory() -> None:
    """Tests if the working folder is recognized as valid.

    Testing principles: right, performance, range (with lower limit)
    """
    assert _is_posix_path("./.")


@pytest.mark.timeout(1)
def test_parent_directory() -> None:
    """Tests if the parent folder is recognized as valid.

    Testing principles: right, performance, range (with lower limit)
    """
    assert _is_posix_path("../.")


@pytest.mark.timeout(1)
def test_windows_path() -> None:
    """Tests if a Windows path is recognized as invalid.

    Testing principles: right, performance, conformance
    """
    assert not _is_posix_path("C:\\Users\\iosifache")


@pytest.mark.timeout(1)
def test_null_path() -> None:
    """Tests if am empty path is recognized as invalid

    Testing principles: right, performance, existence
    """
    assert not _is_posix_path("")
