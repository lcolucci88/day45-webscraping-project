import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response= requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movies= [tag.get_text().replace(":",")").split(") ")[1] for tag in soup.find_all(name="h3", class_="title")]
i=-1
n=1
with open("movies.txt", "w", encoding= "utf-8") as file:
    for movie in movies:
        file.write(f"{n}) {movies[i]}\n")
        i-= 1
        n +=1

