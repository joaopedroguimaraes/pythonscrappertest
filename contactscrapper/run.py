from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == "__main__":
    urls = open(0).read().splitlines()
    process = CrawlerProcess(get_project_settings())
    process.crawl('contactinfo', start_urls=urls)
    process.start()
