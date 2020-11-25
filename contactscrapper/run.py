from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == "__main__":
    urls = open(0).read().splitlines()
    # urls = ['https://www.cmsenergy.com/contact-us/default.aspx',
    #         'https://www.illion.com.au',
    #         'https://www.phosagro.com/contacts',
    #         'https://www.powerlinx.com/contact',
    #         'https://www.cialdnb.com/en',
    #         'https://www.illion.com.au/contact-us']
    process = CrawlerProcess(get_project_settings())
    process.crawl('contactinfo', start_urls=urls)
    process.start()
