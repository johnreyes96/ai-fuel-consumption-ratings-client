import requests

URL = 'http://localhost:8090'


def populateDB():
    requests.get(URL + '/populate-db')


def getPersonRStats():
    personRStats = requests.get(URL + '/person-stats')
    print(personRStats.text)


if __name__ == '__main__':
    populateDB()
    getPersonRStats()
