import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialise stuff
url = "https://topforeignstocks.com/indices/components-of-the-sp-500-index/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

stocks = pd.DataFrame(columns = ["Name", "Ticker", "Sector", "Market Cap", "PE Ratio"])
i = 0

# Go through first table ignoring top row
for row in soup.find_all('table')[0].tbody.find_all('tr')[1:]:
    # Select associated column and assign value to associated variable
    name = row.find_all('td')[1].text
    ticker = row.find_all('td')[2].text
    sector = row.find_all('td')[3].text

    # Initialise secondary site
    stockUrl = "https://finance.yahoo.com/quote/" + ticker + "?ltr=1"
    stockPage = requests.get(stockUrl)
    # Check if page actually exists
    if stockPage.status_code == 200:
        i += 1
        stockSoup = BeautifulSoup(stockPage.content, "html.parser")

        stats = []

        # Find correct table and select all text, appending to list
        for row in stockSoup.find_all('table')[1].tbody.find_all('tr'):
            stats.append(row.find_all('td')[1].text)

        # Selecting right values from list and putting in associated variables
        marketCap = stats[0]
        peRatio = stats[2]

        # Make a dataframe of company by itself
        company = pd.DataFrame({"Name":name, "Ticker":ticker, "Sector":sector, "Market Cap":marketCap, "PE Ratio":peRatio}, index=[i])
        
        # Merge with rest of companies
        stocks = pd.merge(stocks, company, how="outer")

# Output full list as a CSV
stocks.to_csv("Part 1 Output", sep='\t', encoding='utf-8')