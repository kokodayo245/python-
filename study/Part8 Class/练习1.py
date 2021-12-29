class Restaurant(object):
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        print("restaurant's name is " + self.restaurant_name)
        print("restaurant is a " + self.restaurant_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is opening")


my_restaurant = Restaurant('沙县小吃', '快餐店')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()