UNIT = "tonna"
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
