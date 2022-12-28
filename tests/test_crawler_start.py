import pytest
from scrapy import Spider
from scrapy.crawler import CrawlerProcess
from scrapy.link import Link


class WrapperSpider(Spider):
    name = "all_pages_spider"
    links = {}

    def parse(self, response):
        links = response.css("a::attr(href)").extract()

        if self.name in WrapperSpider.links:
            WrapperSpider.links[self.name].append(links)
        else:
            WrapperSpider.links[self.name] = links


class ThreePagesScrapper(WrapperSpider):
    name = "three"
    start_urls = [
        "https://www.smithfieldfoods.com/",
        "https://digi24.ro",
        "https://adevarul.ro",
    ]


@pytest.fixture(scope="module", autouse=True)
def setup_function() -> None:
    print("executed")
    process = CrawlerProcess()

    process.crawl(ThreePagesScrapper)

    process.start()


def get_links(spider: WrapperSpider) -> list[Link]:
    return WrapperSpider.links[spider.name]


@pytest.mark.timeout(1)
def test_no_link() -> None:
    """Tests if no link is returned for an isolated page.

    Testing principles: right, performance, cardinality of 0 elements
    """
    links = get_links(ThreePagesScrapper)

    print(links)
