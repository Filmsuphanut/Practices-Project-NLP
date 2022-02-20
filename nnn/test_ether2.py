from bs4 import BeautifulSoup, Comment
import requests
import regex as re
from urllib.request import Request, urlopen

pantip = "https://pantip.com/topic/41259649"
#test = "https://www.reddit.com/r/Genshin_Impact/comments/ssi32y/would_you_support_a_genshin_anime/"
#pantip = "https://pantip.com/topic/41075810"
#test = ' https://sirichaiwatt.com/%e0%b8%9a%e0%b8%97%e0%b8%84%e0%b8%a7%e0%b8%b2%e0%b8%a1%e0%b8%94%e0%b8%b5%e0%b9%86/%e0%b8%81%e0%b8%b2%e0%b8%a3%e0%b8%9e%e0%b8%b1%e0%b8%92%e0%b8%99%e0%b8%b2%e0%b8%95%e0%b8%99%e0%b9%80%e0%b8%ad%e0%b8%87/%e0%b8%81%e0%b8%b2%e0%b8%a3%e0%b9%80%e0%b8%9b%e0%b8%a5%e0%b8%b5%e0%b9%88%e0%b8%a2%e0%b8%99%e0%b9%81%e0%b8%9b%e0%b8%a5%e0%b8%87%e0%b8%95%e0%b8%b1%e0%b8%a7%e0%b9%80%e0%b8%ad%e0%b8%87/%e0%b8%ab%e0%b8%99%e0%b8%b6%e0%b9%88%e0%b8%87%e0%b8%a7%e0%b8%b4%e0%b8%98%e0%b8%b5%e0%b8%ab%e0%b8%99%e0%b8%b5%e0%b8%84%e0%b8%a7%e0%b8%b2%e0%b8%a1%e0%b8%a5%e0%b9%89%e0%b8%a1%e0%b9%80%e0%b8%ab%e0%b8%a5 '
url = 'https://etherscan.io/block/14211005'
req = Request(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})   # I got this line from another post since "uClient = uReq(URL)" and "page_html = uClient.read()" would not work (I beleive that etherscan is attemption to block webscraping or something?)
response = urlopen(req, timeout=20).read()
response_close = urlopen(req, timeout=20).close()
soup = BeautifulSoup(response, "html.parser")

for element in soup(text=lambda text: isinstance(text, Comment)): ##remove comment tag
    element.extract()

text = soup.find_all(text=True)

regexp = re.compile(r'\s|\t|\n|\x7C', re.UNICODE)

valid_tag = ['div','h','h1','h2','h3','h4','h5','p','p1','p2','p3','p4','p5']

output = ""
for t in text:
    if t.parent.name in valid_tag :
        #if regexp.sub('', t) != '':
        output += '{}'.format(regexp.sub('', t))
print(output)

# ### write text file


f = open('text1.txt', 'w')
with open('text1.txt', 'w',encoding='utf-8') as f:
    f.write(output)




# blacklist = [
#     '[document]',
#     'noscript',
#     'header',
#     'html',
#     'meta',
#     'head', 
#     'input',
#     'script',
#     'style',
#     'li',
#     'a',
#     'span',
#     'option',
#     'button',
#     'em',
#     'iframe',
#     'select'
#     # there may be more elements you don't want, such as "style", etc.
# ]