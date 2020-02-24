import http.client

h2 = http.client.HTTPConnection('10.41.18.32')
h2.connect()
h2.request("GET","/")
res = h2.getresponse()

print(res.status)

h2.close()
