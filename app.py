from flask import Flask, render_template, request
from salat import get_salat_timings
from waitress import serve
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/salat')
def salat():
    city = request.args.get('city')
    country = request.args.get('country')
    day_a = request.args.get('date')

    if not bool(city.strip()):
        city = "Tangail"
    if not bool (country.strip()):
        country = "Bangladesh"

    
    day = datetime.strptime(day_a, '%Y-%m-%d').strftime('%d-%m-%Y')
        

    get_n = get_salat_timings(day, country, city)
    
    if get_n == 201:
        return render_template('not_found.html')

    return render_template(
        'salat.html',
        city=city,
        country=country,
        date=date,
        fajr=get_n[0],
        dhuhr=get_n[1],
        asr=get_n[2],
        maghrib=get_n[3],
        isha=get_n[4]
    )

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
