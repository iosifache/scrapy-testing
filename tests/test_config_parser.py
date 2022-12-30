"""Unit tests for scrapy.utils.conf.get_config

Method type: Processing files
"""

import tempfile
from configparser import ParsingError

import pytest
from scrapy.utils.conf import ConfigParser, get_config

EMPTY_CONFIG = ""

ONE_KEY_CONFIG = """[simple]
key = value
"""

TWO_KEYS_CONFIG = """[simple]
key = value
new_key = new_value
"""

ERRONEOUS_CONFIG = """[simple]
key
"""


def __mock_get_sources_with_valid_one_key_config(_: bool) -> list[str]:
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(ONE_KEY_CONFIG.encode("utf-8"))

    return [temp.name]


def __mock_get_sources_with_valid_two_keys_config(_: bool) -> list[str]:
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(TWO_KEYS_CONFIG.encode("utf-8"))

    return [temp.name]


def __mock_get_sources_with_empty_config(_: bool) -> list[str]:
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(EMPTY_CONFIG.encode("utf-8"))

    return [temp.name]


def __mock_get_sources_with_inexistent_config(_: bool) -> list[str]:
    return ["/path/to/no/config"]


def __mock_get_sources_with_erroneous_file(_: bool) -> list[str]:
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(ERRONEOUS_CONFIG.encode("utf-8"))

    return [temp.name]


def __check_dumped_content(config: ConfigParser, original_content: str) -> bool:
    temp = tempfile.TemporaryFile(mode="w+")
    config.write(temp)
    temp.flush()
    temp.seek(0)
    is_identical = temp.read().strip() == original_content.strip()
    temp.close()

    return is_identical


@pytest.mark.timeout(0.1)
def test_empty_file(
    capsys: pytest.CaptureFixture, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Tests if a valid configuration with two keys is loaded correctly.

    Testing principles: right, cardinality of 0 elements, inverse relationship,
        performance
    Testing technique: monkey patching
    """
    monkeypatch.setattr(
        "scrapy.utils.conf.get_sources", __mock_get_sources_with_inexistent_config
    )

    config = get_config()
    assert config, "The inexistent configuration was not loaded at all."
    assert config.sections() == [], "The inexistent configuration was misrepresented."


@pytest.mark.timeout(0.1)
def test_valid_parsing_of_one_key(
    capsys: pytest.CaptureFixture, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Tests if a valid configuration with one key is loaded correctly.

    Testing principles: right, cardinality of one element, inverse relationship,
        performance
    Testing technique: monkey patching
    """
    monkeypatch.setattr(
        "scrapy.utils.conf.get_sources", __mock_get_sources_with_valid_one_key_config
    )

    config = get_config()

    assert (
        config["simple"]["key"] == "value"
    ), "A value from the configuration was wrongly loaded."

    assert __check_dumped_content(
        config, ONE_KEY_CONFIG
    ), "The dumped configuration is different than the original one, with one key."


@pytest.mark.timeout(0.1)
def test_valid_parsing_of_two_keys(
    capsys: pytest.CaptureFixture, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Tests if a valid configuration with two keys is loaded correctly.

    Testing principles: right, cardinality of N elements, inverse relationship,
        performance
    Testing technique: monkey patching
    """
    monkeypatch.setattr(
        "scrapy.utils.conf.get_sources", __mock_get_sources_with_valid_two_keys_config
    )

    config = get_config()

    assert (
        config["simple"]["key"] == "value"
        and config["simple"]["new_key"] == "new_value"
    ), "A value from the configuration was wrongly loaded."

    assert __check_dumped_content(
        config, TWO_KEYS_CONFIG
    ), "The dumped configuration is different than the original one, with two key."


@pytest.mark.timeout(0.1)
def test_no_file(
    capsys: pytest.CaptureFixture, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Tests if no error is raised when parsing an inexistent file.

    Testing principles: right, existence, inverse relationship, performance
    Testing technique: monkey patching
    """
    monkeypatch.setattr(
        "scrapy.utils.conf.get_sources", __mock_get_sources_with_empty_config
    )

    config = get_config()
    assert config, "The empty configuration was not loaded at all."
    assert config.sections() == [], "The empty configuration was misrepresented."


@pytest.mark.timeout(0.1)
def test_file_with_errors(
    capsys: pytest.CaptureFixture, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Tests if an error is raised when parsing an invalid configuration.

    Testing principles: right, error, performance
    Testing technique: monkey patching
    """
    monkeypatch.setattr(
        "scrapy.utils.conf.get_sources", __mock_get_sources_with_erroneous_file
    )

    try:
        get_config()
    except ParsingError:
        pass
    else:
        assert (
            False
        ), "No exception was raised when parsing a configuration file containing errors."
