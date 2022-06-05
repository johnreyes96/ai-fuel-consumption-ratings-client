import requests
from sklearn.linear_model import LinearRegression
import pickle as pk
import json

URL = 'http://localhost:8090'


def populateDB():
    requests.get(URL + '/populate-db')


def getPersonRStats():
    personRStats = requests.get(URL + '/person-stats')
    print(personRStats.text)


def trainingDatasetToLinearRegression():
    Dataset = requests.get(URL + '/dataset-linear-regression')
    X = Dataset.json()['X']
    y = Dataset.json()['y']
    model = LinearRegression().fit(X, y)
    pickle_file = open('D:\\Users\\jhonf\\Documents\\Programacion\\Codigo\\Python\\ai-fuel-consumption-ratings\\src'
                       '\\main\\resoures\\modelo.txt', 'wb')
    pk.dump(model, pickle_file)
    return X


def predictLinearRegression(X):
    predictions = {'predictions': X}
    data = json.dumps(predictions)
    result = requests.post(URL + '/predict', data=data, headers={"Content-Type": "application/json"})
    print(result.text)


if __name__ == '__main__':
    populateDB()
    getPersonRStats()
    samples = trainingDatasetToLinearRegression()
    predictLinearRegression(samples)
