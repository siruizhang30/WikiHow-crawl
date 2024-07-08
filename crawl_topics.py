# -*- coding: utf-8 -*-
"""Downloading all wikihow pages from WikiHow (https://www.wikihow.com/Main-Page)"""

import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import random
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


def get_topics(infos):
    """
    Get related topics.
    """
    url, current_topic_from_prev, father_topic, _ = infos

    try:
        time.sleep(0.5)
        html = requests.get(url, headers=random.choice(headers_list), timeout=2)
    except:
        return None

    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "html.parser")

        # get current topic
        Current_Topic = soup.find("div", class_="cat_section", attrs={"id": "cat_description"}).find("h1").string
        try:
            # https://www.wikihow.com/Category:Arts-and-Entertainment
            Current_Description = soup.find("div", class_="cat_section", attrs={"id": "cat_description"}).find("div", class_="mw-parser-output").find("p").getText().strip()
        except:
            # https://www.wikihow.com/Category:Amusement-and-Theme-Parks
            Current_Description = soup.find("div", class_="cat_section", attrs={"id": "cat_description"}).getText().strip().split('\n')[-1].strip('\n').strip('\t')
        print(" We reach the topic: ", Current_Topic)
        if Current_Topic != current_topic_from_prev:
            print("Warning: we found a misalignment on current topic, " + Current_Topic + " and " + current_topic_from_prev)

        topic_infos = [[url, Current_Topic, father_topic, Current_Description]]  # url; name; father topics; topic description
        father_topic = father_topic + [Current_Topic]

        # get related topics:
        try:
            # import IPython
            # IPython.embed()
            # exit()
            related_topics = soup.find("div", {"id": "cat_container"}).find("div", class_="cat_section", attrs={"id": "cat_sub_categories"}).find_all("div", class_="subcat_container")

            
            for topic in related_topics:
                if topic["class"] == ["subcat_container"]:
                    topic_link = topic.find("a", class_="cat_link")
                    topic_url = root + topic_link["href"]
                    topic_name = topic_link.string
                    topic_infos.append([topic_url, topic_name, father_topic, None])
                elif topic["class"] == ["subcat_container", "with_subsubcats"]:
                    # it have sub related topics: the first one is related and the further one is sub related
                    topic_links = topic.find_all("a", class_="cat_link")
                    topic_urls = [root + topic_link["href"] for topic_link in topic_links]
                    topic_names = [topic_link.string for topic_link in topic_links]
                    
                    topic_infos.append([topic_urls[0], topic_names[0], father_topic, None])  # we only keep the top one, but find it in the next sub
                    # topic_infos.extend(list(zip(topic_urls, topic_names, topic_fathers, topic_descs)))
                else:
                    raise NotImplementedError(" FIND: ", topic)
            has_related = True
        except Exception as e:
            has_related = False
            print(" Exception in related topics: ", e)
        html.close()
        return topic_infos, has_related
    else:
        html.close()
        return None
    

def get_head_topics():
    url = "https://www.wikihow.com/Special:CategoryListing"
    try:
        time.sleep(2.0)
        html = requests.get(url, headers=random.choice(headers_list), timeout=2)
    except:
        return None

    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "html.parser")
        Current_Topic = soup.find("div", class_="content", attrs={"id": "bodyContent"}).find("div", class_="cat_container").find("div", class_="catlist", attrs={"id": "catlist"}).find_all("div")
        topic_infos = []
        for topic in Current_Topic:
            topic_link = topic.find("a")
            topic_url = root + topic_link["href"]
            topic_name = topic_link.string
            topic_infos.append([topic_url, topic_name, ["root"], None])  # father is root
        return topic_infos
    else:
        print(html.text)
        exit()    
    

if __name__ == "__main__":
    
    csv_name = "topics.csv"
    
    f = open(csv_name, 'w', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["topic url", "topic name", "father topics", "topic description"])

    # init topics pool
    current_topics = get_head_topics()
    # we will write it in the following with description
    # for current_topic in current_topics:
    #     csv_writer.writerow(current_topic)

    # single thread
    while len(current_topics) > 0:
        print(f" !! >> We have {len(current_topics)} topics in Pool")
        subcurrent_topics = []
        for info in tqdm(current_topics):
            try:
                fetched_topics, has_related = get_topics(info)
                if fetched_topics is None:
                    print(" We don't get pages for : ", info[1])
                else:
                    # write topics first; we can dedup it
                    print(f" !! >> We find {len(fetched_topics)} under {info[1]}")
                    csv_writer.writerow(fetched_topics[0])

                    if has_related:
                        subcurrent_topics.extend(fetched_topics[1:])
            except:
                print(f" !! >> error for {info[1]}")
        current_topics = subcurrent_topics
