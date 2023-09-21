import urllib.request


try:
    url= urllib.request.urlopen('http://www.youtube.com')

except urllib.error.URLError:
    print('Pagina Offiline')

else:
    print('Pagina online')
    #print(url.read())


