class User:

    def __init__(self, first_name, last_name, location, title) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.title = title
    
    def describe_user(self):
        print("\nUser Details")
        print(f"Users Full name: {self.first_name} {self.last_name}")
        print(f"Location: {self.location}")
        print(f"Title: {self.title}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} from {self.location}.  How are you today?")

user001 = User("Ivan", "Windon", "South Carolina", "Lead DevOps Engineer")
user002 = User("Evan", "Windon", "South Carolina", "Student")
user003 = User("Michele", "Windon", "South Carolina", "Sales Manager")

user001.describe_user()
user001.greet_user()

user002.describe_user()
user002.greet_user()

user003.describe_user()
user003.greet_user()
    