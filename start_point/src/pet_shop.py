# WRITE YOUR FUNCTIONS HERE
# 1
def get_pet_shop_name(shop_name):
    return shop_name["name"] 
# 2
def get_total_cash(shop_cash):
    return shop_cash["admin"]["total_cash"]
# 3 and 4
def add_or_remove_cash(total, plus_ten): 
    total["admin"]["total_cash"] += plus_ten
    return plus_ten
# 5
def get_pets_sold(shop):
    num_of_sold = shop["admin"]["pets_sold"]
    return num_of_sold
# 6
def increase_pets_sold(shop, two):
    shop["admin"]["pets_sold"] += two
# 7
def get_stock_count(num_of_animals):
    stock_add = len(num_of_animals["pets"])
    return stock_add
# 8 # 
def get_pets_by_breed(shops, animal):
    for shop in shops["pets"]:
        if shop["breed"] == animal:
            return shop, animal












# 9




def find_pet_by_name(shops, dogs_name):

    for shop in shops["pets"]:
        if shop["name"] == dogs_name:
            return shop
# 10
def find_pet_by_name(shops, dogs_name):
    for shop in shops["pets"]:
        if shop["name"] == dogs_name:
            return shop
# 11
def remove_pet_by_name(shops, dogs_name):
    for shop in shops["pets"]:
        if shop["name"] == dogs_name:
            shops["pets"].remove(shop)

# 13 
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
# 14
def get_customer_cash(customer):
    customer_cash = customer["cash"]
    return customer_cash
# 15
def remove_customer_cash(person, bill):
    person["cash"] -= bill
# 16
def get_customer_pet_count(customer):
    no_pets = len(customer["pets"])
    return no_pets
# 17
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)









