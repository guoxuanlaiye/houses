import scrapy
from ..items import AnjukeItem
from ..sql import sql

class Anjuke(scrapy.Spider):

    name = "anjuke"
    allowed_domains = ["shen.fang.anjuke.com"]
    start_urls = ["https://shen.fang.anjuke.com/loupan/all/p1/"]

    # 初始化数据库
    sql.initDB()

    def parse(self, response):
        house_resource = response.xpath('//div[@class="key-list"]/div')
        # print(house_resource)
        for house in house_resource:
            houses_name = house.xpath('div[@class="infos"]/a[@class="lp-name"]/h3/span/text()').extract_first()
            houses_adress = house.xpath('div[@class="infos"]/a[@class="address"]/span/text()').extract_first()
            average_price = house.xpath('a[@class="favor-pos"]/p[@class="price"]/span/text()').extract_first()
            price_status = house.xpath('a[@class="favor-pos"]/p[@class="price"]/text()').extract_first()
            if not price_status:
                price_status = ""
            # print(price_status)
            # 户型 huxing  只有一个span标签时，显示的是建筑面积，>1时显示 户型+建筑面积
            # 建筑面积：600000㎡
            houses_type = ""
            houses_area = ""
            houses_types = house.xpath('div[@class="infos"]/a[@class="huxing"]/span/text()').extract()
            if len(houses_types) == 0:
                pass
            elif len(houses_types) == 1:
                houses_area = houses_types[0]

            else:
                houses_area = houses_types[-1]
                del houses_types[-1]
                houses_type = ",".join(houses_types)

            tags_list1 = house.xpath('div[@class="infos"]/a[@class="tags-wrap"]/div[@class="tag-panel"]/i/text()').extract()
            tags_list2 = house.xpath('div[@class="infos"]/a[@class="tags-wrap"]/div[@class="tag-panel"]/span/text()').extract()
            tags_list = tags_list1 + tags_list2

            around_ava_price = ""
            if not average_price:
                average_price = house.xpath('a[@class="favor-pos"]/p[@class="price-txt"]/text()').extract_first()
                around_ava_price = house.xpath('a[@class="favor-pos"]/p[@class="favor-tag around-price"]/span/text()').extract_first()
            if not average_price or not average_price.isdigit():
                average_price = "0"
            if not around_ava_price or not around_ava_price.isdigit():
                around_ava_price = "0"

            item = AnjukeItem()
            item["houses_name"] = houses_name
            item["houses_adress"] = houses_adress.replace("\xa0", " ")
            item["average_price"] = int(average_price)
            item["around_ava_price"] = int(around_ava_price)
            item["tags"] = ",".join(tags_list)
            item["price_status"] = price_status
            item["houses_type"] = houses_type
            item["houses_area"] = houses_area.replace("建筑面积：", "")
            yield item

        next_page_url = response.xpath('//div[@class="pagination"]/*[last()]/@href').extract_first()
        print("----------------url = %s" % next_page_url)
        if next_page_url:
            yield scrapy.Request(next_page_url)

