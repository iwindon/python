from restaurant import Restaurant

my_restaurant = Restaurant("The Pizza Place", "Italian")
my_restaurant.describe()
my_restaurant.open()
my_restaurant.read_number_served()
my_restaurant.set_number_served(10)
my_restaurant.read_number_served()
my_restaurant.increment_number_served(5)
my_restaurant.read_number_served()
my_restaurant.increment_number_served(-5)
my_restaurant.read_number_served()
my_restaurant.set_number_served(5)
my_restaurant.read_number_served()
