#pyidf

This Python library allows to read, modify and create EnergyPlus idf files.

[![Build Status](https://travis-ci.org/rbuffat/pyidf.svg?branch=master)](https://travis-ci.org/rbuffat/pyidf)
[![Coverage Status](https://coveralls.io/repos/rbuffat/pyidf/badge.png)](https://coveralls.io/r/rbuffat/pyidf)
[![Code Health](https://landscape.io/github/rbuffat/pyidf/master/landscape.svg)](https://landscape.io/github/rbuffat/pyidf/master)

The Pyidf library is generated from the current (EnergyPlus V8.4.0) Energy+.idd IDF specification. For each EnergyPlus Object a Python class is generated. This class is aware of the specified properties. Thus input values can be checked to be valid against the EnergyPlus specification.

Due to ambiguities in the EnergyPlus IDF specification file some EnergyPlus objects are (possibly) not correctly transferred to Python objects:

```
Site:SpectrumData
ZoneProperty:UserViewFactors:bySurfaceName
GroundHeatTransfer:Slab:XFACE
GroundHeatTransfer:Slab:YFACE
GroundHeatTransfer:Slab:ZFACE
GroundHeatTransfer:Basement:XFACE
GroundHeatTransfer:Basement:YFACE
GroundHeatTransfer:Basement:ZFACE
```

## Why should I use pyidf?

Pyidf represents EnergyPlus Objects as Python Classes. This allows auto completion. Pyidf EnergyPlus Objects are aware of their schema. Thus input values can be tested against the specification when the IDF is generated. The Python classes are documented based on the EnergyPlus specification.


## Installation
 
### pip:
```
pip install pyidf
```

### manual 
```
git clone https://github.com/rbuffat/pyidf.git
cd pyidf
python setup.py install
```
## Documentation

[Link to pyidf documentation page](https://rbuffat.github.io/pyidf)

## Usage

### Validation levels

Pyidf supports four different levels of validation. `ValidationLevel.no` does not perform any validation. `ValidationLevel.warn` issues warnings for all values not following the specification. `ValidationLevel.transition` tries to transition values to follow the specification. This includes casting float values to integers, matching values of choice types to values from the specification and setting default values for required fields when no value is set. For values not possible to match or cast, a warning is issued. `ValidationLevel.error` issues exceptions when a value is not valid according the specification. The default validation level is `ValidationLevel.transition`. The validation level can be changed with:

```python
from pyidf import ValidationLevel
import pyidf

pyidf.validation_level = ValidationLevel.no
```

### Reading an existing idf file

```python
import logging
from pyidf.idf import IDF

logging.info("start")
idf = IDF(r"/usr/local/EnergyPlus-8-2-0/ExampleFiles/BasicsFiles/Exercise1A.idf")
```

### Writing an existing idf file

```python
idf.save(r"~/Exercise1A_out.idf")
```

### Accessing data objects

Accessing data objects is possible either by the name of the object:

```python
for building in idf['Building']:
    print building

 # Output:
 # Building,Exercise 1A,0.0,Country,0.04,0.4,FullInteriorAndExterior,,6
```

or by the corresponding property:

```python
for building in idf.buildings:
    print building

 # Output:
 # Building,Exercise 1A,0.0,Country,0.04,0.4,FullInteriorAndExterior,,6
```

Both variants return a list of the corresponding data objects present in the idf object. The name of the EnergyPlus data dictionaries were pythonified, for example `BuildingSurface:Detailed` is represented by the Python class `BuildingSurfaceDetailed`. Each data dictionary is located in the module of its group. 

It is possible to iterate over all data objects of an idf object:
```python
for obj in idf:
    print obj

 # Output:
 # Version,8.2
 # Building,Exercise 1A,0.0,Country,0.04,0.4,FullInteriorAndExterior,,6
 # Timestep,4
 # SurfaceConvectionAlgorithm:Inside,TARP
 # ...
```

There are two types of fields. Normal fields and extensible fields. Normal fields exists only once while extensible fields can exist multiple times. Normal fields of a data object can similarly be accessed as data objects by their name, corresponding property or additionally by their index:

```python
print idf['Building'][0]['Name']

 # Output:
 # Exercise 1A
```

```python
print idf.buildings[0].name

 # Output:
 # Exercise 1A
```

```python
print idf.buildings[0][0]

 # Output:
 # Exercise 1A
```

The schema of normal fields can be accessed with:
```python
print idf['Building'][0].schema['fields']

 # Output
 # OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'default': u'NONE', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), ....
```

and of extensible fields with:
```python
print idf['Building'][0].schema['extensible-fields']

 # Output:
 # OrderedDict()  ( object has no extensible-fields)
```

The schema of a field can be accessed with:
```python
print idf['Building'][0].field("Name")

 # Output:
 # {'name': u'Name', 'pyname': u'name', 'default': u'NONE', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}
```

Extensible fields can be accessed with:
```python
print idf.buildingsurfacedetaileds[0].extensibles

 # Output:
 # [[8.0, 6.0, 2.7], [8.0, 6.0, 0.0], [0.0, 6.0, 0.0], [0.0, 6.0, 2.7]]
```

For example for `BuildingSurface:Detailed` the extensible fields are vertexes consisting of x,y,z values. The following code adds one to all coordinates:

```python
print idf["BuildingSurface:Detailed"][0].schema['extensible-fields'].keys()
a = idf.buildingsurfacedetaileds[0].extensibles
b = [map(lambda x: x + 1, ext) for ext in a]
idf.buildingsurfacedetaileds[0].extensibles = b
```

### Creating data objects

The following code creates a new `BuildingSurfaceDetailed` object and fills the values from an existing object: 

```python
from pyidf.idf import IDF
from pyidf.thermal_zones_and_surfaces import BuildingSurfaceDetailed

idf = IDF(r"/usr/local/EnergyPlus-8-2-0/ExampleFiles/BasicsFiles/Exercise1A.idf")
bsd = BuildingSurfaceDetailed()
for key in bsd.schema['fields']:
    bsd[key] = idf.buildingsurfacedetaileds[0][key]
bsd.extensibles = idf.buildingsurfacedetaileds[0].extensibles
bsd.name = "test"

idf2 = IDF()
idf2.add(bsd)
```

Extensible fields can be added with add_extensibles. The number of parameters required by this method depends on the number of extensible fields of a data object.

```python
bsd.add_extensible(1.0, 2.0, 3.0)
```

Single values of extensible fields can be altered by referencing the field to alter with a tuple (field name, index):

```python
print bsd[(u'Vertex 1 Y-coordinate', 4)]
bsd[(u'Vertex 1 Y-coordinate', 4)] = 11.0
print bsd[(u'Vertex 1 Y-coordinate', 4)]
```

All values with corresponding keys of a data object can be accessed with the method items():
```python
print bsd.items()

 # Output:
 # [(u'Name', 'test'), (u'Surface Type', 'Wall'), (u'Construction Name', 'LTWALL'), (u'Zone Name', 'ZONE ONE'), (u'Outside Boundary Condition', 'Outdoors'), (u'Outside Boundary Condition Object', None), (u'Sun Exposure', 'SunExposed'), (u'Wind Exposure', 'WindExposed'), (u'View Factor to Ground', 0.5), (u'Number of Vertices', 4.0), ((u'Vertex 1 X-coordinate', 0), 8.0), ((u'Vertex 1 Y-coordinate', 0), 6.0), ((u'Vertex 1 Z-coordinate', 0), 2.7), ((u'Vertex 1 X-coordinate', 1), 8.0), ((u'Vertex 1 Y-coordinate', 1), 6.0), ((u'Vertex 1 Z-coordinate', 1), 0.0), ((u'Vertex 1 X-coordinate', 2), 0.0), ((u'Vertex 1 Y-coordinate', 2), 6.0), ((u'Vertex 1 Z-coordinate', 2), 0.0), ((u'Vertex 1 X-coordinate', 3), 0.0), ((u'Vertex 1 Y-coordinate', 3), 6.0), ((u'Vertex 1 Z-coordinate', 3), 2.7)]

```

## Notes

### Field name issues

Keep in mind that pyidf is automatically generated from the specification. For some fields, especially extensible-fields, the field name contains a number where it shouldn't. For example for "BuildingSurface:Detailed", the specification looks as follows:
```
...
  N3,  \field Vertex 1 X-coordinate
       \begin-extensible
       \required-field
       \units m
       \type real
  N4 , \field Vertex 1 Y-coordinate
       \required-field
       \units m
       \type real
  N5 , \field Vertex 1 Z-coordinate
       \required-field
       \units m
       \type real
  N6,  \field Vertex 2 X-coordinate
       \required-field
       \units m
       \type real
  N7,  \field Vertex 2 Y-coordinate
       \required-field
       \units m
       \type real
  N8,  \field Vertex 2 Z-coordinate
       \required-field
       \units m
       \type real
...
```

In pyidf only the 3 fields "Vertex 1 [X|Y|Z]-coordinate" are included in the schema. Extensible fields are implemented as a list of lists containing the values of the extensible fields. Thus field names can contain a number, for example "Vertex 1 X-coordinate", but should be named "Vertex X-coordinate" or "Vertex n X-coordinate" 

## Library generation

Large parts of this library are generated automatically. In case the library should be rebuilt, for example to fix bugs or generate the library for a different EnergyPlus version, main.py in the generator package need to be executed. Currently generator/V8-2-0-Energy+.idd is used as basis to generate the library. generator/V8-2-0-Energy+Alt.idd contains modified data objects. Every data object in V8-2-0-Energy+Alt.idd overwrites data objects with the same name in the original idd. Generating the library requires the libraries jinja2, autopep8 and docformatter.

## Alternatives

An alternative Python library to manipulate EnergyPlus idf files is [eppy](https://github.com/santoshphilip/eppy).