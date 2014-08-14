#############################################################
# Use google api to saerch for some links
#
# Time: 2014814
# Usage:
#   python google_result.py
#############################################################
import requests
import re

headers  = {
    'User-agent':'Mozilla/5.0 (X11; Linux i686; rv:2.0.0) Gecko/20130130',
}

google_api = 'http://www.google.com/search?q='

keyword='site:*.qq.com inurl:.swf'

url = google_api+keyword+'&number=100&start=0'

response = requests.get(url)

content = response.text

m = re.search('did not match any',response.text)

if m:
    print '[-]did\'t get any userful info!'

print m
#print response.text
