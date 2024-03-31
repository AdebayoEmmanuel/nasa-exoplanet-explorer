import azure.functions as func
import datetime
import json
import logging
from csv2json.main import bp1

app = func.FunctionApp()

app.register_functions(bp1)