"""Unit tests for scrapy.crawler.CrawlerProcess.start

Method type: Taking time to process
N/A criteria:
- Inverse relationship: Not the case as the extracted links cannot be reverted
    to the initial, crawled websites
- Error: No exception is documented for this method.
"""
import pytest
from scrapy import Spider
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response
from scrapy.link import Link


class WrapperSpider(Spider):
    links = {}

    def parse(self, response: Response) -> None:
        links = response.css("a::attr(href)").extract()

        if self.name in WrapperSpider.links:
            WrapperSpider.links[self.name].append(links)
        else:
            WrapperSpider.links[self.name] = links


class ThreePagesScrapper(WrapperSpider):
    name = "lazy_three_websited"
    start_urls = [
        "https://www.smithfieldfoods.com/",
        "https://digi24.ro",
        "https://adevarul.ro",
    ]


def get_links(spider: WrapperSpider) -> list[Link]:
    return WrapperSpider.links[spider.name]


@pytest.mark.timeout(3)
def test_no_link() -> None:
    """Tests if the processing of three lazy websites does not result in a
    timeout.

    Testing principles: right, performance
    """
    process = CrawlerProcess()
    process.crawl(ThreePagesScrapper)
    process.start()

    links = get_links(ThreePagesScrapper)
    assert len(links) > 0, "No links were retrieved from the crawled websites."
