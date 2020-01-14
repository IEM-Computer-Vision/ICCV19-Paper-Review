from bs4 import BeautifulSoup
import requests

paper_url = "http://openaccess.thecvf.com/ICCV2019.py"
domain = "http://openaccess.thecvf.com/"

papers_done = 13

response = requests.get(paper_url)

soup = BeautifulSoup(response.text, 'html.parser')

titlebox = soup.findAll('dt', attrs={'class': 'ptitle'})
dd_box = soup.findAll('dd')

# firstTitle = titlebox[0].find('a')
# print(firstTitle.contents[0])


# print(domain + dd_box[1].find('a')['href'])

for titleboxes in titlebox:
    titleboxes.find('a')