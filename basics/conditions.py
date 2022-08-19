# Conditional statement for logical code branching
def run_conditional_code():
    """
    run conditional statements
    """
    state = False
    if state:
        print("State is not set")
    else:
        print("State is set")

    number = 1
    if number == 0:
        print('number is 0')
    elif number == 1:
        print('number is 1')
    else:
        print('number is not set')

    # Nested if conditions
    price = 100
    credit = 90

    if price > 0:
        if credit > 0:
            if credit >= price:
                credit = credit-price
                print('remaining credit', credit)
                print('Bought product')
            else:
                print('No credit avaialbe to buy')
        else:
            print('No credit to buy anything')
    else:
        print('No product available')

    # Using and
    # In and conditions all evaluations shoud be true, even single evaluation fails, it will not pass the condition.
    # condition and condition and condition | shoud be true and true and true
    if price > 0 and credit > 0:
        if credit >= price:
            credit = credit - price
            print('remaining credit', credit)
            print('Bought product')
        else:
            print('No credit avaialbe to buy')

    # Using or operator
    credit = 100
    crimial_record = True
    # (credit < 100 will become false) and criminal_record is true
    # In or condition if either of evaluation tends to true it will consider it to be true
    # and will go into the condition, and user is not eligible for loan
    if credit < 100 or crimial_record:
        print('Not eligible for loan')
    else:
        print('eligible')

    # Can also be written using not operator
    # Not before any evaluation like ( not True or not False) inverts it
    # (credit < 100 if false will invert to true) and (crimilal_record is true will invert to false)
    # result is if (true and true)
    # and only passes the condition if both evaluation is true
    if not credit < 100 and not crimial_record:
        print('eligible')
    else:
        print('Not eligible for loan')

