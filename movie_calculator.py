# movie night calculator

def calculate_ticket_price(age, is_student):

    if age < 12:
        ticket_price = 5
    elif age <= 60:
        ticket_price = 10
    else:
        ticket_price = 7

    if is_student == 'yes':
        ticket_price -= 2

    return ticket_price


def calculate_snacks_cost(popcorn_price, drinks_price, candy_price):
    total = popcorn_price + drinks_price + candy_price
    return total


def main():
    print('*** Welcome to movie night calculator ***')

   

    age = int(input('Please enter your age: '))

    while True:
        is_student = input('Are you a student? (yes/no): ').strip().lower()
        if is_student in ['yes', 'no']:
            break
        else:
            print('Please enter yes or no.')

    popcorn = float(input('Popcorn price: '))
    drink = float(input('Drink price: '))
    candy = float(input('Candy price: '))

    ticket = calculate_ticket_price(age, is_student)
    snacks = calculate_snacks_cost(popcorn, drink, candy)

    total = ticket + snacks

    print('Ticket price:', ticket)
    print('Snacks price:', snacks)
    print('Your total expenses are: $' , total )

movie_name = input('Enter a movie name:\n')

main()

print('Your movie:' , movie_name)
print('Enjoy your movie!')

