import requests
import xml.etree.ElementTree as ET

SERVER_ACTIVE = 'http://localhost:8081'

r = requests.get(SERVER_ACTIVE + '/TimeUTC')