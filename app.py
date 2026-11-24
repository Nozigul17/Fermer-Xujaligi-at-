UNIT = "tonna"
fields = []
harvests = []
sales = []

def list_fields():
    for i, f in enumerate(fields, 1):
        print(f"{i}. {f['name']} ({f['area']} ga)")

if __name__ == "__main__":
    list_fields()
