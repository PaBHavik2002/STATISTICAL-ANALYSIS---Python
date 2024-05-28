import requests
from bs4 import BeautifulSoup
import pandas as pd

# Link to fetch the data
flipkart_url = 'https://www.flipkart.com/search?q=Laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

# Response to get from amazon_url
response = requests.get(flipkart_url)


# Checking the connectivity
if response.status_code == 200: 
    soup = BeautifulSoup(response.text, 'lxml')    
    count = 1
    div_class = soup.find_all(class_='CGtC98')
    
    # An Empty List
    product_name = []
    
    for child_class in div_class:
        _class = child_class.find(class_='KzDlHZ')


        # Splitting the text
        if _class.text.find('-'):
            splitted_text = _class.text.split('-')
            
            # Further bifergation
            

    frame = pd.DataFrame(
        {
            'Product Name': product_name
        }
    )
    # For More Courses
    more_courses = soup.find()
    
else:
    print('Not Working Properly')