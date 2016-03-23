import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.watsons.com.tw/%E7%86%B1%E9%8A%B7%E5%95%86%E5%93%81/c/bestSeller?q=:igcBestSeller:category:1041&page=5&resultsForPage=30&text=&sort=')
#print(res.text)
soup = BeautifulSoup(res.text)
for i in soup.select('.productName'):
	print(i.text)
