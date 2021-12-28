# *toppings中的 '*' 让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参
# **user_info中 '**' 让Python创建一个名为user_info的空字典，并将收到的所有键——值对都封装到这个字典中
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
