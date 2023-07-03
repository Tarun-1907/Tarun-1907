import random
import string
import array

max_len = 10

digit = string.digits
spe_char = string.punctuation
ALPHABETS = string.ascii_letters

passw = digit+spe_char+ALPHABETS

ran_digi = random.choice(digit)
ran_spe_char = random.choice(spe_char)
ran_ALPHABETS_U = random.choice(ALPHABETS)

passwor = ran_digi+ran_spe_char+ran_ALPHABETS_U

for i in range(max_len-5):
    passwor += random.choice(passw)

    p = array.array('u', passwor)
    random.shuffle(p)

password = ''
for i in p:
    password +=i
    
print("\n")
print("\t \t \t \t  | STRONG PASSWORD GENERATOR | \t \t \t \t")
print("Here is your password:- \n")
print(password)
print("Don't share it with anyone !!!!!")