import requests, json
from bs4 import BeautifulSoup
product_key=["productName","brandName","price"]
final_prod_json_arr=[]
def crawl_watsons():
	prod_dict={}
	res = requests.get('http://www.watsons.com.tw/%E7%86%B1%E9%8A%B7%E5%95%86%E5%93%81/c/bestSeller?q=:igcBestSeller:category:1041&page=5&resultsForPage=30&text=&sort=')
	#print(res.text)
	soup = BeautifulSoup(res.text)

	counter=0
	for i in soup.select('.productName'):
		prod=[] #productName
		prod.append(i.text)
		prod.append(soup.select('.brandName')[counter].text)
		prod.append(soup.select('.promoPrice')[counter].text.strip())#strip可以把前後不必要的空白去掉
		counter+=1
		prod_dict=dict(zip(product_key,prod))
		final_prod_json_arr.append(prod_dict)

	with open('watsons.json','w',encoding='UTF-8') as f:
		f.write('[')
		for i in final_prod_json_arr:
			s=json.dumps(i, ensure_ascii=False, sort_keys=True)
			f.write(s+',')
		f.write(']')




def start_json(json_path):
    with open(json_path, 'w' ,encoding = 'UTF-8') as json_file:
        json_file.truncate()#如果沒有傳入參數的話，就會本全文清空
        #若傳入整數n的話，是指把n位置以後的文字都刪掉
        json_file.write('[')#單純只是寫入而已

def to_json(json_path,arr,notFirst = False):
    # print(arr)
    with open(json_path, 'a', encoding='UTF-8') as json_file:
        #with 述句執行完畢後會自動關檔，後面的as 則是把開檔完的reference指派給as 後的變數
        #as裡面的名稱在外部是看不到的，是區域變數
        for d in arr:
            json_str = json.dumps(d, ensure_ascii=False, sort_keys=True)
            #在這裡使用到json的module,dump是轉存，將python的物件型態轉成json的物件型態
            #因為json是js的型態；ensure_ascii若為true(預設)
            #就會確保所有輸入的字元都是ascii，若非則跳過那個字元
            #設為false就會照原樣輸出
            #sort_keys預設為false，功用為把key做排序
            json_file.write('{}{}'.format((',' if notFirst else ''), json_str))
            #str.format()這個函式，會在{}裡面填入字串，{}裡面可以放index或key名稱
            notFirst = True

def end_json(json_path):
    with open(json_path, 'a' ,encoding = 'UTF-8') as json_file:
        json_file.write(']')

if __name__  ==  "__main__":
    # start_json('watsons.json')
    crawl_watsons()
    #print(course_unit)
    # to_json('ptt_comment.json',course_unit,False)
    # end_json('ptt_comment.json')