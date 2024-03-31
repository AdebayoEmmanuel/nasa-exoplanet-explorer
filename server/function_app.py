import azure.functions as func
import datetime
import json
import logging
from csv2json.main import json_converter

app = func.FunctionApp()

app.register_functions(json_converter)