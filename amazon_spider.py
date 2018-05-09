import scrapy
import search_url


class AmazonSpider(scrapy.Spider):
    """docstring for AmazonSpider"""
    name = "products"
    start_urls = []

    start_urls.append(search_url.get_search_url(raw_input("Enter the keyword\n")))

    def parse(self, response):
        for product in response.css("ul.s-result-list"):
            yield {
                'product': product.css('a.a-link-normal::attr("title")').extract(),
                'price': product.css('span.a-color-price::text').extract(),
                # 'price': product.xpath('span/small/text()').extract_first(),
            }
        next_page = response.xpath('//*[@id="pagn"]/span[7]').css('a.pagnNext::attr("href")').extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)



