full_name = 'Liel Morim'

full_name_as_upper = full_name.upper()
length = len(full_name)
index = full_name.index(" ")
first_name = full_name[0:index]
last_name = full_name[index + 1:]
first_name_v1 = full_name[:index]
last_name_v1 = full_name[index + 1:]

price = " 111 $"

price = price.replace("$", "ILS")
count = price.count("1")
price_no_space = price.strip()
# Removes spaces only at the edges (at the beginning/end)

# Casting example -  Replace integer to string or the other way around

num1 = 21
num2 = 1
counter = num1 + num2
counter_as_str = str(counter)  # convert from integer to string

num_as_str = "7"
num_as_int = int(num_as_str)  # convert from string to integer

print("Test End")
