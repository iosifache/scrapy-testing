"""Unit tests for scrapy.utils.sitemap.Sitemap's constructor

Method type: Using objects from other classes
    (lxml.etree.ElementTree.Element.tag)
N/A criteria:
- Inverse relationship: No method is exposed to return the initial sitemap
    tree.
"""

import typing

import pytest
from lxml.etree import XMLSyntaxError, _Element
from scrapy.utils.sitemap import Sitemap

MANY_CONTENT = """
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url>
<loc>http://www.google.com/</loc>
<lastmod>2009-02-06</lastmod>
<changefreq>monthly</changefreq>
<priority>0.9</priority>
</url>
<url>
<loc>https://www.google.com/search?q=europecountry+article&oq=europe&aqs</loc>
<changefreq>day</changefreq>
</url>
<url>
<loc>https://www.google.com/search?q=europecountry+article&oq=europe&aqs</loc>
<lastmod>2010-11-20</lastmod>
<changefreq>weekly</changefreq>
</url>
<url>
<loc>https://www.zoho.com/writer/collaborative-writing.html</loc>
<lastmod>2006-11-21T16:00:13+00:00</lastmod>
<priority>0.4</priority>
</url>
<url>
<loc>http://www.example.com/catalog?item=83&amp;desc=vacation_usa</loc>
<lastmod>2006-10-23</lastmod>
</url>
</urlset>"""

SINGLE_CONTENT = """
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url>
<loc>http://www.google.com/</loc>
<priority>0.9</priority>
</url>
</urlset>"""

EMPTY_CONTENT = """
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
</urlset>
"""

EMPTY_STRING = ""

INVALID_CONTENT = """
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9>
><ur
</urlset>
"""


def check_root(root: typing.Any) -> bool:
    return isinstance(root, _Element)


@pytest.mark.timeout(1)
def test_valid_sitemap_with_many_urls() -> None:
    """Tests if a sitemap with multiple URLs is parsed correctly.

    Testing principles: right, cardinality (with many elements), performance
    """
    sitemap = Sitemap(MANY_CONTENT)

    assert sitemap.type == "urlset"
    assert check_root(sitemap._root)


@pytest.mark.timeout(1)
def test_valid_sitemap_with_single_url() -> None:
    """Tests if a sitemap with multiple URLs is parsed correctly.

    Testing principles: right, cardinality (with single element), performance
    """
    sitemap = Sitemap(SINGLE_CONTENT)

    assert sitemap.type == "urlset"
    assert check_root(sitemap._root)


@pytest.mark.timeout(1)
def test_empty_urlset() -> None:
    """Tests if a sitemap with multiple URLs is parsed correctly.

    Testing principles: right, cardinality (with no element), performance
    """
    sitemap = Sitemap(EMPTY_CONTENT)

    assert sitemap.type == "urlset"
    assert check_root(sitemap._root)


@pytest.mark.timeout(1)
def test_empty_parsing() -> None:
    """Tests if an error is raised when

    Testing principles: right, error, performance
    """
    try:
        Sitemap(EMPTY_STRING)
    except XMLSyntaxError:
        pass
    else:
        assert False


@pytest.mark.timeout(1)
def test_invalid_parsing() -> None:
    """Tests if no error is raised when passing an invalid XML string.

    Testing principles: right, boundary, performance
    """
    sitemap = Sitemap(INVALID_CONTENT)

    assert sitemap.type == "urlset"
    assert check_root(sitemap._root)
