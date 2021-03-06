import scrapy
import re


class GameSpider(scrapy.Spider):
    name = "game"

    def start_requests(self):
        ids = self.game_ids.split(',')

        cookies = {"steamCountry":"IN%7C4e3872bffa3dc3f2cc8046cd1efd8bd9"}
        for id in ids:
            if id:
                url = f'https://store.steampowered.com/app/{id}/'
                yield scrapy.Request(url=url,cookies=cookies, callback=self.parse)

    def parse(self, response):
        for game_item in response.css("div.game_area_purchase_game_wrapper"):
            if game_item:
                yield {
                    'title': game_item.css("h1::text").extract(),
                    'discount': game_item.css("div.discount_final_price::text").extract(),
                    'prices':  game_item.css("div.game_purchase_price::text").extract_first(),
                }
