products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code,property):
    return products[code][property]

def main():
    receipt = []
    orderlist = []
    while(True):
        order = input("Input order:").split(",")
        if(order == ["/"]):
            break
        elif(not(order[0] in products)):
            print("Invalid order.")
            continue
        elif(order[0] in orderlist):
            order[1] = int(order[1])
            receipt[orderlist.index(order[0])][1] = int(receipt[orderlist.index(order[0])][1]) + order[1]
        else:
            order[1] = int(order[1])
            orderlist.append(order[0])
            receipt.append(order)
    receipt.sort()
    with open("receipt.txt", "w") as r:
        r.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL''')
        total = 0
        for i in range(len(receipt)):
            code = receipt[i][0]
            name = get_property(receipt[i][0],"name")
            quantity = receipt[i][1]
            subtotal = get_property(receipt[i][0],"price")*quantity
            total += subtotal
            if(len(name) < 8):
                r.write(f'''
{code}\t\t\t{name}\t\t\t{quantity}\t\t\t\t\t{subtotal}''')
            elif(len(name) > 11):
                r.write(f'''
{code}\t{name}\t{quantity}\t\t\t\t\t{subtotal}''')
            else:
                r.write(f'''
{code}\t\t{name}\t\t{quantity}\t\t\t\t\t{subtotal}''')
        r.write(f'''

Total:\t\t\t\t\t\t\t\t\t\t\t\t{total}
==
        ''')

    
main()