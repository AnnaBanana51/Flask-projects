from flask import Flask, render_template, request
import math
from Anna_script import scrapper

app = Flask(__name__)

url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"


@app.route('/')
def welcome_home():
    return f"working on scrapping data from {url}"

@app.route('/covid19')
def scrapper():
    table = scrapper(url)
    return render_template("table.html", data=table)

@app.route('/user/<user>')
def message(username):
    return f"Hello {username}"

@app.route('/sqrt/<num>')
def squared_root_num(num):
    return srt(math.sqrt(int(num)))

@app.route('/login', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        result = request.form
        return result
    else:
        return f"this was a {request.method}"

if __name__ == '__main__':
    print(soup.prettify())
    app.run(debug=True)
