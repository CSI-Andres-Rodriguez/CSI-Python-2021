import json, ssl
import os
from pathlib import Path
import urllib.request
from Cannabis import Cannabis

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
cannabisURL = "https://random-data-api.com/api/cannabis/random_cannabis"


req = urllib.request.Request(cannabisURL)
r = json.loads(urllib.request.urlopen(req).read())

cannabis:Cannabis = Cannabis(**r)

print(cannabis.strain)

