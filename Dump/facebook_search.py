from urllib.request import urlopen
import json
def likes(access_token):
	url='https://graph.facebook.com/v2.10/me?fields=name%2Cfirst_name%2Clast_name%2Cgender%2Cid%2Clikes&access_token='+access_token
	f=urlopen(url)
	json1=json.load(f)
	return json1
def likes1(access_token):
	url=access_token
	f=urlopen(url)
	json1=json.load(f)
	return json1
def like_print(json):
	access_token=[]
	for i in json['likes']['data']:
		if 'IIIT' in i['name']:
			access_token.append(i)

	return access_token
def search(json):
	access_token=json['likes']['paging']['next']

	return access_token

p1=likes('EAACEdEose0cBAPbklCO7KdtBFP4HrjyP9aFtl2nRCBRTGZAFzEGsGX4ZALlk9xlQa1Co71L6wTXOncCMYxjdy6Ij04G6LzZCWjIZCtwslmU4UdTahbZA3h4gyDZB4YcYFtRMkZCxGepZAOp0EDIWDP48W4kNLiJbmDVmG6Ax8H2qVwF4gh5eOdiBTAuQVNQOEtS9cVINck8IYgZDZD')
p2=like_print(p1)
print(p2)
for i in range(10):
	access=search(p1)
	print(access)
	p1=likes1(access)
	print(p1)
	p2=like_print(p1)
	print(p2)