from enum import Enum


class WeatherProp(Enum):
    """
    enum reduces risk of misspelling dictionary keys
    https: // docs.python.org / 3 / library / enum.html

    seattle-data.csv field names contains abbreviations. Doesn't include measurement units.

    These abbreviations appear to match. Units may be different, not sure.
    https://github.com/soodoku/get-weather-data/blob/master/zip2wd/column-names-info.txt

    awnd average wind speed
    http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.DAILY/.FSOD/.AWND/

    snwd snow depth [mm]?
    http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.DAILY/.FSOD/.SNWD/
    """
    STATION = "STATION"
    NAME = "NAME"
    DATE = "DATE"
    AWND = "AWND"
    PRCP = "PRCP"
    SNOW = "SNOW"
    SNWD = "SNWD"
    TAVG = "TAVG"
    TMAX = "TMAX"
    TMIN = "TMIN"
    WT01 = "WT01"
    WT02 = "WT02"
    WT03 = "WT03"
    WT05 = "WT05"
    WT08 = "WT08"
