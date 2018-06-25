import json


class Model(object):
    """ Represents an E+ epJSON file """

    required_objects = [{{required_objects}}]
    unique_objects = [{{unique_objects}}]

    def __init__(self, path=None):
        """ Inits epJSON object."""
        self._model = {}

        if path is not None:
            self.load(path)

    def add(self, obj):
        class_name = obj.schema['eplus_name']
        if class_name not in self._model:
            self._model[class_name] = {}
        if obj.name not in self._model[class_name]:
            self._model[class_name][obj.name] = {}

        self._model[class_name][obj.name] = obj.__dict__['_data']

    def save(self, path):
        """ Save epJSON to path.
        Args:
            path (str): path where data should be save
        """

        with open(path, 'w') as out_file:
            json.dump(self._model, out_file)
    
    def load(self, path):
        """ Loads epJSON data from path.
        Args:
            path (str): path to read data from
        """

        with open(path) as in_file:
            self._model = json.load(in_file)