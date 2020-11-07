"""
    Написать функцию isabstract, которая проверяет, является ли класс абстрактным или нет
"""

import abc


class PluginBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, input):
        pass

    @abc.abstractmethod
    def save(self, output, data):
        pass


class DefaultClass:
    def load(self, input):
        pass

    def save(self, output, data):
        pass


def isabstract(class_ob: object):
    return '__abstractmethods__' in dir(class_ob)


print(isabstract(DefaultClass))
print(isabstract(PluginBase))