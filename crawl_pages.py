# -*- coding: utf-8 -*-
"""Downloading all wikihow pages from WikiHow (https://www.wikihow.com/Main-Page)"""

import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import random
import IPython
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

headers_list = [
    # New:
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'},
    # Chrome
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'},
    # Firefox
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'},
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
]

root = "https://www.wikihow.com"


def get_pages(infos):
    """
    Get all related wikihow in each topic.
    """
    topic_url, topic, father_topic, topic_description = infos

    try:
        time.sleep(1.0)
        html = requests.get(topic_url, headers=random.choice(headers_list), timeout=2)
    except:
        return None

    def get_single_page(single_soup):
        try:
            # https://www.wikihow.com/Category:Arts-and-Entertainment
            wikihows = single_soup.find("div", {"id": "cat_container"}) \
                                    .find("div", class_="cat_section", attrs={"id": "cat_all"}) \
                                    .find_all("div", class_="cat_grid")
            # filter out other data-idx
            for wikihow in wikihows:
                if wikihow["class"] == ["cat_grid cat_grid_filter"]:
                    continue
                elif wikihow["class"] == ["cat_grid"]:
                    break

            all_wikihows = wikihow.find_all("div", class_="responsive_thumb")
            wikihow_infos = []
            for per_wikihow in all_wikihows:
                url = per_wikihow.find("a")["href"]
                title = per_wikihow.find("a").find("div", class_="responsive_thumb_title").getText().strip()
                cover_img_url = root + per_wikihow.find("a").find("div", class_="content-spacer").find("img")["data-src-nowebp"]
                is_expert = per_wikihow.find("div", class_="cat_expert")
                is_expert = True if is_expert is not None else False
                wikihow_infos.append([topic_url, topic, url, title, is_expert, cover_img_url])
            return wikihow_infos
        except Exception as e:
            return None

    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "html.parser")

        # get how many pages in per topics
        # e.g.: https://www.wikihow.com/Category:Relationships?pg=2
        try:
            pages_of_wikihow = soup.find("div", {"id": "cat_container"}) \
                                    .find("div", class_="cat_section", attrs={"id": "cat_all"}) \
                                    .find("div", {"id": "large_pagination"}) \
                                    .find("ul", class_="pagination") \
                                    .find_all("li")
            pages_number = max([int(ele.getText()) for ele in pages_of_wikihow])
        except:
            pages_number = 1

        # get full wikihow pages:
        if pages_number == 1:
            wikihow_infos = get_single_page(soup)
            html.close()
        else:
            print("current page number: ", pages_number)
            wikihow_infos = []
            counter = 0
            while len(wikihow_infos) < (pages_number - 1) * 100:
                wikihow_infos = []
                for page_id in range(1, pages_number+1):
                    current_topic_url = topic_url + f"?pg={page_id}"
                    try:
                        time.sleep(2.0)
                        html = requests.get(current_topic_url, headers=random.choice(headers_list), timeout=2)
                    except:
                        continue

                    if html.status_code == 200:
                        soup = BeautifulSoup(html.text, "html.parser")
                        _wikihow_infos = get_single_page(soup)
                        wikihow_infos.extend(_wikihow_infos)
                        html.close()
                    else:
                        continue
                counter += 1
                if counter > 5:
                    break

            if len(wikihow_infos) < (pages_number - 1) * 100:
                IPython.embed()
            
        return wikihow_infos
    else:
        html.close()
        return None
    

if __name__ == "__main__":
    
    
    meta_csv_name = "topics.csv"
    all_topics = list(csv.reader(open(meta_csv_name, 'r')))[1:]

    # single thread
    for topic_info in tqdm(all_topics):
        topic = topic_info[1]
        print(f" !! >> We are on {topic}")
        csv_name = f"pages/pages_{topic}.csv"
        f = open(csv_name, 'w', newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow(["topic url", "topic name", "wikihow url", "wikihow name", "wikihow expert", "wikihow cover url"])
        # write wikihow pages per topic

        wikihow_infos = get_pages(topic_info)
        if wikihow_infos==None:
            print(" We don't get pages for : ", topic)
            continue

        print(f" !! >> We find {len(wikihow_infos)} under {topic}")
        for wikihow_info in wikihow_infos:
            csv_writer.writerow(wikihow_info)

    """
    Late Dedup
    In [2]: import csv
    In [8]: all_topics = list(csv.reader(open('../topics.tsv', 'r')))[1:]
    In [9]: topics = set()
    In [10]: for i in all_topics:
        ...:     topics.add(i[0])
        len(topics) = 3438 
    In [12]: import os
    In [14]: files = os.listdir('./')
    In [18]: counter = 0
    ...: from tqdm import tqdm
    ...: filterout = []
    ...: allurl = set()
    ...: for f in tqdm(files):
    ...:     pages = list(csv.reader(open(f, 'r')))[1:]
    ...:     counter += len(pages)
    ...:     for p in pages:
    ...:         if p[2] in allurl:
    ...:             pass
    ...:         else:
    ...:             allurl.add(p[2])
    ...:             filterout.append(p)
    ...:             pass
    In [19]: counter
    Out[19]: 89342

    In [20]: len(filterout)
    Out[20]: 73370
    """