from bs4 import BeautifulSoup
import requests
import json

def extract_element(dom_tree, selector, attribute=None):
    try:
        if isinstance(attribute, str):
            return dom_tree.select_one(selector)[attribute].strip()
        if isinstance(attribute, list):
            return [e.text.strip() for e in dom_tree.select(selector)]
        return dom_tree.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None

all_reviews = []
service_url = "https://www.ceneo.pl"
next_page = "/39562616#tab=reviews"

while next_page:
    respons = requests.get(service_url + next_page)
    page_dom = BeautifulSoup(respons.text, 'html.parser')
    reviews = page_dom.select("div.js_product-review")
    for review in reviews:
        single_review = {
            "review_id": review["data-entry-id"],
            "author": extract_element(review, "span.user-post__author-name"),
            "recommendation": extract_element(review, "span.user-post__author-recomendation"),
            "stars": extract_element(review, "span.user-post__score-count"),
            "content": extract_element(review, "div.user-post__text"),
            "pros": extract_element(review,"div.review-feature__title--positives ~ div.review-feature__item", []),
            "cons": extract_element(review, "div.review-feature__title--negatives ~ div.review-feature__item", []),
            "useful": extract_element(review, "button.vote-yes"),
            "useless": extract_element(review, "button.vote-no"),
            "purchased": extract_element(review, "div.review-pz"),
            "review_date": extract_element(review, "span.user-post__published > time:nth-child(1)", "datetime"),
            "purchase_date": extract_element(review, "span.user-post__published > time:nth-child(2)", "datetime")
        }
        all_reviews.append(single_review)
    next_page = extract_element(page_dom,"a.pagination__next", "href")

with open("opinions/39562616.json", "w", encoding="UTF-8") as jf:
    json.dump(all_reviews, jf, ensure_ascii=False, indent=4)
