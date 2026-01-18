# added this function for making sure that the "amount" is a numerical value, not a null, invaled, or any other thing
def is_numeric_string(s):
    try:
        float(s) # try converting it to a float, if it was converted successfully then it has a valied value
        return True
    except (ValueError, TypeError): # otherwise we should throw an error
        return False
    

def calculate_average_order_value(orders):
    total_value = 0
    number_of_not_cancelled_orders = 0 # we need to keep track of number of orders that are not cancelled
    total_number_of_orders = len(orders)

    if total_number_of_orders == 0: # in case 'orders' was completly empty
        print("We have no orders !!")
        return 0
        
    for order in orders:
        if "status" in order and "amount" in order: # if we received the input without either of the two main attributes "status" and "amount"
            if order["status"] != "cancelled":
                amount_str = str(order["amount"])
                if is_numeric_string(amount_str): # to handle if the 'amount' attribute has an invalied value
                    number_of_not_cancelled_orders += 1
                    total_value += float(order["amount"]) # in case we received the 'amount' as a string

    if number_of_not_cancelled_orders == 0: # in case all the orders were cancelled
        print("All orders were cancelled !!") # need to send an alert in this case
        return 0
    
    return total_value / number_of_not_cancelled_orders # then divide by the number of orders that weren't cancelled


# Some Test cases i used to make sure i handled all the edge cases i mentioned

# orders = [
#     {"status": "completed", "amount": 100},
#     {"status": "cancelled", "amount": 50},
#     {"status": "completed", "amount": 200}
# ]
# orders = [
#     {"status": "cancelled", "amount": 100},
#     {"status": "cancelled", "amount": 200}
# ]
# orders = []
# orders = [
#     {"status": "completed", "amount": 100},  # Valid
#     {"amount": 200},  # Missing "status" key
#     {"status": "completed"}  # Missing "amount" key
# ]
# orders = [
#     {"status": "completed", "amount": 100},  # Valid
#     {"status": "completed", "amount": "invalid"}  # "amount" is a string, not numeric
# ]

# print(calculate_average_order_value(orders))

