Sales = []
def Add_sale():
    product_name = input("What is the product name: ")
    unit_price = float(input("What is the product unit price: "))
    quantity_sold = int(input("What is the quantity sold: "))
    total = quantity_sold * unit_price

    sale = {
        "product": product_name,
        "quantity": quantity_sold,
        "unit price": unit_price,
        "total": total
    }

    
    Sales.append(sale)
    print(f"\nPRODUCT {product_name} --- QUANTITY SOLD {quantity_sold}--- TOTAL ${total}")