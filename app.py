UNIT = "kg"
fields = []
harvests = []
sales = []

def add_field(name, area):
    fields.append({"name": name, "area": area})
    print(f"Maydon qo'shildi: {name}, {area} ga")

def list_fields():
    for i, f in enumerate(fields, 1):
        print(f"{i}. {f['name']} ({f['area']} ga)")

if __name__ == "__main__":
    list_fields()

add_field("Shimoliy dala", 12.5)

def record_harvest(field_name, amount):
    harvests.append({"field": field_name, "amount": amount, "unit": UNIT})
    print(f"Hosil qayd etildi: {field_name} - {amount} {UNIT}")

record_harvest("Shimoliy dala", 45.0)

def register_sale(product, amount, price):
    sales.append({"product": product, "amount": amount, "unit": UNIT, "price": price})
    print(f"Sotuv: {product}, {amount} {UNIT}, {price} so'm")

register_sale("Bug'doy", 10, 25000000)
