def e(date):
	m=date[:date.find('/')]
	d=date[(date.find('/')+1):date.rfind('/')]
	y=date[date.rfind('/')+1:]
	if len(d)==1:
		d="0"+d
	if len(m)==1:
		m="0"+m
	assert (int(d)<=31 and int(m)<=12), "enter a proper date" 
	dn=d+'/'+m+'/'+y
	return dn

date=input('aa')
print(e(date))