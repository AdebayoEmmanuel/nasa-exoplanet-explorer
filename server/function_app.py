import azure.functions as func
import datetime
import json
import logging
from csv2json.main import json_converter
from fetchdata.main import data_fetcher

app = func.FunctionApp()

app.register_functions(json_converter)
app.register_functions(data_fetcher)