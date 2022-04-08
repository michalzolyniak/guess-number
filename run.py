from functions.basic_functions import draw_number

if __name__ == '__main__':
    start = 1
    end = 100
    drawn_number = draw_number(start=1, end=100)
    while True:
        user_number = input(f"Guess the number between {start} and {end} : ")
        try:
            user_number = int(user_number)
        except ValueError:
            print("It's not a number!")
            continue
        if user_number == drawn_number:
            print("You win!")
            break
        elif user_number > drawn_number:
            print("To big")
        elif user_number < drawn_number:
            print("To small!")
