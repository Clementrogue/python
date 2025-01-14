from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Health Calculator API!",
        "routes": {
            "/bmi": "POST - Calculate BMI (requires 'height' in meters and 'weight' in kg)",
            "/bmr": "POST - Calculate BMR (requires 'height' in cm, 'weight' in kg, 'age' in years, and 'gender')"
        }
    })

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    height = data['height']  # in meters
    weight = data['weight']  # in kilograms
    bmi_result = calculate_bmi(height, weight)
    return jsonify({'bmi': bmi_result}), 200

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    height = data['height']  # in cm
    weight = data['weight']  # in kg
    age = data['age']        # in years
    gender = data['gender']  # 'male' or 'female'
    bmr_result = calculate_bmr(height, weight, age, gender)
    return jsonify({'bmr': bmr_result}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
