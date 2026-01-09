# the other one has a limit to the number of request i can make. at some point if a recruiter runs it it will not work + it is not getting the price or the title of the page.

from bs4 import BeautifulSoup
import requests
# get the information off the website
# Fetch page
url = "https://www.amazon.co.uk/Dreo-Electric-Efficient-Thermostat-Protection/dp/B0C9D4KL9D/?_encoding=UTF8&pd_rd_w=iuqDJ&content-id=amzn1.sym.6b52c2a5-fada-4e73-a099-82fe56c2e0de&pf_rd_p=6b52c2a5-fada-4e73-a099-82fe56c2e0de&pf_rd_r=4CTKMZNRX9WF6ZTTB5V3&pd_rd_wg=HpRFF&pd_rd_r=d6020ec1-84d2-42e0-acc7-776272225e82&th=1"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
name = soup.find(id='productTitle')
big_integer_price = soup.find(class_="a-price-whole")
decimal_price = soup.find(class_="a-price-fraction")
if name:
    name = name.get_text().strip()
    #rint(name)
else:
    print("Title not found")

if big_integer_price and decimal_price:
    price = big_integer_price.get_text().strip()+ decimal_price.get_text().strip()
    print(big_integer_price.get_text().strip()+ decimal_price.get_text().strip())

from datetime import date # get the date

today = date.today().strftime("%Y-%m-%d")  # 2026-01-05 format
print(today)


# put the data in a csv and manage it with pandas
import pandas as pd
import os
 ##### TODO: make up the name from the first 15char in the title - DON'T do it i can group by the name of the project
filename = "products.csv"

# Check if file exists
if not os.path.exists(filename):
    # Create new CSV with headers
    df_new = pd.DataFrame({
        "name": [name],
        "price": [price],
        "date": [today]
    })
    df_new.to_csv(filename, index=False)
    print("New CSV created with data")
    
else:
    # File exists, read it
    df = pd.read_csv(filename)
    
    # Check if date exists
    if today in df['date'].values:
        print("Value for this date is already in the table")
    else:
        # Add new row
        new_row = pd.DataFrame({
            "name": [name],
            "price": [price],
            "date": [today]
        })
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(filename, index=False)
        print("New row added to existing CSV")


# make it run daily
# refactor the code
# wait for 10 seconds for a reponse. if not just continue with the rest of the program

# add tests