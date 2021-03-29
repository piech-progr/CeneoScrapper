import requests
from bs4 import BeautifulSoup

respons = requests.get("https://www.ceneo.pl/70068802#tab=reviews")


page_dom = BeautifulSoup(respons.text, "html.parser")

opinion = page_dom.select("div.js_product-review").pop(0)

opinion_id = opinion["data-entry-id"]
author = opinion.select("span.user-post__author-name").pop(0).get_text().strip()
try:
    recomedation = opinion.select("span.user-post__author-recomendation > em").pop(0).get_text().strip()
    recomedation = True if recomedation=="Polecam" else False
except IndexError:
    recomendation = None
stars = opinion.select("span.user-post__score-count").pop(0).get_text().strip()
stars = float(stars.split("/")[0].replace(",","."))
content = opinion.select("div.user-post__text").pop(0).get_text().strip()
try:
    pros = opinion.select("div.review-feature_col:has(>div[class*=\"possitives\"])>div.review-feature_item")
    pros = [x.get_text().strip() for x in pros]
except IndexError:
    pros = None
try:
    cons = opinion.select("div.review-feature_col:has(>div[class*=\"negatives\"])>div.review-feature_item")
    [x.get_text().strip() for x in cons]
except IndexError:
    cons = None
try:
    purchased = bool(opinion.select("div.review-pz").pop(0).get_text().strip())
except IndexError:
    purchased = None
submit_date = opinion.select("span.user-post__published > time:nth-child(1)").pop(0)["datetime"].strip()
try:
    purchase_date = opinion.select("span.user-post__published > time:nth-child(2)").pop(0)["datetime"].strip()
except IndexError:
    purchase_date = None
useful = int(opinion.select("span[id^='votes-yes']").pop(0).get_text().strip())
useless = int(opinion.select("span[id^='votes-no']").pop(0).get_text().strip())

print( author, recomedation, stars, content, pros, cons, purchased, submit_date, purchase_date, useful, useless, sep="\n")
print(type(opinion))