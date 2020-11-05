"""
    Создайте свой класс и с помощью pickle запишите его в файл под название "MyClassInFile"
"""


import pickle


class MyClassInFile:

    def __init__(self, name):
        self._name = name

    def set(self, new_name):
        self._name = new_name
        return self._name

    def get(self):
        return self._name


with open('MyClassInFile.pickle', 'wb') as f:
    pickle.dump(MyClassInFile, f)