"""Unit tests for scrapy.robotstxt.PythonRobotParser.allowed

Method type: Simplifying the usage of other functionality (from
    urllib.robotparser.RobotFileParser)
N/A criteria:
- Inverse relationship: No method is exposed to return the intial robots.txt.
"""

import pytest
from scrapy.robotstxt import PythonRobotParser

DUMMY_ROBOTSTXT = """
User-agent: *
Disallow: /

User-agent: Googlebot
Disallow:
"""


@pytest.mark.principle_right
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.robotstxt_testing
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_valid_robots() -> None:
    """Tests if a valid file is parsed correctly."""
    robot = PythonRobotParser(DUMMY_ROBOTSTXT, None)

    assert robot, "No parser was created."
    assert robot.allowed(
        "/", "Googlebot"
    ), "Googlebot is not allowed to crawl."
    assert not robot.allowed(
        "/", "YandexBot"
    ), "YandexBot is allowed to crawl."


@pytest.mark.principle_right
@pytest.mark.principle_range_lower
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.robotstxt_testing
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_empty_file() -> None:
    """Tests if no error is raised when giving an empty file."""
    robot = PythonRobotParser("", None)

    assert robot, "No parser was created."
    assert robot.allowed(
        "/", "Googlebot"
    ), "Googlebot is not allowed to crawl."
    assert robot.allowed(
        "/", "YandexBot"
    ), "YandexBot is not allowed to crawl."


@pytest.mark.principle_right
@pytest.mark.principle_time
@pytest.mark.principle_performance
@pytest.mark.robotstxt_testing
@pytest.mark.offline
@pytest.mark.timeout(0.1)
def test_no_robotstxt_at_all() -> None:
    """Tests if an error is raised when giving a None."""
    try:
        PythonRobotParser(None, None)
    except TypeError:
        pass
    else:
        assert False, "No error is raised when parsing a None."
