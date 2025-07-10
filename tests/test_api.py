def apply_cupon(price, cupon):
	discounts = {
		"SALES10": 0.10,
		"SUPER20": 0.20
		# El cupon "BIENVENIDA" se eliminó sin querer
	}
	if cupon in discounts:
		return round(price * (1 - discounts[cupon]), 2)
	return price