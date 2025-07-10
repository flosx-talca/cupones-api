from app.cupones import apply_cupon, calculate_final_price
def test_discount_sale10():
 assert apply_cupon(100, "SALES10") == 90.0
def test_discount_super20():
 assert apply_cupon(200, "SUPER20") == 160.0
def test_discount_welcome():
 assert apply_cupon(100, "WELCOME") == 85.0
def test_invalid_coupon():
  assert apply_cupon(990, "FAKE") == 990
def test_price_final_price_with_tax():
 assert calculate_final_price(100, "SALES10") == 107.1