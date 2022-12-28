"""Unit tests for scrapy.linkextractors.LinkExtractor.extract_links

Method type: Returning a list
N/A criteria:
- Inverse relationship: Not the case as the links cannot produce the initial
    webpage
- Error: No exception is documented for this method.
"""

import pytest
from scrapy import Spider
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response
from scrapy.link import Link
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.url import is_url


class WrapperSpider(Spider):
    link_extractor = LinkExtractor()
    links = {}

    def parse(self, response: Response) -> None:
        WrapperSpider.links[self.name] = self.link_extractor.extract_links(response)


class NoLinkSpider(WrapperSpider):
    name = "none"
    start_urls = ["https://itcorp.com/"]


class SingleLinkSpider(WrapperSpider):
    name = "single"
    start_urls = ["https://milk.com/faq/"]


class MultipleLinksSpider(WrapperSpider):
    name = "multiple"
    start_urls = ["https://iosifache.me/about"]


@pytest.fixture(scope="module", autouse=True)
def setup_function() -> None:
    print("executed")
    process = CrawlerProcess()

    process.crawl(NoLinkSpider)
    process.crawl(SingleLinkSpider)
    process.crawl(MultipleLinksSpider)

    process.start()


def __get_links(spider: WrapperSpider) -> list[Link]:
    return WrapperSpider.links[spider.name]


@pytest.mark.timeout(1)
def test_no_link() -> None:
    """Tests if no link is returned for an isolated page.

    Testing principles: right, performance, cardinality of 0 elements
    """
    links = __get_links(NoLinkSpider)

    assert len(links) == 0


@pytest.mark.timeout(1)
def test_one_link() -> None:
    """Tests if a single link is returned for a specific page.

    Testing principles: right, performance, conformance with link format,
        cardinality of 1 element
    """
    links = __get_links(SingleLinkSpider)

    assert len(links) == 1
    assert is_url(links[0].url)


@pytest.mark.timeout(1)
def test_multiple_links() -> None:
    """Tests if multiple links are returned.

    Testing principles: right, performance, conformance with link format,
        cardinality of N elements
    """
    links = __get_links(MultipleLinksSpider)

    assert len(links) == 13
    for link in links:
        assert is_url(link.url)
