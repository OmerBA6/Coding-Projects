from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")

movie_titles = soup.findAll(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

with open("Top 100 Movies.txt", "w") as file:
    for movie in movie_titles[::-1]:
        file.write(f"{movie.getText()}\n")

