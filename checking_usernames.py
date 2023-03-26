current_users = ['evan', 'micah', 'james', 'admin', 'michele']
new_users = ['mark', 'john', 'chris', 'evan', 'micah']

for user in new_users:
    if user.lower() in current_users:
        print("This username is taken, please try again.")
    else:
        print("The username is available!")
