from app import app
import requests
from bs4 import BeautifulSoup
from flask import request, jsonify
import time


supported_sources = {
    "SGD": "Singapore Dollar",
    "MYR": "Malaysian Ringgit",
    "LKR": "Sri Lankan Rupee",
    "USD": "United States Dollar",
    "GBP": "British Pound Sterling",
}


@app.route("/api/live")
def index():
    source = request.args.get("source", "USD")
    values_res_dict = dict()
    timestamp = int(time.time() * 1000.0)
    for cur in supported_sources:
        if cur != source:
            query = f"1+{source}+to+{cur}"
            user_agent_header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
            }
            url = "https://www.google.com/search?q=" + query
            res = requests.get(url, headers=user_agent_header)
            try:
                soup = BeautifulSoup(res.text, "html.parser")
                result = soup.find("div", {"class": "b1hJbf"}).attrs[
                    "data-exchange-rate"
                ]
                valueAccurate = float(result)
                values_res_dict[source + cur] = valueAccurate
            except TypeError:
                return jsonify(
                    {
                        "success": False,
                        "code": 1500,
                        "messafe": "Unable to get exchange rates at the moment",
                    }
                )

    return jsonify(
        {
            "success": True,
            "code": 200,
            "source": source,
            "quotes": values_res_dict,
            "timestamp": timestamp,
        }
    )


@app.route("/api/list")
def list():
    return jsonify({"success": True, "code": 200, "currencies": supported_sources})
