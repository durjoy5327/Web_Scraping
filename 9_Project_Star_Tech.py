import requests
from bs4 import BeautifulSoup
import pandas as pd
#if ancher tag has no class then you have to think how to get href/link....
#that is on task that how to get obviously you have to find like looping find

product_names = []
prices = []
descriptions = []

for i in range(1, 10):
    #this is for shifting one page to another have a look on ancher tag href then make this
    url = "https://www.startech.com.bd/mobile-phone?filter_price=0-15000&page=" + str(i)
    response = requests.get(url)

    #this is use for handle the Bengali currency symbol correctly
    response.encoding = 'utf-8' 
    soup = BeautifulSoup(response.text, "lxml")

    #this box is make for pulling specific areas data 
    box = soup.find("div", class_="main-content p-items-wrap")

    names = box.find_all("h4", class_="p-item-name")
    
    for n in names:
        product_names.append(n.text)

    price = box.find_all("div", class_="p-item-price")
    for p in price:
        prices.append(p.text.strip())

    description_elements = box.find_all("div", class_="short-description")
    for d in description_elements:
        items = d.find_all("li")
        description = "\n".join(item.text.strip() for item in items)
        descriptions.append(description)


dataframe = pd.DataFrame({
    "Product Names": product_names,
    "Prices": prices,
    "Descriptions": descriptions
})

dataframe.to_csv("F:/Web_Scraping/star_tech_data.csv", index=False)



"""
this is how manually you can shift one page to another
while True:
    # Fetch the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    
    # Find the pagination div
    pagination_div = soup.find("div", class_="col-md-6 col-sm-12")
    
    # Find the anchor tag with the text "NEXT"
    next_page_a = pagination_div.find("a", string="NEXT")
    
    # If the next page link is not found, break the loop
    if not next_page_a:
        break
    
    # Get the href attribute
    next_page_href = next_page_a.get("href")
    
    # Construct the complete URL
    complete_next_page = next_page_href if next_page_href.startswith("http") else "https://www.startech.com.bd" + next_page_href
    print(complete_next_page)
    
    # Update the URL for the next iteration
    url = complete_next_page

"""
