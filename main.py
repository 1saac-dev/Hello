calc_to_unit = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calc_to_unit} {name_of_unit}"
    else:
        return "Please, enter a positive number."


user_input = input("Hey user, enter a number of days.\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)
