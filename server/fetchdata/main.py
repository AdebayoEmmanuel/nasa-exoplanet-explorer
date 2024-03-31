import azure.functions as func
import logging
import subprocess
import os

data_fetcher = func.Blueprint()

@data_fetcher.route(route="datafetcher", auth_level=func.AuthLevel.ANONYMOUS)
def fetchdata(req: func.HttpRequest) -> func.HttpResponse:
    # Print the current working directory
    logging.info(f"Current working directory: {os.getcwd()}")

    # Get the path to the fetch script
    fetch_script_path = os.path.join(os.getcwd(), "fetch")

    # Run the fetch script
    fetch_script_output = subprocess.run([fetch_script_path], capture_output=True, text=True)
    
    # Forward the response from the fetch script to the caller
    return func.HttpResponse(fetch_script_output.stdout, status_code=200)
