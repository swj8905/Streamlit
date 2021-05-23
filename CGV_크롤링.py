import urllib.request as req
from bs4 import BeautifulSoup


code = req.urlopen("http://www.cgv.co.kr/movies/")

soup = BeautifulSoup(code, "html.parser")

title = soup.select("div.sect-movie-chart strong.title")
img = soup.select("div.sect-movie-chart span.thumb-image > img")