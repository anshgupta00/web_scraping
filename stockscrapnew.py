# %% [markdown]
# # web scraping from merolagani.com for study purposes:

# %% [markdown]
# 

# %%
import requests
from bs4 import BeautifulSoup

# %%
web = requests.get("https://merolagani.com/LatestMarket.aspx/")
web

# %%
web.content

# %%
print(web.text)


# %%
soup= BeautifulSoup(web.content,"html.parser")
soup

# %%
web.url

# %%
soup= BeautifulSoup(web.text,"html.parser")
soup

# %%


url = "https://merolagani.com/LatestMarket.aspx/"  # Replace with the target website
response = requests.get(url)

print(response.headers.get("Content-Type"))


# %%
# !pip install beautifulsoup4 lxml html5lib
# 


# %%
soup= BeautifulSoup(web.text,"html.parser")
soup

# %%
table=soup.find("table",class_="table table-hover live-trading sortable")
headers=[i.text for i in table.find_all('th')]
# print(headers)
data=[j for j in table.find_all('tr',{"class":["increase-row","decrease-row","nochange-row"]})]


# %%
result=[{headers[index]:cell.text for index,cell in enumerate(row.find_all("td"))} for row in data]
print(result)

# %%
# !pip install pandas 


# %%
import pandas as pd

# %%
columns = ["Symbol", "LTP", "% Change", "Open", "High", "Low", "Qty.", "PClose", "Diff."]


# %%
data_df=pd.DataFrame(result,columns=columns)
data_df.head()

# %%
data_df.to_csv("stockNepse.csv",index=False)

# %%



