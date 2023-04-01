def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
car = make_car('subaru', 'STI', color = 'black', custom_rims = True)
print(car)
car = make_car('honda', 'civic', color='red', transmission = 'manual')
print(car)
