import requests, json
from bs4 import BeautifulSoup
import shutil
import os
try:
    os.chdir('img')
    #means cd path
except:
    print('path error')
imageUrlPattern = 'http://www.watsons.com.tw'
res =requests.get('http://www.watsons.com.tw/%E7%86%B1%E9%8A%B7%E5%95%86%E5%93%81/c/bestSeller?q=:igcBestSeller:category:1041&page=5&resultsForPage=30&text=&sort=')
soup = BeautifulSoup(res.text)

for i in soup.select('img'):
    try:
        fname = i['alt']
        imageUrl = imageUrlPattern + i['src']
        ires = requests.get(imageUrl,stream=True)
        f = open(fname,'wb')
        shutil.copyfileobj(ires.raw,f)
        f.close()
        del ires
    except Exception as e:
        print(i)
        print(e)