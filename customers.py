#reflections
#1: I would use .get() when I am not sure if a key exists because it prevents my code from crashing. I would use bracket notation when I know the key should be there. My rule of thumb is to use .get() when I am unsure and brackets when I am certain.
#2: This reminds me of using a PivotTable in Excel to organize and add up sales by region. Python can be more useful for large datasets because it can process information faster and automatically update totals without having to do everything manually.


print("--- exercise 1 ---")

customer = {
    "name": "Alice" ,
    "email": "alice@example.com" ,
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("--- exercise 2 ---")

customer['phone'] = '555-5555' # adding a new key value pair to the dictionary
print(customer)
customer['tier'] = 'platinum'
print(customer)
del customer['name']
print(customer)


print("--- exercise 3 ---")

print(customer.get('email', 'No email on file')) 
try:
    print(customer['email']) 
except KeyError as error:
    print("key error caught: ", error)

print("--- exercise 4 ---")

for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(f"{something}: {customer[something]}")    

print("--- exercise 5 ---")

tier_discounts = {
    "bronze": 0,
     "silver": 0.05, 
    "gold": 0.1,
     "platinum": 0.15}

purchase = 200
discount_rate = tier_discounts.get(customer['tier'], 0)
final_price = purchase * (1 - discount_rate)
print(f"tier: {customer['tier']}")
print(f"discount rate: {discount_rate * 100}")
print(f"final price: {final_price:.2f}")

print("--- exercise 6 ---")

for record in customer:
    rate = tier_discounts.get(record['tier'], 0)
    discount = 300 * rate
    print(f" {record['tier']}  {discount:.2f}) {record['name']})")

print("--- exercise 7 ---")

catalog = {
    "widget A": {"price": 9.99, "stock": 150},
    "gadget B": {"price": 49.99, "stock": 8}
}
for name, details in catalog.items():
    if details['stock'] < 20:
        print(f"LOW STOCK: {name} - only {details['stock']} left")

print("--- exercise 8 ---")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
