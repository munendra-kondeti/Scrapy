import requests
import json

url = "https://api.mxplayer.in/v1/web/detail/browseItem?&pageNum=1&pageSize=20&isCustomized=true&browseLangFilterIds=te&type=1&device-density=2&userid=1a06465d-298e-4578-a26e-b471aa7b8fbc&platform=com.mxplay.desktop&content-languages=hi,en&kids-mode-enabled=false"
# userid 1a06465d-298e-4578-a26e-b471aa7b8fbc
class Mxplayer_api_data:
    def __init__(self,userid,pag_no=0,per_page=20,search_name=False):
        self.search_name =search_name
        self.per_page = per_page
        self.pag_no = pag_no
        self.userid = userid
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding" : "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.6",
            "Origin":"https://www.mxplayer.in",
            "Referer": "https://www.mxplayer.in/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }
    def set_url(self):
        """ We are setting up the url based on the requirement"""
        if not self.search_name:
            return f"https://api.mxplayer.in/v1/web/detail/browseItem?&pageNum={self.pag_no}&pageSize={self.per_page}&isCustomized=true&browseLangFilterIds=te&type=1&device-density=2&userid={self.userid}&platform=com.mxplay.desktop&content-languages=hi,en&kids-mode-enabled=false"
        elif self.search_name :
            return f"https://api.mxplayer.in/v1/web/search/resultv2?query={self.search_name}&device-density=2&userid={self.userid}&platform=com.mxplay.desktop&content-languages=hi,en&kids-mode-enabled=false"
    def make_request(self):
        """ Here we are making requests to the url"""
        url = self.set_url()
        return requests.request('GET',url,headers=self.headers)
    def get_data(self):
        """ Its make request and convert that data into json """
        self.data = self.make_request().json()

    def get_urls(self,pag_no): 
        """ its take no pages and featch the all the links locations"""
        total_url_data=[]
        for page in range(0,pag_no+1):
            self.make_request()
            self.get_data()
            for item in self.data['items']:
                item_title = item['title']
                item_type = item['type']
                item_url = item['webUrl']
                total_url_data.append({"item_title":item_title,"item_type":item_type,"item_url":item_url})
        return total_url_data


mxplayer_scraper = Mxplayer_api_data("1a06465d-298e-4578-a26e-b471aa7b8fbc")
print(mxplayer_scraper.get_urls(0)[1]["item_url"]) # print what er we whant from the list
