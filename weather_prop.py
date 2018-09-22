from enum import Enum


class WeatherProp(Enum):
    """
    enum reduces risk of misspelling dictionary keys
    https: // docs.python.org / 3 / library / enum.html
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
