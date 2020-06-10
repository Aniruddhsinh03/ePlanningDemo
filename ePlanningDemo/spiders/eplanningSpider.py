# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, FormRequest


class EplanningspiderSpider(scrapy.Spider):
    name = 'eplanningSpider'
    allowed_domains = ['eplanning.ie']
    start_urls = ['http://eplanning.ie/']

    def parse(self, response):
        # extract country urls from main page
        country_list = response.xpath('//a/@href').extract()
        # extract one by one url
        for country in country_list:
            if '#' == country:
                pass
            else:
                yield Request(country, callback=self.call_country_url)

    def call_country_url(self, response):
        # select receiver application url
        application_list_url = response.xpath(
            '//*[@class="glyphicon glyphicon-inbox btn-lg"]/following-sibling::a/@href').extract_first()
        yield Request(response.urljoin(application_list_url), callback=self.parse_search_listing_form)

    def parse_search_listing_form(self, response):
        # submitting form request with parameters
        yield FormRequest.from_response(response,
                                        formdata={'RdoTimeLimit': '42'},
                                        dont_filter=True,
                                        formxpath='(//form)[2]',
                                        callback=self.parse_search_results)

    def parse_search_results(self, response):
        # extract file numbers urls
        application_urls = response.xpath('//td/a/@href').extract()
        # visit all urls one by one
        for url in application_urls:
            url = response.urljoin(url)
            yield Request(url, callback=self.parse_application_details)
        # extracting next page url
        next_page_url = response.xpath('//*[@rel="next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url, callback=self.parse_search_results)

    def parse_application_details(self, response):
        # extract user agent data from table
        agent_btn = response.xpath('//*[@value="Agents"]/@style').extract_first()
        if 'display: inline;  visibility: visible;' in agent_btn:
            name = response.xpath('//tr[th="Name :"]/td/text()').extract_first()
            address_first = response.xpath('//tr[th="Address :"]/td/text()').extract()
            address_second = response.xpath('//tr[th="Address :"]/following-sibling::tr/td/text()').extract()[0:3]
            address = address_first + address_second
            phone = response.xpath('//tr[th="Phone :"]/td/text()').extract_first()
            fax = response.xpath('//tr[th="Fax :"]/td/text()').extract_first()
            email = response.xpath('//tr[th="e-mail :"]/td/a/text()').extract_first()
            url = response.url

            yield {'name': name,
                   'address': address,
                   'phone': phone,
                   'fax': fax,
                   'email': email,
                   'url': url}
        else:
            self.logger.info('Agent button not found on page, passing invalid url.')
