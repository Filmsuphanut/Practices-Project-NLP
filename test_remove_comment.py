from bs4 import BeautifulSoup, Comment

html = """<div class="foo">
A Arara é um animal voador.
<!-- 
<p>Animais
Nome: Arara
Idade: 12 anos e nove meses
Tempo de Vida: 15 anos
-->

</div>"""

soup = BeautifulSoup(html, 'html.parser')

div = soup.find('div', class_='foo')
print(div)
for element in div(text=lambda it: isinstance(it, Comment)):
    element.extract()

print(soup.prettify())