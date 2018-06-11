

class Model:
    """ Represents an E+ epJSON file """

    required_objects = ["building", "globalgeometryrules"]
    unique_objects = [
        "zoneairheatbalancealgorithm",
        "surfaceconvectionalgorithm:outside:adaptivemodelselections",
        "outputcontrol:sizing:style",
        "runperiodcontrol:daylightsavingtime",
        "building",
        "zoneairmassflowconservation",
        "zoneaircontaminantbalance",
        "site:groundtemperature:shallow",
        "site:solarandvisiblespectrum",
        "output:debuggingdata",
        "outputcontrol:illuminancemap:style",
        "site:heightvariation",
        "lifecyclecost:parameters",
        "timestep",
        "convergencelimits",
        "heatbalancesettings:conductionfinitedifference",
        "version",
        "airflownetwork:simulationcontrol",
        "site:weatherstation",
        "globalgeometryrules",
        "output:energymanagementsystem",
        "shadowcalculation",
        "site:groundreflectance",
        "site:groundtemperature:buildingsurface",
        "surfaceconvectionalgorithm:inside",
        "hvactemplate:plant:chilledwaterloop",
        "site:location",
        "parametric:logic",
        "parametric:runcontrol",
        "surfaceconvectionalgorithm:inside:adaptivemodelselections",
        "zonecapacitancemultiplier:researchspecial",
        "compliance:building",
        "sizing:parameters",
        "hvactemplate:plant:hotwaterloop",
        "site:groundtemperature:deep",
        "hvactemplate:plant:mixedwaterloop",
        "outputcontrol:reportingtolerances",
        "simulationcontrol",
        "output:sqlite",
        "site:groundtemperature:fcfactormethod",
        "heatbalancealgorithm",
        "parametric:filenamesuffix",
        "geometrytransform",
        "outputcontrol:table:style",
        "surfaceconvectionalgorithm:outside",
        "output:table:summaryreports",
        "currencytype"]
    
    def __init__(self, path=None):
        """ Inits epJSON object."""
        self._data = {}
        self.comment_headers = []

        if path is not None:
            self.read(path)
