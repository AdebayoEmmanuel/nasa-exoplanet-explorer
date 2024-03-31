import logging
import re
import azure.functions as func
import csv
import json

bp1 = func.Blueprint()

@bp1.route(route="csv2json", auth_level=func.AuthLevel.ANONYMOUS)
def csv2json(req: func.HttpRequest) -> func.HttpResponse:
    try:
        csv_data = req.get_body().decode('utf-8')
        json_data = CSV2JSON(csv_data)
        logging.info(json_data)
        return func.HttpResponse(json_data, status_code=200)
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse("Error converting CSV to JSON", status_code=500)

import re

def CSVToArray(strData, strDelimiter):
    """
    Convert a CSV string to a 2D array.

    Args:
        strData (str): The CSV string to be converted.
        strDelimiter (str): The delimiter used in the CSV string.

    Returns:
        list: A 2D array representing the CSV data.

    Example:
        >>> CSVToArray('1,2,3\n4,5,6', ',')
        [['1', '2', '3'], ['4', '5', '6']]
    """
    arrData = []
    # Check to see if the delimiter is defined. If not,
    # then default to comma.
    if not strDelimiter:
        strDelimiter = ','
    # Create a regular expression to parse the CSV values.
    objPattern = re.compile(
        r'(\\" + re.escape(strDelimiter) + "|\\r?\\n|\\r|^)(?:"([^"]*(?:""[^"]*)*)"|' + '([^"\\" + re.escape(strDelimiter) + "\\r\\n]*))',
        re.MULTILINE | re.DOTALL)
    # Keep looping over the regular expression matches
    # until we can no longer find a match.
    for arrMatches in objPattern.findall(strData):
        # Get the delimiter that was found.
        strMatchedDelimiter = arrMatches[0]
        # Check to see if the given delimiter has a length
        # (is not the start of string) and if it matches
        # field delimiter. If id does not, then we know
        # that this delimiter is a row delimiter.
        if strMatchedDelimiter and (strMatchedDelimiter != strDelimiter):
            # Since we have reached a new row of data,
            # add an empty row to our data array.
            arrData.append([])
        # Now that we have our delimiter out of the way,
        # let's check to see which kind of value we
        # captured (quoted or unquoted).
        if arrMatches[1]:
            # We found a quoted value. When we capture
            # this value, unescape any double quotes.
            strMatchedValue = arrMatches[1].replace('""', '"')
        else:
            # We found a non-quoted value.
            strMatchedValue = arrMatches[2]
        # Now that we have our value string, let's add
        # it to the data array.
        arrData[-1].append(strMatchedValue)
    # Return the parsed data.
    return arrData

def CSV2JSON(csv):
    """
    Convert a CSV string to a JSON string.

    Args:
        csv (str): The CSV string to be converted.

    Returns:
        str: The JSON string representing the converted data.
    """
    array = CSVToArray(csv, ',')

    objArray = []
    for i in range(1, len(array)):
        objArray.append({})
        for k in range(min(len(array[0]), len(array[i]))):
            key = array[0][k]
            objArray[i - 1][key] = array[i][k]
    json_data = json.dumps(objArray)
    return json_data