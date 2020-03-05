# Nest data structures
crazy_landl_1 = {
    'name': 'Boris',
    'phone': '09875656789',
    'address_of_rent': '10 Chelsea',
    'age': 55

}
crazzy_landl_2 = {
    'name': 'Filipe',
    'phone': '035192747489',
    'address_of_rent': 'Comporta, Portugal',
    'age': 28

}
nested_dictionary = {'boris': crazy_landl_1,
                     'Filipe': crazzy_landl_2
}
print(nested_dictionary)
for key in nested_dictionary:
    print(key)
    for nest_key in nested_dictionary[key]:
        print(nest_key, nested_dictionary[key][nest_key])

# for key in nested_dictionary:
#     print(key)
#     data_nested = nested_dictionary[key]
#     print(data_nested)
#     breakpoint()
#     # print(type(data_nested))
#     # print(data_nested.keys())
#     print(data_nested['name'])
#     print(data_nested['address_of_rent'])


nest_list = [[1, 2, 3], [4, 5, 6]]
print(nest_list[0])
print(nest_list[1])
print(nest_list[1][0])

for data in nest_list:
    print(data)
    breakpoint()
    for num in data:
        print(num * 20)
