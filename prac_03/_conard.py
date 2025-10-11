import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
FILENAME = "stock_output.txt"
export_file=open(FILENAME,"w")
price = INITIAL_PRICE
day=0
print(f"${price:,.2f}", file=export_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day+=1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + price_change)
    print(f"On day {day} price is: ${price:,.2f}", file=export_file)
export_file.close()
