def greet_user():
    print("Hello!")


greet_user()


# 形参和实参 ，形参可指定默认值
def describe_pet(pet_name, animal_type='cat'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('Willie', 'dog')
describe_pet('ace',)
describe_pet(pet_name='banana', animal_type='fish')

