

def limit(user_input, user_equation):
    if user_input == 'infinity':
        count = 0
        numerate = []
        top = []
        equation_list = list(user_equation)

        for i in range(len(equation_list)):
            if equation_list[i] == '/':
                top.append(''.join(numerate))
                numerate = []
            else:
                numerate.append(equation_list[i])

        count = 0
        for value in numerate:
            if value == 'X':
                numerate[count] = '1'
            count += 1
            print(value)

        counter = 0
        for digit in top:
            if digit == 'X':
                top[counter] = '1'

            counter += 1


        numerate_string = ''.join(numerate)
        numerate_string = numerate_string.replace('X', '1')


        top_string = ''.join(top)
        top_string = top_string.replace('X', '1')

        if int(numerate_string) > int(top_string):
            return '0 is the limit, \nas X approaches ' + user_input
        else:
            if int(top_string) < 0:
                return 'Negative Infinity is the limit, \nas X approaches ' + user_input
            else:
                return 'Infinity is the limit, \nas X approaches ' + user_input
            # There are lots more things I need to make sure so that its negative and positive
            # on both sides of a number line.

    elif user_input == 'negative infinity':
        count = 0
        numerate = []
        top = []
        equation_list = list(user_equation)

        for i in range(len(equation_list)):
            if equation_list[i] == '/':
                top.append(''.join(numerate))
                numerate = []
            else:
                numerate.append(equation_list[i])

        count = 0
        for value in numerate:
            if value == 'X':
                numerate[count] = '1'
            count += 1
            print(value)

        counter = 0
        for digit in top:
            if digit == 'X':
                top[counter] = '1'

            counter += 1

        numerate_string = ''.join(numerate)
        numerate_string = numerate_string.replace('X', '1')

        top_string = ''.join(top)
        top_string = top_string.replace('X', '1')

        if int(numerate_string) > int(top_string):
            return '0 is the limit, \nas X approaches ' + user_input
        else:
            if int(top_string) < 0:
                return 'Negative Infinity is the limit, \nas X approaches ' + user_input
            else:
                return 'Infinity is the limit, \nas X approaches ' + user_input
            # There are lots more things I need to make sure so that its negative and positive
            # on both sides of a number line.
    else:
        try:
            equation_list = list(user_equation)
            for i in range(len(equation_list)):
                if equation_list[i] == 'X':
                    equation_list[i] = user_input



                else:
                    continue
            print(equation_list)
            # ['(', '3', '*', '2', ')', '/', '2']



            equation_string = ''.join(equation_list)
            result = float(eval(equation_string))
            return str(result) + ' is the limit, \nas X approaches ' + user_input

        except ZeroDivisionError:
            print('equation can not be divible by zero \n Find the derivative of the bottom and top parts of the function and try again')
        except NameError:
            print('Please type in a number or special cases shown in the example')


user_input = input('When does X approach the following equation? \n Examples: \n 0 \n \
infinity \n negative infinity \n as x -> ')

user_equation = input('What is the equation you need to solve? Use X as the limit. \n Examples: \n \
(3*X)/X \n sqrt(X**2) \n -> Y = ')
print(limit(user_input, user_equation))