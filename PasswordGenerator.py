#Password generator project
# 1- Import string and random modules
import string
import random
# 2- store all characters in lists (upper/ lower case, digits, punctuations)
# s1 = list(string.ascii_lowercase) -> other way
# s2 = list(string.ascii_uppercase) -> other way
# s3 = list(string.digits) -> other way
# s4 = list(string.punctuation) -> other way
# 3- Take the number of characters from the user
char_pass = input("Enter how many characters for your new password?:")
# 4- Check that the user entered only integers and >= 10
while True:
     try:
         char_pass =int(char_pass)
         if char_pass < 10:
             print("A strong password consists of at least 10 characters!")
             char_pass = input("Please, try again and enter the number of characters: ")
         else:
             break
     except:
         print("Please enter numbers ONLY!")
         char_pass = input("Enter how many characters for your new password?:")
# 5- Shuffle all lists
random.shuffle(list(string.ascii_lowercase));
random.shuffle(list(string.ascii_uppercase));
random.shuffle(list(string.digits));
random.shuffle(list(string.punctuation));
# 6- Calculate 30% and 20% of number of characters
# p1 = round(char_pass * (30/100)) -> other way
# p2= round(char_pass * (20/100)) -> other way
# 7- create password 60% letters and 40% digits and punctuations
FinalPassword = []
for i in range(round(char_pass * (30/100))):
    FinalPassword.append(list(string.ascii_lowercase)[i])
    FinalPassword.append(list(string.ascii_uppercase)[i])
for i in range(round(char_pass * (20/100))):
    FinalPassword.append(list(string.digits)[i])
    FinalPassword.append(list(string.punctuation)[i])

# 8- Final touches on the password and displaying it
random.shuffle(FinalPassword)
FinalPassword = "".join(FinalPassword[0:])
print(FinalPassword)
#-----------------------------------------------------------------------------------------------------------------------
