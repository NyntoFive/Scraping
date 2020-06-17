from datetime import datetime
from scrapy.spiders import SitemapSpider, Spider, CSVFeedSpider


class FilteredSitemapSpider(Spider):
    name = "testy"
    allowed_domains = ["knifekits.com"]

    # sitemap_urls = ["http://knifekits.com/vcom/knifekits-smproducts.xml"]


    start_urls = []

    def parse(self, response):
        item = {}
        item["pid"] = response.xpath("//input[@name='products_id']/@value").get(),
        item["sku"] = response.xpath(".//*[@itemprop='model']/text()").get(),
        item["description"] = response.xpath(".//*[@itemprop='description']/descendant-or-self::text()").getall(),
        item["metaKeywords"] = response.xpath(".//meta[@name='keywords']/@content").getall(),
        item["metaDescription"] = response.xpath(".//meta[@name='description']/@content").getall(),
        item["main_img"] = response.xpath(".//div[@class='piGalMain']/img/@src").getall(),
        item["main_img_width"] = response.xpath(".//div[@class='piGalMain']/img/@width").getall(),
        item["main_img_height"] = response.xpath(".//div[@class='piGalMain']/img/@height").get(),
        item["images"] = response.xpath('//img/@src').getall(),
        item["title"] = response.xpath(".//title/text()").get(),
        item["name"] = response.xpath("//span[@itemprop='name']/text()").getall(),
        item["breadcrumbs"] = response.xpath('//*[@class="breadcrumb"]/descendant::text()').getall()[::2],
        item["url"] = response.xpath('//link[@rel="canonical"]/@href').get(),
        item["link_rel"] = response.xpath('//link[@rel="image_src"]/@href').getall(),
        item["listing_page"] = response.xpath('//a[@id="btn2"]/@href').get(),
        item["price"] = response.xpath('//*[@itemprop="price"]/@content').get(),
        yield item