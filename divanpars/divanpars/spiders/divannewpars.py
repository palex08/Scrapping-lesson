import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/vladivostok/category/svet"]

    def parse(self, response):
        lights = response.css("div.LlPhw")
        for light in lights:
            yield {
                "name": light.css("div.lsooF span::text").get(),
                "price": light.css("div.q5Uds span::text").get(),
                "url": light.css("a::attr(href)").get(),
            }
