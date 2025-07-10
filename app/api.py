from flask import Flask, request, jsonify

from app.cupones import calculate_final_price

app = Flask(__name__)
@app.route('/price', methods=['POST'])
def calcute():
	data = request.get_json()
	price = data.get("price")
	cupon = data.get("cupon")
	tax_rate = data.get("tax_rate", 0.19)
	final_price = calculate_final_price(price, cupon, tax_rate)
	return jsonify({"final_price": final_price})
