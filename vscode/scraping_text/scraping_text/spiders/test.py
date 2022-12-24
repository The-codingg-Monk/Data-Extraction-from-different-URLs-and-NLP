import scrapy
import pandas as pd
import os
import shutil
import sys
sys.path.append('./')
from scraping_text.items import ScrapingTextItem

os.remove(r"C:\Users\kannu\OneDrive\Desktop\DataScience\Projects\Blackcoffer\20211030 Test Assignment\vscode\scraping_text\scraping_text\Extracted_data.csv")
df=pd.read_excel(r"C:\Users\kannu\OneDrive\Desktop\DataScience\Projects\Blackcoffer\20211030 Test Assignment\input.xlsx")


class scraper(scrapy.Spider):
    name='quotes'
    for url in df['URL'].values:
        start_urls=df['URL'].to_list()

    def parse(self,response):
        items=ScrapingTextItem()
        title=" ".join(response.css('.entry-title::text').extract())
        text=" ".join(response.css('p::text').extract())
        items['title']=title
        items['text']=text

        url_no=df[df['URL']==response._get_url()]["URL_ID"].values[0]
        items['url_id']=url_no
        
        yield items