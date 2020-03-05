Main_menu = ['chicken Wrap', 'falafel', 'hummus', 'burger', 'pizza', 'soda']
Menu = []
Order =[]
print(Main_menu[0].capitalize())
print(Main_menu[1].capitalize())
print(Main_menu[2].capitalize())
print(Main_menu[3].capitalize())
print(Main_menu[4].capitalize())
print(Main_menu[5].capitalize())

print(f"Here is your  menu: {Menu}")

order_count = 3
while order_count != 0:
    if order_count == 3:
        Order.append(input(f'What would you like to order? '))
    order_count -= 1
    continue
else:
    Order.append(input(f'Anything else you want? '))
order_count -= 1

print(f"your food order:{Order}")
