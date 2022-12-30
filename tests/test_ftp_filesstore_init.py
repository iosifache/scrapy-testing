"""Unit tests for scrapy.pipelines.file.FTPFilesStore's contructor

Method type: Working with values within a range
"""

import pytest
from scrapy.pipelines.files import FTPFilesStore

VALID_CONNECTION_PARAMETERS = (
    "ftp://",
    "demo",
    "password",
    "test.rebex.net",
    22,
)


def constructor_wrapper(
    schema: str, username: str, password: str, hostname: str, port: int
) -> FTPFilesStore:
    return FTPFilesStore(f"{schema}{username}:{password}@{hostname}:{port}")


@pytest.mark.timeout(0.1)
def test_valid_parameters() -> None:
    """Tests if no error is raised when passing a valid connection string.

    Testing principles: right, performance, inverse relationship
    """
    schema, username, password, hostname, port = VALID_CONNECTION_PARAMETERS
    client = constructor_wrapper(schema, username, password, hostname, port)

    assert client, "The contructor returned None."
    assert client.username == username, "The username is invalid."
    assert client.password == password, "The password is invalid."
    assert client.host == hostname, "The hostname is invalid."
    assert client.port == port, "The post is invalid."


@pytest.mark.timeout(0.1)
def test_no_schema() -> None:
    """Tests if an error is raised when no schema is provided.

    Testing principles: right, error
    """
    schema, username, password, hostname, port = VALID_CONNECTION_PARAMETERS
    schema = ""

    try:
        constructor_wrapper(schema, username, password, hostname, port)
    except ValueError:
        pass
    else:
        assert False, "No error was raised when ommiting schema."


@pytest.mark.timeout(0.1)
def test_lowest_port() -> None:
    """Tests if no error is raised when using the lowest port.

    Testing principles: right, range (with lower limit)
    """
    schema, username, password, hostname, port = VALID_CONNECTION_PARAMETERS
    port = 1

    client = constructor_wrapper(schema, username, password, hostname, port)

    assert client, "The contructor returned None."
    assert client.username == username, "The username is invalid."
    assert client.password == password, "The password is invalid."
    assert client.host == hostname, "The hostname is invalid."
    assert client.port == port, "The post is invalid."


@pytest.mark.timeout(0.1)
def test_negative_port() -> None:
    """Tests if an error is raised on a negative value.

    Testing principles: right, error
    """
    schema, username, password, hostname, port = VALID_CONNECTION_PARAMETERS
    port = -1

    try:
        constructor_wrapper(schema, username, password, hostname, port)
    except ValueError:
        pass
    else:
        assert (
            False
        ), "No error was raised when offering a negative value as port."


@pytest.mark.timeout(0.1)
def test_above_max_port() -> None:
    """Tests if an error is when using a port exceeding the maximum value.

    Testing principles: right, error
    """
    schema, username, password, hostname, port = VALID_CONNECTION_PARAMETERS
    port = 65536

    try:
        constructor_wrapper(schema, username, password, hostname, port)
    except ValueError:
        pass
    else:
        assert False, (
            "No exception was raised when offering a port exceeding the"
            " maximum allowed one."
        )
