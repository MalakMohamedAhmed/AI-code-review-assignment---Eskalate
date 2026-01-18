import math

# added this function for making sure that the "amount" is a numerical value, not a null, invaled, or any other thing
def is_numeric_string(value):
    try:
        float(value) # try converting it to a float, if it was converted successfully then it has a valied value
        if math.isnan(value) or math.isinf(value): # if the value is infinity or nan it should be ignored
            return False
        return True
    except (ValueError, TypeError): # otherwise we should throw an error
        return False

def average_valid_measurements(values):
    # in the begining we need to make sure that the 'values' paramter is a list or a tuple
    # to avoid any problems that could happen due to any invalid inputs, if not we need to stop the preocess
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple.")
        
    total_of_values = 0
    number_of_not_null_values = 0 # for counting the actual not null values
    total_number_of_values = len(values) # number of all the values

    if total_number_of_values == 0: # in case 'values' was completly empty
        print("There exists no values")
        return 0

    for value in values:
        if value is not None:
            if is_numeric_string(value): # in case the value weren't a valied thing
                number_of_not_null_values += 1
                total_of_values += float(value)

    if number_of_not_null_values == 0: # in case all the values were null
        print("All the values are null !!")
        return 0
    
    return round(total_of_values / number_of_not_null_values, 10) # in case we added many floates, to fix precision issues


# Some Test cases i used to make sure i handled all the edge cases i mentioned

# values = [10, None, 20, 30]
# values = []
# values = [None, None, None]
# values = [10, "abc", 20]
# values = [10, [1, 2], 20]
# values = [10, float('inf'), 20]
# values = [10, float('nan'), 20]
# values = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# values = "values"
# print(average_valid_measurements(values))
