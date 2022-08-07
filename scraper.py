import requests
from bs4 import BeautifulSoup

url = "https://www.backmarket.fr/fr-fr/r/l/smartphones/6c290010-c0c2-47a4-b68a-ac2ec2b64dca"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.select('a[class="page-link next-page"]')
query = soup.find_all("div", {"data-test" : "reviews-display-reviewList-review"})
print(query.children)