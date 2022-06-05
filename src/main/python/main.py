import requests
from sklearn.linear_model import LinearRegression
import pickle as pk

URL = 'http://localhost:8090'


def populateDB():
    requests.get(URL + '/populate-db')


def getPersonRStats():
    personRStats = requests.get(URL + '/person-stats')
    print(personRStats.text)


def getDatasetToLinearRegression():
    Dataset = requests.get(URL + '/dataset-linear-regression')
    X = Dataset.json()['X']
    y = Dataset.json()['y']
    model = LinearRegression().fit(X, y)
    pickle_file = open('D:\\Users\\jhonf\\Documents\\Programacion\\Codigo\\Python\\ai-fuel-consumption-ratings\\src'
                       '\\main\\resoures\\modelo.txt', 'wb')
    pk.dump(model, pickle_file)


if __name__ == '__main__':
    # populateDB()
    # getPersonRStats()
    getDatasetToLinearRegression()
