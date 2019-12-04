from bs4 import BeautifulSoup

html = '''<!DOCTYPE html>
<html>
    <head>
        <title>HELLO</title>
    </head>
    <body>
    <h1 data-example="yes">HI!!!</h1> 
	<div id="first">
        <ol>
            <li class="special">Banana</li>
            <li class="special">Apple</li>
            <ol>
                <li>One</li>
                <li>Two</li>
            </ol>
            <li>Orange</li>
        </ol>
	</div>
	<div>
        <ul>
                <li>Banana</li>
                <li class="special">Apple</li>
                <ul>
                    <li class="special">One</li>
                    <li>Two</li>
                </ul>
                <li>Orange</li>
            </ul>
	</div>
    </body>
</html>'''

soup = BeautifulSoup(html ,"html.parser")
el = soup.select(".special")[0]
print(el.get_text())
print(el.name)
print(el.attrs)


