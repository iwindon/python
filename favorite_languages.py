favorite_languages = {
    'jen': ['python'],
    'ivan': ['c++', 'python', 'swift'],
    'sarah': ['c'],
    'edward': ['rust'],
    'phil': ['python'],
    'evan': ['python'],
}

friends = ['sarah', 'evan']


#for key, value in favorite_languages.items():
#    print(f"{key.title()}'s favorite programming langauage is {value.title()}")

for name, langauges in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in langauges:
        print(f"\t{language.title()}")

#for name in sorted(favorite_languages.keys()):
#    print(name.title())
#    if name in friends:
#        language = favorite_languages[name].title()
#        print(f"\t{name.title()}, I see you love {language}!")
#if 'erin' not in favorite_languages.keys():
#    print("Erin, please take our poll.")

#print("\n\nThe following languages have been mentioned:")
#for langauge in sorted(set(favorite_languages.values())):
#    print(langauge.title())

    