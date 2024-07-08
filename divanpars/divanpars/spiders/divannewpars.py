import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/vladivostok/category/svet"]
    items = []

    def parse(self, response):
        lights = response.css("div.LlPhw")
        for light in lights:
            name = light.css("div.lsooF span::text").get()
            price = light.css("div.q5Uds span::text").get()
            url = response.urljoin(light.css("a::attr(href)").get())
            if name and price and url:
                item = {
                    "Название": name,
                    "Цена": price,
                    "Ссылка": url,
                }
                self.items.append(item)
                yield item

    def close(self, reason):
        with open('lights.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Название', 'Цена', 'Ссылка']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in self.items:
                writer.writerow(item)

