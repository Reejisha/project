keyword=raw_input('Enter the product you want to search:')

def search_url(keyword):
	
	 keyword.replace(" ",'+')

	 Base_url ='https://www.amazon.com/s/ref=nb_sb_noss_2?keywords='
	 return Base_url + keyword
	

search_url(keyword)

