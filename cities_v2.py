def describe_city(city, country = 'United States'):
    if country == 'United States':
        print(f"{city} is in the {country}.")
    else:
        print(f"{city} is in {country}.")

describe_city('San Francisco')
describe_city('Paris', 'France')
describe_city('Boston')
