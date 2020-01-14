from bs4 import BeautifulSoup
import requests
import re

paper_url = "http://openaccess.thecvf.com/ICCV2019.py"
domain = "http://openaccess.thecvf.com/"

review_domain = "https://iem-computer-vision.github.io/ICCV19-Paper-Review/"

paper_data = {} # {'title' : 'pdf link'}

paper_index_start = 13
papers_todo = 10

response = requests.get(paper_url)

soup = BeautifulSoup(response.text, 'html.parser')

titlebox = soup.findAll('dt', attrs={'class': 'ptitle'})
dd_box = soup.findAll('dd')

# firstTitle = titlebox[0].find('a')
# print(firstTitle.contents[0])


# print(domain + dd_box[1].find('a')['href'])

pdfBox_index = 1

for titleboxes in titlebox:
    title = titleboxes.find('a').contents[0]
    title = re.sub(r"[^a-zA-Z0-9]+", '_', title) # Removing special Characters.

    pdf_link = domain + dd_box[pdfBox_index].find('a')['href'] # parse paper link
    
    review_link = review_domain + title # Generate Review Link

    paper_data[title] = (pdf_link, review_link) # Add data to dictionary    
    pdfBox_index += 2


# print(paper_data)

# Generate review paper markdown files and Update Readme

for title, links in list(paper_data.items())[paper_index_start : paper_index_start + papers_todo]:
    review_paper = open(title+'.md', 'w')
    review_paper.close()

    readme_query = f"| {title.replace('_', ' ')} | [PDF Link]({links[0]}) | [Review Link]({links[1]}) |  |"

    with open('README.md', 'a') as readme_file:
        readme_file.write(readme_query+'\n')
