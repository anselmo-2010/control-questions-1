str_1 = "Aidana"
str_2 = "Adilet"

result =[]

for i in range(len(str_1)):
    result.append(str_1[i] + str_2[i])
    
joined_string = " ".join(result).replace(" ", "")    

print(joined_string)





