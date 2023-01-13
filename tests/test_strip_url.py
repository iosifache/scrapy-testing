"""Unit tests for scrapy.utils.url.strip_url

N/A criteria:
- Inverse relationship: Not the case as the initial URL can't be retrieved.
- Error: No exception is documented for this method.
"""

import pytest
from scrapy.utils.url import strip_url


@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_strip_credentials() -> None:
    """Tests if an URL containing credentials is stripped correctly.

    Testing principles: right, performance
    """
    stripped = strip_url(
        "https://user:password@google.com", strip_credentials=True
    )

    assert (
        stripped == "https://google.com"
    ), "The returned stripped URL with credentials is invalid."


@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_strip_default_port() -> None:
    """Tests if an URL containing the default port is stripped correctly.

    Testing principles: right, performance
    """
    stripped = strip_url("https://google.com:443", strip_default_port=True)

    assert (
        stripped == "https://google.com"
    ), "The returned stripped URL with default port is invalid."


@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_strip_origin() -> None:
    """Tests if an URL containing a path is stripped correctly.

    Testing principles: right, performance
    """
    stripped = strip_url("https://google.com/search", origin_only=True)

    assert (
        stripped == "https://google.com/"
    ), "The returned stripped URL with path is invalid."


@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_strip_fragment() -> None:
    """Tests if an URL containing a fragment is stripped correctly.

    Testing principles: right, performance
    """
    stripped = strip_url(
        "https://google.com/search#result", strip_fragment=True
    )

    assert (
        stripped == "https://google.com/search"
    ), "The returned stripped URL with fragment is invalid."


@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_strip_all_features() -> None:
    """Tests if an overly qualified URL is trimmed correctly.

    Testing principles: right, performance
    """
    stripped = strip_url(
        "https://user:password@google.com:443/search#result",
        strip_credentials=True,
        strip_default_port=True,
        origin_only=True,
        strip_fragment=True,
    )

    assert (
        stripped == "https://google.com/"
    ), "A fully quallified URL is not stripped correctly."


@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_strip_empty_url() -> None:
    """Tests if an empty URL don't generate any error when processed.

    Testing principles: right, performance, range (with lower limit)
    """
    stripped = strip_url(
        "",
        strip_credentials=True,
        strip_default_port=True,
        origin_only=True,
        strip_fragment=True,
    )

    assert stripped == "/", "The empty URL is not processed correctly."
