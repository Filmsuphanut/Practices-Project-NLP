from bs4 import BeautifulSoup, Comment
import requests
import regex as re

pantip = "https://pantip.com/topic/41259649"
pantip = "https://pantip.com/topic/41075810"
test = ' https://sirichaiwatt.com/%e0%b8%9a%e0%b8%97%e0%b8%84%e0%b8%a7%e0%b8%b2%e0%b8%a1%e0%b8%94%e0%b8%b5%e0%b9%86/%e0%b8%81%e0%b8%b2%e0%b8%a3%e0%b8%9e%e0%b8%b1%e0%b8%92%e0%b8%99%e0%b8%b2%e0%b8%95%e0%b8%99%e0%b9%80%e0%b8%ad%e0%b8%87/%e0%b8%81%e0%b8%b2%e0%b8%a3%e0%b9%80%e0%b8%9b%e0%b8%a5%e0%b8%b5%e0%b9%88%e0%b8%a2%e0%b8%99%e0%b9%81%e0%b8%9b%e0%b8%a5%e0%b8%87%e0%b8%95%e0%b8%b1%e0%b8%a7%e0%b9%80%e0%b8%ad%e0%b8%87/%e0%b8%ab%e0%b8%99%e0%b8%b6%e0%b9%88%e0%b8%87%e0%b8%a7%e0%b8%b4%e0%b8%98%e0%b8%b5%e0%b8%ab%e0%b8%99%e0%b8%b5%e0%b8%84%e0%b8%a7%e0%b8%b2%e0%b8%a1%e0%b8%a5%e0%b9%89%e0%b8%a1%e0%b9%80%e0%b8%ab%e0%b8%a5 '
url = requests.get(pantip)
url.encoding = "utf-8"
soup = BeautifulSoup(url.text, "html.parser")

for element in soup(text=lambda text: isinstance(text, Comment)):
    element.extract()
text = soup.find_all(text=True)

blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style',
    'li',
    'a',
    'span',
    'option',
    'button',
    'em',
    # there may be more elements you don't want, such as "style", etc.
]


output = ""
for t in text:
    if t not in '\n' and t not in '\t' and t not in '\n' and t.parent.name not in blacklist:
        output += '{} '.format(t)

### write text file

# f = open('text1.txt', 'w')
# with open('text1.txt', 'w',encoding='utf-8') as f:
#     f.write(output)

# print(output)