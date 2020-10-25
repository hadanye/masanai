def makeURL(**kwargs):
    myUr1 = "http://192.168.1.120/index.php?"
    for k,v in kwargs. items():
        myUr1 += k + '=' +v+ '&'

    myUrl = myUrl.rstrip('&')
    print(myUrl)

makeURL(user = 'psychoria', index = '5', page = '10')