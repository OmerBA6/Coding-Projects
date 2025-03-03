from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com/"
response = requests.get(URL)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles_titles_spans = soup.findAll(name="span", class_="titleline")

articles_names = []
articles_links = []
for span_tag in articles_titles_spans:
    a_tag = span_tag.find("a")
    articles_names.append(a_tag.getText())
    articles_links.append(a_tag.get("href"))

articles_scores = [int(tag.getText().split(" ")[0]) for tag in soup.findAll(name="span", class_="score")]

max_score_index = articles_scores.index(max(articles_scores))

print(f"{articles_names[max_score_index]}\n{articles_links[max_score_index]}\n{articles_scores[max_score_index]}")

# first_article_tag = soup.findall("a", {"rel": "noreferrer"})
# first_article_name = first_article_tag.text
# first_article_link = first_article_tag.get("href")
# print(first_article_link)
