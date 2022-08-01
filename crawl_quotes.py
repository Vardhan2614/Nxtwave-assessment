from django.test import tag
import requests
import json
from bs4 import BeautifulSoup
import Converting_to_json
import store_quotes

urlrequest = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(urlrequest.content,"html.parser")
quotesdata = soup.find_all("div",{"class":"quote"})

for data in quotesdata:
    description = data.find("span",{"class":"text"}).get_text()
    author = data.find("small",{"class":"author"}).get_text()
    tags = data.find_all("div",{"class":"tags"})
    author_data = data.find_all("span",{"class":""})
    for information in author_data:
        finding_url = information.a["href"]
        author_details_url = "http://quotes.toscrape.com{}".format(finding_url)
        author_url_request = requests.get(author_details_url)
        authors_html_soup = BeautifulSoup(author_url_request.content,"html.parser")
        author_name = authors_html_soup.find_all("div",{"class":"author-details"})
        for info in author_name:
            author_info = info.find("h3",{"class":"author-title"}).get_text()
            print(author_info[])
    tags_list = []
    for tag in tags:
        individual_tag = tag.find_all('a',{"class":"tag"})
    for data in individual_tag:
        tag_text = data.get_text()
        tags_list.append(tag_text)
    jsondata = Converting_to_json.convert_to_json(description,author,tags_list)

original_json_file = jsondata



