# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(name):
    return name["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]

def add_or_remove_cash(cash, amount):
    cash["admin"]["total_cash"] += amount
    return cash["admin"]["total_cash"]

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(number, increase):
    number["admin"]["pets_sold"] += increase
    return number["admin"]["pets_sold"]

def get_stock_count(shop_name):
    return len(shop_name["pets"])

def get_pets_by_breed(shop_name, breed):
    pet_by_breed = []
    for pet in shop_name["pets"]:
        if pet["breed"] == breed:
            pet_by_breed.append(pet)
    return pet_by_breed
    
def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet
    else:
        return None

def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            pet["name"] = None

def add_pet_to_stock(shop, pet):
    shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount
    return customer["cash"]

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(shop, pet):
    if shop["cash"] >= pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(shop, pet, customer):
    if (pet != None) and (customer_can_afford_pet(customer, pet) == True):
        add_pet_to_customer(customer, pet)
        increase_pets_sold(shop, 1)
        remove_pet_by_name(shop, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(shop, pet["price"])


        