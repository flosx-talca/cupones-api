def apply_cupon(price, cupon):
	discounts = {
		"SALES10": 0.10,
		"SUPER20": 0.20,
		"WELCOME": 0.15
	}
	if cupon in discounts:
		return round(price * (1 - discounts[cupon]), 2)
	return price

def calculate_final_price(base_price, cupon, tax_rate=0.19):
	price_desc = apply_cupon(base_price, cupon)
	return round(price_desc * (1 + tax_rate), 2)