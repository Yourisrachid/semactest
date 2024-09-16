# Module import

import json
import requests
from bs4 import BeautifulSoup

# Main function


def get_title(request) :

    # Fetch the URL parameter

    url = request.args.get('url')

    if not url:

        # Return an error if no URL is provided (as parameter)

        return json.dumps({"error": "Please add an URL !"}), 400

    try:

        # Fetch the URL

        r = requests.get(url)

        # Raise an HTTPError for bad responses

        r.raise_for_status()  

        # Parse the HTML

        bsh = BeautifulSoup(r.content, 'html.parser')

        # Find and save the title from the h1 tag

        if bsh.h1:
            value = {
                "title": bsh.h1.get_text()
            }
        else:
            value = {
                "error": "No title was found on this page."
            }

        # Return the value as JSON

        return json.dumps(value), 200
    
    except Exception as e:

        # Handle exceptions and return an error 500

        return json.dumps({"error": f"Error: {e}"}), 500