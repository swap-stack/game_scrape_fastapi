import scrapy
import re


class GameSpider(scrapy.Spider):
    name = "game"

    def start_requests(self):
        ids = self.game_ids.split(',')

        for id in ids:
            url = f'https://store.steampowered.com/app/{id}/'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for game_item in response.css("div.game_area_purchase_game_wrapper"):
            yield {
                'title': game_item.css("h1::text").extract(),
                'prices': re.findall(r'\d+', game_item.css("div.game_purchase_price::text").extract_first().replace(',', ''))[0],
            }
