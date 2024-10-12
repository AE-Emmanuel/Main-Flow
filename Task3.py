import requests
from bs4 import BeautifulSoup

#url of the website which we want to scrape
url="https://beebom.com/google-pixel-9-pro-fold-review/"

#send GET request to the webpage
response=requests.get(url)

#checking if the request is succeeded or not 
if response.status_code == 200:
    
    soup=BeautifulSoup(response.text,'html.parser') #parsethe html content of the page
    
    page_text=soup.get_text() #getting all the text from the page 
    
    links = [a['href']for a in soup.find_all('a',href=True)] #extract all link s
    
    images = [img['src']for img in soup.find_all('img',src=True)] #extract all image 
    
    print('Texts From Webpage:\n')
    print(page_text)
    
    print('\nlinks From Webpage:\n')
    
    for link in links:
        print(link)
    print('\nImages From Webpage:\n')
    for i in images:
        print(i)        
else:
    print (f"Failed to Retrieve data Status Code:",{response.status_code})