""" Python library to generate building analysis models
    Author: designnest.io
    License: Apache License 2.0
"""

__author__ = "designnest.io"
__copyright__ = "Copyright 2018"
__credits__ = []
__license__ = "Apache 2.0"
__version__ = "{{ version }}"
__maintainer__ = "designnest.io"
__email__ = "designnestio@gmail.com"
__status__ = "Development"


class ValidationLevel(object):
    """ Validation levels:
        - no: no validation
        - warn: issue warnings
        - transition: try to transition values to follow specification
        - error: raise exceptions when values are not according specification"""
    no = "no"
    warn = "warm"
    transition = "transition"
    error = "error"

validation_level = ValidationLevel.transition