import requests  

def shorten_url(url):
	base_url = 'http://tinyurl.com/api-create.php?url='
	url = base_url + url
	print('Original URL', url)
	r = requests.get(url)
	print(r.text)

url = 'https://github.com/anurag123-ctrl/CodeClause_url_shortner/blob/main/code%20clause/urlsho.py'
shorten_url(url)
