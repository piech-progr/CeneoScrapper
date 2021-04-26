import requests
from bs4 import BeautifulSoup
import json

def extract_element(opinion,selector,atribute=None):
    try:
        if atribute:
            if isinstance(atribute,str):
                return  opinion.select(selector).pop(0)[atribute].strip()
            else:
                return [x.get_text().strip() for x in opinion.select(selector)]
        else:
            return opinion.select(selector).pop(0).get_text().strip()
    except IndexError:
            return None



selectors = {
    "author": ["span.user-post__author-name"],
    "recomedation": ["span.user-post__author-recomendation > em"],
    "stars": ["span.user-post__score-count"],
    "content": ["div.user-post__text"],
    "pros": ["div.review-feature__col:has(> div[class*=\"positives\"]) > div.review-feature__item",1],
    "cons": ["div.review-feature__col:has(> div[class*=\"negatives\"]) > div.review-feature__item",1],
    "purchased": ["div.review-pz"],
    "submit_date": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchase_date": ["span.user-post__published > time:nth-child(2)", "datetime"],
    "useful": ["span[id^='votes-yes']"],
    "useless": ["span[id^='votes-no']"]
}




extracted_opinions= []

product_id=input("Podaj kod produktu: ")
next_page="https://www.ceneo.pl/{}#tab=reviews".format(product_id)

while next_page:

    respons = requests.get(next_page)


    page_dom = BeautifulSoup(respons.text, "html.parser")


    # opinion=opinions.pop(0)

    opinions = page_dom.select("div.js_product-review")
    # opinions = page_dom.select("div.js_product-review").pop(0)

    for opinion in opinions:

        opinion_elements={key:extract_element(opinion,*args)
                            for key, args in selectors.items()}

        opinion_elements["opinion_id"]= opinion["data-entry-id"]
        


        opinion_elements["recomedation"] = True if  opinion_elements["recomedation"]=="Polecam" else False if  opinion_elements["recomedation"]=="Nie Polecam" else None
        opinion_elements["stars"] = float(opinion_elements["stars"].split("/")[0].replace(",", "."))
        opinion_elements["purchased"] = bool(opinion_elements["purchased"])
        opinion_elements["useful"] = int(opinion_elements["useful"])
        opinion_elements["useless"] = int(opinion_elements["useless"])


        extracted_opinions.append(opinion_elements)
    try:
        next_page= "https://www.ceneo.pl" + \
        page_dom.select("a.pagination_next").pop()["href"]
    except IndexError:
        next_page=None

        # print(extracted_opinions)
    print(next_page)

with open(f"./opinions/{product_id}.json","w",encoding="UTF-8") as fp:
    json.dump(extracted_opinions, fp,indent=4, ensure_ascii=False)

 