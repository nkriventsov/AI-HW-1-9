import requests     # Library import
import json     # Library import
from flask import Flask     # Library import


def get_valutes_list(): # Function creation
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'  # Variable with json url
    response = requests.get(url)    # variable which sends a GET request to the specified url
    data = json.loads(response.text)    # variable which parses data
    valutes = list(data['Valute'].values())     # variable which creates a list from "Valute" section of data
    return valutes  # exit a function and return a value

def get_date(): # Function creation
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'  # Variable with json url
    response = requests.get(url)    # variable which sends a GET request to the specified url
    data = json.loads(response.text)    # variable which parses data
    date = str(data['Date'])     # variable which creates a list from "Valute" section of data
    return date  # exit a function and return a value


app = Flask(__name__)   # Variable of Flask module 1st argument


def create_html(valutes):   # Function creation
    text = '<h1>Курс валют</h1>'    # adds HTML Heading
    text += f'<b>{get_date()}</b><br><br>'  # adds HTML date
    text += '<table>'     # adds HTML table
    text += '<tr>'      # adds HTML row
    for _ in valutes[0]:    # Loop to search in data
        text += f'<th><th>'     # adds a cell with empty heading
    text += '</tr>'     # adds a row
    for valute in valutes:      # Loop to search in data
        text += '<tr>'      # adds a row
        for v in valute.values():   # Loop to search in data
            text += f'<td>{v}</td>'     # adds cells for each relevant value
        text += '</tr>'     # adds a row

    text += '</table>'      # ends the table
    return text     # exit a function and return a value


@app.route("/")     # binds a URL to a function
def index():        # Function creation
    valutes = get_valutes_list()        # variable which runs the function
    html = create_html(valutes)        # variable which runs the function
    return html     # exit a function and return a value


if __name__ == "__main__":      # restriction to run function only directly
    app.run()       # run function