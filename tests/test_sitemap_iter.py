"""Unit tests for scrapy.utils.sitemap.Sitemap.__iter__

Method type: Using methods from other classes (lxml.etree.XMLParser.getchildren)
N/A criteria:
- Inverse relationship: No method is exposed to return the initial sitemap
    tree.
"""

import typing

import pytest
from scrapy.utils.sitemap import Sitemap

EMPTY_URLSET_SITEMAP = """
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
</urlset>
"""

SITEMAP_WITH_ONE_LINK = """
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url>
<loc>http://www.google.com/</loc>
<priority>0.9</priority>
</url>
</urlset>"""

SITEMAP_WITH_MULTIPLE_LINK = """
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


def __check_node(node: typing.Any) -> bool:
    return isinstance(node, dict) and "loc" in node.keys()


@pytest.mark.timeout(1)
def test_empty_urlset() -> None:
    """Tests if a sitemap with multiple URLs is parsed correctly.

    Testing principles: right, cardinality with 0 elements, performance
    """
    sitemap = Sitemap(EMPTY_URLSET_SITEMAP)

    nodes_count = 0
    for _ in sitemap:
        nodes_count += 1

    assert nodes_count == 0


@pytest.mark.timeout(1)
def test_valid_sitemap_with_single_url() -> None:
    """Tests if a sitemap with multiple URLs is parsed correctly.

    Testing principles: right, cardinality with 1 element, performance,
        conformance
    """
    sitemap = Sitemap(SITEMAP_WITH_ONE_LINK)

    nodes_count = 0
    for elem in sitemap:
        assert __check_node(elem)

        nodes_count += 1

    assert nodes_count == 1


@pytest.mark.timeout(1)
def test_valid_sitemap_with_many_urls() -> None:
    """Tests if a sitemap with multiple URLs is parsed correctly.

    Testing principles: right, cardinality with N elements, performance,
        conformance
    """
    sitemap = Sitemap(SITEMAP_WITH_MULTIPLE_LINK)

    nodes_count = 0
    for elem in sitemap:
        assert __check_node(elem)

        nodes_count += 1

    assert nodes_count == 5
