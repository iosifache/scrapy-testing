"""Unit tests for scrapy.utils.url._is_posix_path

Method type: Checking if a string has a correct format
N/A criteria:
- Inverse relationship: Not the case as the initial path can't be extracted
    from the resulted boolean
- Error: No exception is documented for this method.
"""

import pytest
from scrapy.utils.url import _is_posix_path


@pytest.mark.principle_right
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_valid_file() -> None:
    """Tests if a valid path is recognized as valid."""
    assert _is_posix_path(
        "/home/iosifache/unit/test.py"
    ), "A valid folder is not recognized as valid."


@pytest.mark.principle_right
@pytest.mark.principle_range_lower
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_root() -> None:
    """Tests if the root folder is recognized as valid."""
    assert _is_posix_path("/."), "The root folder is not recognized as valid."


@pytest.mark.principle_right
@pytest.mark.principle_range_lower
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_home() -> None:
    """Tests if the home folder is recognized as valid."""
    assert _is_posix_path("~/."), "The home folder is not recognized as valid."


@pytest.mark.principle_right
@pytest.mark.principle_range_lower
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_working_directory() -> None:
    """Tests if the working folder is recognized as valid."""
    assert _is_posix_path(
        "./."
    ), "The working folder is not recognized as valid."


@pytest.mark.principle_right
@pytest.mark.principle_range_lower
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_parent_directory() -> None:
    """Tests if the parent folder is recognized as valid."""
    assert _is_posix_path(
        "../."
    ), "The parent folder is not recognized as valid."


@pytest.mark.principle_right
@pytest.mark.principle_conformance
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_windows_path() -> None:
    """Tests if a Windows path is recognized as invalid."""
    assert not _is_posix_path(
        "C:\\Users\\iosifache"
    ), "A Windows path is recognized as valid."


@pytest.mark.principle_right
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.principle_existence
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_null_path() -> None:
    """Tests if am empty path is recognized as invalid."""
    assert not _is_posix_path(""), "An empty path is recognized as valid."
