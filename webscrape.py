from requests import get
from bs4 import BeautifulSoup as Soup
import random

# Get url

url = get("https://www.imdb.com/chart/top/")
request = url.text
soup_data = Soup(request, "html.parser")

# Dict where data will be stored

movies_dict = {}

# Get movie title & ratings & link

scraped_movies = soup_data.findAll("td", class_="titleColumn")
scraped_ratings = soup_data.findAll("td", class_="ratingColumn imdbRating")

# Clean the data & add it to the dict

for rating, movie in zip(scraped_ratings, scraped_movies):
    movie = movie.get_text().replace("\n", "")
    movie = movie[10:-6].strip(" ")

    rating = rating.get_text().replace("\n", "")
    rating = rating.strip(" ")

    movies_dict[movie] = rating

print(random.choice(list(movies_dict.items())))
