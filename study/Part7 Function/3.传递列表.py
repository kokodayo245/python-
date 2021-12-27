def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'try', 'margot']
greet_users(usernames)


# 在函数中修改列表


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# print_models(unprinted_designs[:], completed_models) 使用unprinted_designs[:]并不会影响unprinted_designs本身只是使用了副本
# 若直接使用unprinted_designs则会影响本身 ，若打印unprinted_designs可发现其已被清空
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)