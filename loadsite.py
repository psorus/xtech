import sys
import json



vers=sys.version
vers=vers[:vers.find(".")]
vers=float(vers)

if vers<3:
  import urllib
  import urllib2
else:
  # import urllib.request as u
  import urllib.parse
  import urllib.request

def loadsite(url,values=None):
  if vers<3:
    if not values is None:
      data = urllib.urlencode(values)
      req = urllib2.Request(url, data)
    else:
      req=urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page.decode("utf-8")
  else:
    if not values is None:
      data = urllib.parse.urlencode(values)
      req = urllib.request.Request(url, data.encode("utf-8"))
    else:
      req=urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    return the_page.decode("utf-8")