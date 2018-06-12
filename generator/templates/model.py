import json

groups = {
    'simulation_parameters':[
        'Version',
        'SimulationControl',
        'ShadowCalculations',
        'SurfaceConvectionAlgorithm:Outside',
        'SurfaceConvectionAlgorithm:Inside'
        'TimeStep',
        'GlobalGeometryRules',
        'HeatBalanceAlgorithm'
    ],
    'building': [
        'Site:Location',
        'Building'
    ],
    'climate': [
        'SizingPeriod:DesignDay',
        'Site:GroundTemperature:BuildingSurface',
    ],
    'schedules': [
        'ScheduleTypeLimits',
        'ScheduleDayHourly',
        'ScheduleDayInterval',
        'ScheduleWeekDaily',
        'ScheduleWeekCompact',
        'ScheduleConstant',
        'ScheduleFile',
        'ScheduleDayList',
        'ScheduleYear',
        'ScheduleCompact'
    ],
    'construction': [
        'Material',
        'Material:NoMass',
        'Material:AirGap',
        'WindowMaterial:SimpleGlazingSystem',
        'WindowMaterial:Glazing',
        'WindowMaterial:Gas',
        'WindowMaterial:Gap',
        'Construction'
    ],
    'internal_gains': [
        'People',
        'Lights',
        'ElectricEquipment',

    ],
    'airflow': [
        'ZoneInfiltration:DesignFlowRate',
        'ZoneVentilation:DesignFlowRate'
    ],
    'zone': [
        'BuildingSurface:Detailed',
    ],
    'zone_control': [
        'ZoneControl:Thermostat',
        'ThermostatSetpoint:SingleHeating',
        'ThermostatSetpoint:SingleCooling',
        'ThermostatSetpoint:SingleHeatingOrCooling',
        'ThermostatSetpoint:DualSetpoint',
    ],
    'systems': [
        'Zone:IdealAirLoadsSystem',
        'HVACTemplate:Zone:IdealLoadsAirSystem'
    ],
    'outputs': [
        'Output:SQLite',
        'Output:Table:SummaryReports'
    ]
}
class Model:
    """ Represents an E+ epJSON file """
    
    def __init__(self, path=None):
        """ Inits epJSON object."""
        self._model = {}

        with open('eplus_8.9_schema.json') as in_file:
            self._schema = json.load(in_file)

        if path is not None:
            self.load(path)

    def add(self, obj):
        self._model[obj.name].update(obj)
    

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

    @property
    def schema_version(self):
        """ Get e+ schema version. """
        return self._model["epJSON_schema_version"]