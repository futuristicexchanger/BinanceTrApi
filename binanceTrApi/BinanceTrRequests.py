import requests
import Apihelpers
import sys
import traceback


def sendRequest(method, url, options, parameters=None, cancellationToken="default"):
    try:
        url = Apihelpers.GetRequestUrl(url, True)
        urlExtension = str(Apihelpers.CreateQueryString(parameters))
        if method == "GET":
            url = url + str(urlExtension) + "&" + str(Apihelpers.BuildRequest(options.secret, urlExtension))
            response = requests.get(url, headers={"X-MBX-APIKEY": options.api})
            return response.json()
        elif method == "POST":
            parameters["signature"] = str(Apihelpers.BuildRequest(options.secret, urlExtension)).split("=")[1]
            response = requests.post(url, headers={"X-MBX-APIKEY": options.api}, data=parameters)
            return response.json()

    except Exception:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
        print(errorDetails)


def sendRequestWithoutAuthorization(url, parameters=None, baseUrl=False):
    try:
        url = Apihelpers.GetRequestUrl(url, baseUrl)
        request = requests.get(url)
        return request

    except Exception:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
        print(errorDetails)
