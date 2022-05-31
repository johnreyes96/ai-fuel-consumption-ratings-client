import requests

URL = 'http://localhost:8090'


def populateDB():
    requests.get(URL + '/populate-db')


def getPersonRStats():
    personRStats = requests.get(URL + '/person-stats')
    print(personRStats.text)


def linearRegressionFeatureImportance():
    linearRegression = requests.get(URL + '/linear-regression-feature-importance')
    print(linearRegression.text)


if __name__ == '__main__':
    # populateDB()
    # getPersonRStats()
    linearRegressionFeatureImportance()
