# author="lox_liu"
# first python function to retrieve hitting keyword from "stand news"

# import requests lib for use
# import lxml to analyze html
import requests
from lxml import html
import time

# define url
stand_news_url='https://www.thestandnews.com/'

# define function to grab web info
def grabkeyword(url_link):
    # define text var to get and record html infor// static method
    try:
        pageRes = requests.get(url_link,timeout=10)
        # get html raw text into lxml tree for sort
        tree = html.fromstring(pageRes.text)
        # stand news key words sort here with div class named "tags-module hidden-xs"
        keywords=tree.xpath("//div[@class=\"tags-module hidden-xs\"]//a/text()")
    except Exception as e:
        keywords=[str(e)]
    return keywords

while True:
    for keyword in grabkeyword(stand_news_url):
        print(keyword)
    time.sleep(1)


