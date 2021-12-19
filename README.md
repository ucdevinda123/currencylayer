[![CodeFactor](https://www.codefactor.io/repository/github/ucdevinda123/currencylayer/badge)](https://www.codefactor.io/repository/github/ucdevinda123/currencylayer)

Currency Layer API Implementation : 
This is an attempt to make latest/live  exchange rates via flask rest api. Few more improvements are in the pipeline and eventually it will have the same functionality ass currency layer api but for free :)  Feel free to hop on cheers!


# 1. Create a Virtual Environment : python -m venv env

# 2. Activate Virtual Environment : source ./env/bin/activate

# Endpoints :

# Get List of Countries : <http://127.0.0.1:5000/list>

{
"code": 200,
"currencies": {
"AUD": "Australian Dollar",
"BTN": "Bhutanese Ngultrum",
"CAD": "Canadian Dollar",
"EUR": "Euro",
"GBP": "British Pound Sterling",
"INR": "Indian Rupee",
"JPY": "Japanese Yen",
"LKR": "Sri Lankan Rupee",
"MYR": "Malaysian Ringgit",
"NZD": "New Zealand Dollar",
"SGD": "Singapore Dollar",
"USD": "United States Dollar"
},
"success": true
}

# Get Live currency Rates : <http://127.0.0.1:5000/live?source=SGD>

{
"code": 200,
"quotes": {
"SGDAUD": 1.025801702,
"SGDBTN": 55.03972502,
"SGDCAD": 0.9405275287,
"SGDEUR": 0.6485208737,
"SGDGBP": 0.55179,
"SGDINR": 55.704014900000004,
"SGDJPY": 83.02433562,
"SGDLKR": 147.9224083,
"SGDMYR": 3.080209625,
"SGDNZD": 1.0856045600000002,
"SGDSGD": 0.3229171,
"SGDUSD": 0.73225
},
"source": "SGD",
"success": true
}
