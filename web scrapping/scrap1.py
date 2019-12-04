from bs4 import BeautifulSoup
import csv
import requests
page_no = 1
while(True):
    response = requests.get("https://www.rithmschool.com/blog?page="+str(page_no))
    print(response)
    with open("blogs.csv", "a+") as file:
        csv_writer = csv.writer(file)
        if(page_no == 1):
            headers = ["TITLE","DATE","LINK"]
            csv_writer.writerow(["TITLE","DATE","LINK"])

        soup = BeautifulSoup(response.text,"html.parser")
        if(soup.find(class_ = "lead").get_text() == "No matches found"):
            break 
        
        articles = soup.find_all("article")
        

        for article in articles:
            a_tag = article.find("a")
            title = a_tag.get_text()
            link = "https://www.rithmschool.com"+ a_tag['href']
            date = article.find("time")["datetime"]
            csv_writer.writerow([title,date,link])
    
    page_no += 1











