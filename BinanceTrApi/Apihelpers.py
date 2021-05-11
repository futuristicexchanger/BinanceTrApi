import time
import datetime
import dateparser
import pytz
from .UserModel import UserModel as UM
import json
import os
current_dir = os.path.dirname(__file__)
target_dir = os.path.abspath(os.path.join(current_dir, "constants.json"))


with open(target_dir) as json_file:
    c = json.load(json_file)


def contain(source, value):
    if value not in source:
        return True
    else:
        return False


def GetRequestUrl(url, baseUrl=False):
    if baseUrl:
        return c["BASE_URL"] + url
    return c["API_URL"] + url


def CreateQueryString(parameters):
    if parameters == None:
        return ""

    parameters["timestamp"] = GetTimestamp()
    resultList = []
    for k, v in parameters.items():
        resultList.append(f"{k}={v}")
    result = "&"
    return "?" + result.join(resultList)


def BuildRequest(apiSecret, extension):
    if (extension == None) or (len(extension) == 0):
        extension = "&" + GetTimestamp()

    temp = UM("", apiSecret)
    if (apiSecret != None) or (apiSecret != ""):
        return "signature=" + temp.generate_signature(extension[1:])


def GetTimestamp():
    return str(int(round(time.time() * 1000)))


def date_to_milliseconds(date_str):
    epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
    d = dateparser.parse(date_str)
    if d.tzinfo is None or d.tzinfo.utcoffset(d) is None:
        d = d.replace(tzinfo=pytz.utc)
    return int((d - epoch).total_seconds() * 1000.0)


def interval_to_milliseconds(interval):
    ms = None
    seconds_per_unit = {
        "m": 60,
        "h": 60 * 60,
        "d": 24 * 60 * 60,
        "w": 7 * 24 * 60 * 60
    }
    unit = interval[-1]
    if unit in seconds_per_unit:
        try:
            ms = int(interval[:-1]) * seconds_per_unit[unit] * 1000
        except ValueError:
            pass
    return ms