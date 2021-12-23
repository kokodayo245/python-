# 6-6
persons = ['a', 'b', 'c', 'd', 'e', 'f']
favorite_languages = {
    'a': 'python',
    'b': 'c',
    'c': 'java',
    'd': 'python'
    }
for name in persons:
    if name in favorite_languages.keys():
        print("Hi! " + name.title() + " Thank you for taking our poll.")
    else:
        print("Hi! " + name.title() + " Could you join us ？")
