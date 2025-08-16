from controller.simcard_controller import save
print("simcard view (gui)")

number = int(input("enter number"))
owner = input("enter owner")
register_data = input("enter register data")
operator = input("enter operator")
charge = int(input("enter charge"))
save(number,owner,register_data,operator,charge)