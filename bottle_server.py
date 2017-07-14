import income_portfolio
import json

from bottle import route, run, template

@route('/dividends')
def index():
    name = 'dividends' 
    endpoints = ['getYield']

    response_json = json.dumps(endpoints)
    return response_json


@route('/dividends/<symbol>')

def get_dividend(symbol):

  
    dividend_dictionary = {"amount":1} 

    response = json.dumps(dividend_dictionary) 

    return response

run(host='localhost', port=8080, debug=True)

