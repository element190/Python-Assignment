inch_str = input("type the amount of rain in inches on the acre: ")

acres_str = input("enter how many acres: ")
acres_int = int(acres_str)

gallons= 6272640*acres_int / 231

print("There are ",gallons,"gallons of water on",acres_int,"acres of land")