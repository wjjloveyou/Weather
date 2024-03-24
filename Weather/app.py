from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': '城市名称不能为空'}), 400

    url = f'http://v1.yiketianqi.com/api?unescape=1&version=v63&appid=96418142&appsecret=t2exMqgR&city={city}'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

    weather_data = response.json()



    return jsonify(weather_data)



from flask import render_template

@app.route('/')
def index():
    return render_template('weacher.html')

if __name__ == '__main__':
    app.run(debug=True)
