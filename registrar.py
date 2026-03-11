Sales = []
def Add_sale():
    product_name = input("What is the product name: ")
    try:
        unit_price = float(input("What is the product unit price: "))
        quantity_sold = int(input("What is the quantity sold: "))
    except ValueError:
        print("❌ Error: Please enter a valid number for price and quantity.")
        return # Sale de la función sin guardar nada roto
    total = quantity_sold * unit_price

    sale = {
        "product": product_name,
        "quantity": quantity_sold,
        "unit price": unit_price,
        "total": total
    }

    
    Sales.append(sale)
    print(f"\nPRODUCT {product_name} --- QUANTITY SOLD {quantity_sold}--- TOTAL ${total}")