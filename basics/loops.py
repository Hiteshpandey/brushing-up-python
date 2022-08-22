# loops are used for iterative operations. Usually when we need to repeat an opeartions n number of times

def looping_operations():
    i = 1
    # until i <= 5
    while i <= 5:
        # print i
        print(i)
        # increment i
        i = 1 + 1
    print(i)

def guessing_game():
    number = 9
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = input("enter guess number: ")
        if int(guess) == number:
            print("Correct")
            break;
        else:
            print("wrong guess try again")
            guess_count += 1
    # While loop can also have else condition
    # That means, if the while loop is completely exhausted, or completed.
    # i.e user never guesses the answer.
    # This condition is ran
    else:
        print("number of guesses exhausted")

def list_iteration:
    ll = [1, 2, 3, 4, 5]

    # Iterating directly by acquiring elements directly
    # This iterates over elements on by one
    for i in ll:
        print(ll)
    

    # Print 0 to 9
    for i in range(10):
        print(i)
    # Iterating index wise
    # range provised us incremental step by step index of the list
    # we can use the index of [1,2,3,4] as index [0,1,2,3]
    # so ll[0] ll[1]
    # if range is given number 10 it will iterate from 0 to 9
    for i in range(len(ll)):
        print(ll[i])


guessing_game()