from functions.draw_number import draw_number

if __name__ == '__main__':
    START = 1
    END = 100
    drawn_number = draw_number(start=START, end=END)
    while True:
        user_number = input(f"Guess the number between {START} and {END} : ")
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
