users: list = [
    {'name': 'Julia', 'location': 'Ząbki', 'posts': 10},

]

print(users)

def add_user(users_data: list)->None:

    new_name:str = input('Podaj imię nowego znajomego: ')
    new_location:str = input ('Podaj nazwe lokalizacji:')
    new_posts:int = int(input('Podaj liczbę postów:'))
    users.append( {'name': new_name, 'location': new_location, 'posts': new_posts} ,)


add_user(users)
print(users)