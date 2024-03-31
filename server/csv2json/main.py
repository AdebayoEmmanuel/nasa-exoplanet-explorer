import logging
import re
import azure.functions as func
import csv
import json
import logging
import re
import csv
import json
import json

json_converter = func.Blueprint()


@json_converter.route(route="csv2json", auth_level=func.AuthLevel.ANONYMOUS)
def csv2json(req: func.HttpRequest) -> func.HttpResponse:
    """
    Convert CSV data to JSON format.

    Args:
        req (func.HttpRequest): The HTTP request object.

    Returns:
        func.HttpResponse: The HTTP response object containing the converted JSON data.

    Raises:
        Exception: If there is an error converting CSV to JSON.

    """
    try:
        csv_file = req.files['csvFile']
        csv_data = csv_file.read().decode('utf-8')
        logging.info(f"CSV data: {csv_data}")  # Log the CSV data
        json_data = convert_csv_to_json(csv_data)
        return func.HttpResponse(json_data, status_code=200)
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse("Error converting CSV to JSON", status_code=500)


def convert_csv_to_json(csv_data):
    """
    Convert CSV data to JSON format.

    Args:
        csv_data (str): The CSV data to be converted.

    Returns:
        str: The JSON data converted from the CSV data.
    """
    lines = csv_data.splitlines()
    headers = lines[0].split(',')
    json_data = []
    for line in lines[1:]:
        values = line.split(',')
        json_data.append(dict(zip(headers, values)))
    return json.dumps(json_data, ensure_ascii=False)