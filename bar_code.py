import barcode
from barcode import Code128
def generate_barcode(data):
    code=Code128(data)
    code.save("Barcode.png")
    print("Barcode saved to file")

data=input("Enter the data you want to generate barcode for:: ")
generate_barcode(data)
