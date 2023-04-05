<<<<<<< HEAD
import random
import array

max_len = 12
lowercase_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digit_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_array = ['!', '@', '#', '$', '%', '^', '&', '*']

combined_list = lowercase_array + uppercase_array + digit_array + symbols_array

choose_digit = random.choice(digit_array)
choose_uppercase = random.choice(uppercase_array)
choose_lowercase = random.choice(lowercase_array)
choose_symbols = random.choice(symbols_array)

temp_pas = choose_digit + choose_uppercase + choose_symbols + choose_lowercase

for x in range(max_len-4):
    temp_pas =temp_pas + random.choice(combined_list)
    pas_array = array.array('u', temp_pas)
    random.shuffle(pas_array)

password = ""

for x in pas_array:
      password += x
print(password)
print(pas_array.typecode)
=======
import random
import array

max_len = 12
lowercase_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digit_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_array = ['!', '@', '#', '$', '%', '^', '&', '*']

combined_list = lowercase_array + uppercase_array + digit_array + symbols_array

choose_digit = random.choice(digit_array)
choose_uppercase = random.choice(uppercase_array)
choose_lowercase = random.choice(lowercase_array)
choose_symbols = random.choice(symbols_array)

temp_pas = choose_digit + choose_uppercase + choose_symbols + choose_lowercase

for x in range(max_len-4):
    temp_pas =temp_pas + random.choice(combined_list)
    pas_array = array.array('u', temp_pas)
    random.shuffle(pas_array)

password = ""

for x in pas_array:
      password += x
print(password)
print(pas_array.typecode)
>>>>>>> c9620fbf3a4515d86fcebd2f69f58b69fe37309f
