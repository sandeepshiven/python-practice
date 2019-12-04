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
print(type(soup)) # this contains all objects of diffrent tags
print(soup,'\n\n\n') # seems like string but it is object of <class 'bs4.BeautifulSoup'>
print(soup.div,'\n\n\n') # <class 'bs4.element.Tag'>
print(type(soup.div),'\n\n\n')
print(soup.find('div'),'\n\n\n') # return first div element
print(soup.find_all('div'),'\n\n\n') # returns list of all div elements
print(soup.find_all('li'),'\n\n\n')
print(soup.find(id='first'),'\n\n\n')
print(soup.find_all(class_='special'),'\n\n\n')
print(soup.find(attrs={"data-example":"yes"}),'\n\n\n')

