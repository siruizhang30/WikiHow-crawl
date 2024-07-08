import trafilatura
from bs4 import BeautifulSoup 
import json
import requests
import csv
from tqdm import tqdm

meta_csv_name = "chinese_topics.csv"
all_pages = list(csv.reader(open(meta_csv_name, 'r')))[1:]

# all_pages = all_pages[:10]

json_data = []
for page in tqdm(all_pages):
    english_url = page[2]
    try:
        html_content_en = trafilatura.fetch_url(english_url)
        soup_en = BeautifulSoup(html_content_en, "html.parser")
        other_languages = soup_en.find("div", attrs={"id": "other_languages"}).find_all("div", attrs={"class": "language_link"})
        for language in other_languages:
            # print(language.find('span').text)
            if language.find('span').text == "中文:":
                chinese_url = language.find("a").get("href")
                # print(chinese_url)
                break

        html_content_ch = trafilatura.fetch_url(chinese_url)
        soup_ch = BeautifulSoup(html_content_ch, "html.parser")

        application_ld_json_en = soup_en.find_all("script", attrs={"type": "application/ld+json"})
        application_ld_json_ch = soup_ch.find_all("script", attrs={"type": "application/ld+json"})

        paried_dict = {
            "topic_url": page[0],
            "topic_name": page[1],
            "wikihow_expert": page[4],
            "english_url": english_url,
            "chinese_url": chinese_url,
            "wikihow_title_en": soup_en.find_all("title")[0].text,
            "wikihow_title_ch": soup_ch.find_all("title")[0].text,
            "english_method_total": [],
            "chinese_method_total": [],
            "english": [], 
            "chinese": []
        }
        for num, ld_json in enumerate(application_ld_json_en):
            json_ld_data_en = json.loads(ld_json.string)  
            if 'step' in json_ld_data_en:
                steps_en = json_ld_data_en.get("step")
                if steps_en[0].get("itemListElement") is None:
                    steps_en = [steps_en]
                for method, step in enumerate(steps_en):  
                    # FIXME: 有些步驟没有itemListElement
                    try:
                        items = step.get("itemListElement")
                        name = step.get("name")
                    except:
                        items = step
                        name = "None" 
                        
                    paried_dict["english_method_total"].append(len(items))
                    item_dict = {
                        "method_num": method, 
                        "name": name, 
                        "text_num": len(items), 
                        "item": [] 
                    }
                    for text_num, text in enumerate(items):
                        # print(item.get("text"))
                        item_dict["item"].append({
                            "text_num":text_num, 
                            "text":text.get("text"), 
                            "image":text.get("image")
                        })
                    paried_dict["english"].append(item_dict)

        for num, ld_json in enumerate(application_ld_json_ch):
            json_ld_data_ch = json.loads(ld_json.string)  
            if 'step' in json_ld_data_ch:
                steps_ch = json_ld_data_ch.get("step")
                if steps_ch[0].get("itemListElement") is None:
                    steps_ch = [steps_ch]
                for method, step in enumerate(steps_ch):
                    try:
                        items = step.get("itemListElement")
                        name = step.get("name")
                    except:
                        items = step
                        name = "None" 
                        
                    paried_dict["chinese_method_total"].append(len(items))
                    item_dict = {
                        "method_num": method, 
                        "name": name, 
                        "text_num": len(items), 
                        "item": [] 
                    }
                    for text_num, text in enumerate(items):
                        # print(item.get("text"))
                        item_dict["item"].append({
                            "text_num":text_num, 
                            "text":text.get("text"), 
                            "image":text.get("image")
                        })
                    paried_dict["chinese"].append(item_dict)
        
        json_data.append(paried_dict)

    except Exception as e:
        print(e)
        print("Error: ", english_url)
        print("Error: ", chinese_url)

with open('/workspace/data_example.json', 'w') as outfile:
    json.dump(json_data, outfile, indent=4, ensure_ascii=False)