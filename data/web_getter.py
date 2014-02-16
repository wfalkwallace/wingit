from httplib2 import httplib2
from urllib import urlencode
h = Http()
data = dict(
	f = JFK,
	d = 2014-02-20, 
	r = 2014-03-14
	)
resp, hontent = h.request('http://www.google.com/flights/#search', 'POST', urlencode(data))
resp