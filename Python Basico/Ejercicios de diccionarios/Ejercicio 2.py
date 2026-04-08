dict1 = {

}

list1 = ["first_name","last_name","role"]
list2 = ["Esteban","Araya","Software engineer"]

for index in range(len(list1)):
    dict1_key = list1[index]
    dict1_value = list2[index]
    dict1[dict1_key] = dict1_value

print(dict1)