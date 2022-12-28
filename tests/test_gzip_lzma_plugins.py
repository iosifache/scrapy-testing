"""Unit tests for GzipPlugin and LZMAPlugin from scrapy.extensions.postprocessing

Methods type: Returning an integer
"""

import gzip
import lzma
import tempfile

import pytest
from scrapy.extensions.postprocessing import GzipPlugin, LZMAPlugin


def gzip_wrapper(filename: str, data: bytes) -> int:
    with open(filename, "wb") as file:
        plugin = GzipPlugin(
            file,
            feed_options={
                "gzip_compresslevel": 9,
                "gzip_mtime": 0,
                "gzip_filename": "",
            },
        )
        return_code = plugin.write(data)
        plugin.close()

        return return_code


def lzma_wrapper(filename: str, data: bytes) -> int:
    with open(filename, "wb") as file:
        plugin = LZMAPlugin(file, feed_options={})
        return_code = plugin.write(data)
        plugin.close()

        return return_code


def gzip_inverse(filename: str) -> bytes:
    return gzip.open(filename).read()


def lzma_inverse(filename: str) -> bytes:
    return lzma.open(filename).read()


@pytest.mark.timeout(1)
def test_gzip_valid_content() -> None:
    """Tests if content is written correctly into the GZIP file.

    Testing principles: right, performance, inverse relationship
    """
    data = b"data"

    with tempfile.NamedTemporaryFile("wb", delete=False) as temp:
        return_code = gzip_wrapper(temp.name, data)
        assert return_code != 0

        uncompressed_content = gzip_inverse(temp.name)
        assert data == uncompressed_content


@pytest.mark.timeout(1)
def test_lzma_valid_content() -> None:
    """Tests if content is written correctly into the LZMA file.

    Testing principles: right, performance, inverse relationship
    """
    data = b"data"

    with tempfile.NamedTemporaryFile("wb", delete=False) as temp:
        return_code = lzma_wrapper(temp.name, data)
        assert return_code != 0

        uncompressed_content = lzma_inverse(temp.name)
        assert data == uncompressed_content


@pytest.mark.timeout(1)
def test_gzip_zero_length() -> None:
    """Tests if length 0 is returned when passing empty input to GZIP.

    Testing principles: right, performance, range
    """
    data = b""

    with tempfile.NamedTemporaryFile("wb", delete=False) as temp:
        return_code = gzip_wrapper(temp.name, data)
        assert return_code == 0


@pytest.mark.timeout(1)
def test_lzma_zero_length() -> None:
    """Tests if length 0 is returned when passing empty input to LZMA.

    Testing principles: right, performance, range
    """
    data = b""

    with tempfile.NamedTemporaryFile("wb", delete=False) as temp:
        return_code = lzma_wrapper(temp.name, data)
        assert return_code == 0


@pytest.mark.timeout(1)
def test_gzip_inexistent_file() -> None:
    """Tests if generic exception is raised when passing an inexistent file
        to GZIP.

    Testing principles: performance, existence
    """
    try:
        gzip_wrapper("/path/to/no/file", b"exception")
    except Exception:
        pass
    else:
        assert False


@pytest.mark.timeout(1)
def test_lzma_inexistent_file() -> None:
    """Tests if generic exception is raised when passing an inexistent file
        to LZMA.

    Testing principles: performance, existence
    """
    try:
        lzma_wrapper("/path/to/no/file", b"exception")
    except Exception:
        pass
    else:
        assert False