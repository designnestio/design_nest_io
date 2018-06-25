""" Helper methods for design_nest """
import design_nest

class BaseObject(object):

    _schema = {}
    _name = None

    def __init__(self):
        """ Init data dictionary object
        """
        self._data = {}
        for key in self.schema['patternProperties']['.*']['properties']:
            self._data[key] = None

    @property
    def schema(self):
        """ Get schema of class"""
        return self._schema

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

