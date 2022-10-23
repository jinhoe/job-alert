import re



txt = "6 Year Exp"



# x = re.match(r"^\S*", txt)
#
# my_str = int(x.group())
#
# print(my_str)


#x = re.match(r"^\S*", txt)

#my_str = int(re.match(r"^\S*", txt).group())

print(int(re.match(r"^\S*", txt).group()))