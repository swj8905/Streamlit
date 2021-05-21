import streamlit as st

import urllib.request as req
from bs4 import BeautifulSoup


code = req.urlopen("http://www.cgv.co.kr/movies/")

soup = BeautifulSoup(code, "html.parser")

title = soup.select("div.sect-movie-chart strong.title")
img = soup.select("div.sect-movie-chart span.thumb-image > img")

"# 무비차트"
for i in range(len(title)):
    # st.write(i.string)
    # st.markdown(f"# **{i+1}위.** {title[i].string}")
    # st.markdown(f"![] ({img[i].attrs['src']})")
    f"# **{i+1}위.** {title[i].string}"
    st.image(img[i].attrs["src"], width=200)
