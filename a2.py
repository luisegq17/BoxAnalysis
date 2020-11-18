import scrapy
from scrapy.utils.response import open_in_browser
from a1 import url_list

# run "scrapy runspider a2.py -o hist_data_k.json" on cmd while on this folder

class BoxSpider(scrapy.Spider):

    name = 'boxspider'
    download_delay = 0.25
    login_url="https://boxrec.com/en/login"
    start_urls=url_list
    """start_urls=[
        "https://boxrec.com/en/date?date=2011-01-07&sport=proboxing",
    ]"""

    def parse(self, response):

        data={
            "_target_path":"",
            "_username":"luisegq17",
            "_password":"Fri10Fer05Lk32",
            "login[go]":""
        }

        yield scrapy.FormRequest(
            url=self.login_url,
            formdata=data,
            callback=self.parse1
        )

    def parse1(self, response):

        for page in self.start_urls:
            yield scrapy.Request(
                url=page,
                callback=self.parse2
            )

    def parse2(self, response):

        for q in response.css('tbody'):
            ############### result ##############
            res=q.xpath('tr/td[7]/div/text()').get()
            if(res=="W"):
                res=1
            elif(res=="L"):
                res=0
            ############### category ##############
            categ=q.xpath('tr/td[2]/text()').get()
            try:
                categ=categ[1:]
            except:
                categ="NS"
            else:
                categ=categ[1:]
                categ=categ.replace("\n","")
            ############### weight winner/looser ##############
            wfw=q.xpath('tr/td[4]/text()').get()
            lfw=q.xpath('tr/td[11]/text()').get()
            try:
                wfw=wfw[:3]
                lfw=lfw[:3]
            except:
                wfw="NS"
                lfw="NS"
            else:
                if(wfw=="\n"):
                    wfw="NS"
                else:
                    wfw=wfw[:3]
                    wfw=int(wfw)
                if(lfw=="\n"):
                    lfw="NS"
                else:
                    lfw=lfw[:3]
                    lfw=int(lfw)
            ################# Other vars ####################
            if(categ=="heavy" and wfw!="NS" and lfw!="NS"):
                if(res==1 or res==0):
                    dw=wfw-lfw
                    dw_w=dw/wfw
                    dw_l=dw/lfw
            ################ parse yield #####################
            if(categ=="heavy" and wfw!="NS" and lfw!="NS"):
                if(res==1 or res==0):
                    yield {
                        "res":res,
                        "wfw":wfw,
                        "lfw":lfw,
                        "dw":dw,
                        "dw_w":dw_w,
                        "dw_l":dw_l
                    }