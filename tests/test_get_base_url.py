"""Unit tests for scrapy.utils.get_base_url

Method type: Using members from other classes (Response)
N/A criteria:
- Inverse relationship: No method is exposed to return the initial response
    from the base URL.
- Error: No exception is documented for this method.
"""

import pytest
from scrapy.utils.response import get_base_url


@pytest.mark.principle_right
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.technique_fake
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_without_base() -> None:
    """Tests if the base URL is returned correctly when no <base> in body."""

    class FakeResponseWithoutBase:
        text: str = "<b>Content</b>"
        url: str = "https://google.com"
        encoding: str = "utf-8"

    response = FakeResponseWithoutBase()

    url = get_base_url(response)
    assert url == "https://google.com", "The returned base URL in invalid."


@pytest.mark.principle_right
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.technique_fake
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_with_base() -> None:
    """Tests if the base URL is returned correctly when <base> in body."""

    class FakeResponseWithBase:
        text: str = "<base href='https://www.canonical.com'/><b>Content</b>"
        url: str = "https://google.com"
        encoding: str = "utf-8"

    response = FakeResponseWithBase()

    url = get_base_url(response)
    assert (
        url == "https://www.canonical.com"
    ), "The returned base URL, when specified in the body, is invalid."


@pytest.mark.principle_right
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.technique_fake
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_with_comments() -> None:
    """Tests if the base URL is returned correctly when <base> in commented."""

    class FakeResponseWithBase:
        text: str = (
            "<!-- <base href='https://www.canonical.com'/> --><b>Content</b>"
        )
        url: str = "https://google.com"
        encoding: str = "utf-8"

    response = FakeResponseWithBase()

    url = get_base_url(response)
    assert (
        url == "https://google.com"
    ), "The comments were not correctly eliminated."


@pytest.mark.principle_right
@pytest.mark.principle_range_lower
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.technique_fake
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_with_empty_content() -> None:
    """Tests if the base URL is returned correctly when empty body."""

    class FakeResponseWithBase:
        text: str = ""
        url: str = "https://google.com"
        encoding: str = "utf-8"

    response = FakeResponseWithBase()

    url = get_base_url(response)
    assert (
        url == "https://google.com"
    ), "The base URL is not returned correctly when the text is empty."


@pytest.mark.principle_right
@pytest.mark.principle_range_lower
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.technique_fake
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_with_empty_url_and_body() -> None:
    """Tests if the base URL is returned correctly when empty body and URL."""

    class FakeResponseWithBase:
        text: str = ""
        url: str = ""
        encoding: str = "utf-8"

    response = FakeResponseWithBase()

    url = get_base_url(response)
    assert (
        url == ""
    ), "The base URL is not returned correctly when the URL is empty."


@pytest.mark.principle_right
@pytest.mark.principle_range_lower
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.technique_fake
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_with_empty_url_and_base_in_body() -> None:
    """Tests if the base URL is returned correctly when specified only in body.
    """

    class FakeResponseWithBase:
        text: str = "<base href='https://www.canonical.com'/><b>Content</b>"
        url: str = ""
        encoding: str = "utf-8"

    response = FakeResponseWithBase()

    url = get_base_url(response)
    assert url == "https://www.canonical.com", (
        "The base URL is not returned correctly when the URL is empty, but"
        " <base> present in body."
    )
