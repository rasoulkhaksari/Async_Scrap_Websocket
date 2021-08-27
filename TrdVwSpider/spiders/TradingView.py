import scrapy


class TradingViewSpider(scrapy.Spider):
    name = 'tradingviewspider'
    start_urls=['https://www.tradingview.com/markets/cryptocurrencies/prices-all/']


    def parse(self, response):
        for tr in response.css("#js-screener-container table tbody tr"):
            yield {
                'Title': tr.css("td:nth-child(1) a::text").get().strip(),
                'Mkt_Cap': tr.css("td:nth-child(2)::text").get(),
                'FD_Mkt_Cap': tr.css("td:nth-child(3)::text").get(),
                'LAST': tr.css("td:nth-child(4)::text").get(),
                'Avail_Coins': tr.css("td:nth-child(5)::text").get(),
                'Total_Coins': tr.css("td:nth-child(6)::text").get(),
                'Traded_Vol': tr.css("td:nth-child(7)::text").get(),
                'Chg': tr.css("td:nth-child(8)::text").get(),
            }

