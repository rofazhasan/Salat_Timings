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
    city = request.args.get('city', 'Tangail').strip()
    country = request.args.get('country', 'Bangladesh').strip()
    day_a = request.args.get('date', '').strip()

    if not city:
        city = "Tangail"
    if not country:
        country = "Bangladesh"

    if not day_a:
        day = datetime.now().strftime('%d-%m-%Y')
    else:
        try:
            day = datetime.strptime(day_a, '%Y-%m-%d').strftime('%d-%m-%Y')
        except ValueError:
            return render_template('error.html', message="Invalid date format. Please use YYYY-MM-DD.")

    get_n = get_salat_timings(day, country, city)
    
    if get_n == 201:
        return render_template('not_found.html')

    return render_template(
        'salat.html',
        city=city,
        country=country,
        date=get_n[5],
        fajr=get_n[0],
        dhuhr=get_n[1],
        asr=get_n[2],
        maghrib=get_n[3],
        isha=get_n[4]
    )

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
