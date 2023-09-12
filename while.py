x = 1
while x < 5:
    print('*' * x)
    x += 1
print('done')

secret_no = 20
no_of_gues = 1
gues_limit = 4
while no_of_gues < gues_limit:
    gues = int(input('gues: '))
    no_of_gues += 1
    if int(gues) == secret_no:
        print("correct")
        print("Your guessing is correct")
        break
    else:
        print('incorrect')
        print('Sorry, your guessing didn"t match.')

started = False
while True:
    command = input('> ').lower()
    if command == "start":
        if started:
            print("car is already started...")
        else:
            started = True
            print('car started..')
    elif command == "stop":
        if not started:
            print('the car is already stopped.')
        else:
            started = False
            print('car stopped')
    elif command == "help":
            print("""
start - to start to car
stop - to stiop the car
quit - to quit
""")
    elif command == "quit":
        break

    else:
        print('sorry, i do not understand')
        break



