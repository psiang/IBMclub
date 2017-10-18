class goods(object):
    def __init__(self, number, name, price):
        self.name = name
        self.number = number
        self.price = price
    def print(self):
        print("GoodInformation:",self.number,self.name,self.price)

numbers = {}
names = {}
total = 0
print("!!!!! Welcome to Siang's Shoppingsystem !!!!!\n")
while 1>0:
    print("1.Input Commodity")
    print("2.Query Commodity")
    print("3.Delete Commodity")
    print("4.Checkout the Bill")
    print("5.Save Commodities List")
    print("6.Load Commodities List")
    print("7.Show the Commodities List")
    print("8.Exit")
    op = input("Please select your operation：")
    print("")

    if op == "1":
        print("Please enter the number, name and price of the goods:")
        number = input("Number:")
        name = input("Name:")
        price = int(input("Price:"))
        total += 1
        good = goods(number, name, price)
        numbers[number] = good
        names[name] = good
        print("The commodity has been successfully entered!\n")

    elif op == "2":
        print("1.Number")
        print("2.Name")
        op2 = input("Known number or name?")
        if op2 == "1":
            number = input("Number:")
            if (number in numbers):
                numbers[number].print()
            else:
                print("No such commodity")
            print("")
        elif op2 == "2":
            name = input("Name:")
            if (name in names):
                names[name].print()
            else:
                print("No such commodity")
            print("")
        else:
            print("Invalid Input\n")

    elif op == "3":
        print("1.Number")
        print("2.Name")
        op2 = input("Known number or name?")
        if op2 == "1":
            number = input("Number:")
            if number in numbers:
                del names[numbers[number].name]
                del numbers[number]
                total -= 1
                print("The commodity have been deleted!")
            else:
                print("No such commodity")
            print("")
        elif op2 == "2":
            name = input("Name:")
            if name in names:
                del numbers[names[name].number]
                del names[name]
                total -= 1
                print("The commodity have been deleted!")
            else:
                print("No such commodity")
            print("")
        else:
            print("Invalid Input\n")

    elif op == "4":
        num = int(input("How many commodities are needed to buy?"))
        print("Please enter the number of the goods and the quantity purchased:")
        i = 1
        count = 0
        temp = {}
        while i <= num:
            print("No.", i)
            number = input("Number:")
            quantity = int(input("Quantity:"))
            temp[number] = quantity
            count += quantity * numbers[number].price
            i += 1
        print("Total: ", count)
        print("")
        print("1.Yes")
        print("2.No")
        op2 = input("Do you need to print a receipt?")
        if op2 == "1":
            with open('Receipt.txt', 'w') as f:
                f.write("Number" + "\t" + "Name" + "\t" + "Price" + "\t" + "Quantity" + "\n")
                for x in temp:
                    f.write(str(x) + "\t" + numbers[x].name + "\t" + str(numbers[x].price) + "\t" + str(temp[x]) + "\n")
                f.write("Total: " + str(count) + "\n")
        print("Receipt has been printed!\n")

    elif op == "5":
        with open('Commodities.txt', 'w') as f:
            f.write(str(total) + "\n")
            for x in numbers:
                f.write(x + "\n")
                f.write(numbers[x].name + "\n")
                f.write(str(numbers[x].price) + "\n")
        print("The list of Commodities has been saved!\n")

    elif op == "6":
        with open('Commodities.txt', 'r') as f:
            tmp = f.readline()
            num = int(tmp[0:-1])
            i = 1
            while i <= num:
                number = f.readline()
                number = number[0:-1]
                name = f.readline()
                name = name[0:-1]
                tmp = f.readline()
                price = int(tmp[0:-1])
                total += 1
                good = goods(number, name, price)
                numbers[number] = good
                names[name] = good
                i += 1
        print("The commodities list was successfully imported!\n")

    elif op == "7":
        print("Number" + "\t" + "Name" + "\t" + "Price")
        for x in numbers:
            print(str(x) + "\t" + numbers[x].name + "\t" + str(numbers[x].price))
        print("")

    else:
        break