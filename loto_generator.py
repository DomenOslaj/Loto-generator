import random


def main():
    print "Welcome to the Lottery numbers generator."

    quantity_question = raw_input("Please enter how many random numbers would you like to have: ")

    quantity_num = int(quantity_question)               #quantity_question is a string - raw_input
    print generate_random_numbers(quantity_num)


def generate_random_numbers(quantity):
    lottery_list = []

    while True:
        if len(lottery_list) == quantity:      # when the length of the list reaches the desired quantity, stop choosing new numbers
            break

        lot_num = random.randint(0, 50)

        if lot_num not in lottery_list:          # if the chosen number is not in the list yet, add it to it (this helps avoiding duplicates)
            lottery_list.append(lot_num)

    return lottery_list


if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    main()