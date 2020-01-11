import requests
url = 'http://localhost:1337/student/ongoinglecture/L1/'
myobj = {'somekey': 'somevalue'}
x = requests.post(url, data = myobj)
