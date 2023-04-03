# from turtle import ht
from bs4 import BeautifulSoup
import requests

# to install VeaytufulSoup if it's not in the pipfile: "pipenv install bs4"

# If you get a 403 Forbidden error, the website may be trying to prevent bots. You may need to define headers with user-agent.
headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)
# html = requests.get("https://google.com/")

doc = BeautifulSoup(html.text, 'html.parser')

print(doc.select('.heading-primary')[0].contents)
print(doc.select('.heading-35-semibold.color-teal.mb-20'))

# courses = doc.select('.slick-slide.slick-active')

# for course in courses: 
#   print(course[0].contents)

name = doc.select('.heading-60-black.color-black.mb-20')[0].name

doc.select('.heading-60-black.color-black.mb-20')[0].attrs