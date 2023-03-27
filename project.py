name = input('Name Please! : ')
name1 = name.upper()
print('Hello', name, "My name is 3A's alexa")
if name1[0] == 'A':
    print('💥⭕ You are so deremined , having so much patient , open minded and Practical person 😁')
if name1[0] == 'R':
    print('💥⭕ You are so virtuous, powerful, pleasant and child lover 😊')
print("What do you want's from me ? ")
print(''' 
          1. Interest based Questions 
          2. Calculation Helping Agent ''')
n1 = int(input('Enter the no. as shown in above table ☝️'))
if n1 == 1:
    print(''' What are you interested in ?

              1. Cricket 🏏
              2. Football ⚽''')
    n2 = int(input('Enter the no. as shown in above table ☝️'))
    if n2 == 1:
        print("WELCOME TO Cricket Knowledge Testing")

        positive_score = 0
        total_point = (positive_score)

        print('ok', name, "Lets START ")
        Ques1 = print("1: Which measurement in cricket has remained unchanged since 1744?")
        options = print("(a): Bat's rule\n(b): Ball\n(c): Helmate\n(d): Yard")
        answer_1 = input("The correct answer for First question is  *", ).lower()
        if answer_1 == 'd':
            positive_score = positive_score + 2
            print("correct,you get 2 points")
        else:
            print("incorrect answer, don't worry attempt next one ")

        Ques2 = print("2: Till 1889 how many balls an over used to be bowled?")
        options = print("(a): 3\n (b): 4\n (c): 5\n (d): 6 ")
        answer_2 = input("The correct answer for this question is  *", ).lower()
        if answer_2 == 'b':

            positive_score = positive_score + 2

            print("correct,you get 2 points")
        else:

            print("incorrect answer,don't worry attempt next one ")

        Ques3 = print("3. When was overarm bowling accepted as legal? ")
        options = print("(a): 1947\n (b): 1911\n (c): 1860\n (d): 1864 ")
        answer_3 = input("The correct answer for this question is  *", ).lower()
        if answer_3 == 'd':

            positive_score = positive_score + 2
            print("correct,you get 2 points")
        else:
            print("incorrect answer,don't worry attempt next one ")

        Ques4 = print("4: Who is the first indian player to score century in IPL ")
        options = print("(a): Manish Pandey\n (b): Rohit Sharma\n (c): Gautam Gambhir\n (d): Brendon Mccullum")
        answer_4 = input("The correct answer for this question is  *", ).lower()
        if answer_4 == 'a':

            positive_score = positive_score + 2
            print("correct,you get 2 points")
        else:
            print("incorrect answer, don't worry attempt next one ")

        Ques5 = print("5: Name the Player who scoring highest run in one match of ODI format ")
        options = print("(a): Manish Pandey\n (b): Rohit Sharma\n (c): Gautam Gambhir\n (d): Brendon Mccullum")
        answer_5 = input("The correct answer for this question is  *", ).lower()
        if answer_5 == 'b':

            positive_score = positive_score + 2
            print("correct,you get 2 points")
        else:
            print("incorrect answer")

    if n2 == 2:
        print("WELCOME TO Football Knowledge Testing")

        positive_score = 0
        total_point = (positive_score)

        print('ok', name, "Lets START ")
        Ques1 = print("1: Which of the following country hosted the first Football World Cup?")
        options = print("(a): Argentina\n(b): India\n(c): Brazil\n(d): Uruguay")
        answer_1 = input("The correct answer for First question is  *", ).lower()
        if answer_1 == 'd':
            positive_score = positive_score + 2
            print("correct,you get 2 points")
        else:
            print("incorrect answer, don't worry attempt next one ")

        Ques2 = print("2: Which country became the first nation to win the Football World Cup?")
        options = print("(a): Uruguay\n (b):Argentina\n (c): India\n (d): America ")
        answer_2 = input("The correct answer for this question is  *", ).lower()
        if answer_2 == 'a':

            positive_score = positive_score + 2

            print("correct,you get 2 points")
        else:

            print("incorrect answer,don't worry attempt next one ")

        Ques3 = print("3. which of the following country won Football world Cup maximum times? ")
        options = print("(a): Uganda\n (b): Argentina\n (c): Germany\n (d): Brazil ")
        answer_3 = input("The correct answer for this question is  *", ).lower()
        if answer_3 == 'd':

            positive_score = positive_score + 2
            print("correct,you get 2 points")
        else:
            print("incorrect answer,don't worry attempt next one ")

        Ques4 = print("4: How many minutes are usually played in a football match ")
        options = print("(a): 90\n (b): 120\n (c): 50\n (d): 200")
        answer_4 = input("The correct answer for this question is  *", ).lower()
        if answer_4 == 'a':

            positive_score = positive_score + 2
            print("correct,you get 2 points")
        else:
            print("incorrect answer, don't worry attempt next one ")

        Ques5 = print("5: What is the usual lenght of time allowed for half time in football match ")
        options = print("(a): 20 minutes\n (b): 15 minutes\n (c): 10 minutes\n (d): 30 minutes")
        answer_5 = input("The correct answer for this question is  *", ).lower()
        if answer_5 == 'b':

            positive_score = positive_score + 2
            print("correct,you get 2 points")
        else:
            print("incorrect answer")

    print("Total number of question is 5:")
    print("Max Score : 10")
    print("YOUR SCORE IS:", positive_score, '/10')
    print("Your Percentage : ", (positive_score / 10) * 100, '%')

if n1 == 2:
    print(''' 
          1. Reverse the word :
          2. Check palindrome :
          3. Check the prime no. :
          4. Factorial of the number :
          5. Average of a no. :
          6. Sum of the no. :
          7. Substraction of the no. :
          8. Intresting facts :''')

    n = int(input('Enter the number as shown above ☝️: '))

    if n == 1:
        str1 = input("Give me a word for reversing : ")
        print(str1[::-1])

    if n == 2:
        str2 = input('Give me a word : ')
        if str2[::-1] == str2:
            print('Yes , The given word is having Palindrome ✌️')
        else:
            print('Nope , The given word is not in Palindrome 🤷‍♂️')

    if n == 3:
        n1 = int(input('Give me a number for checking Prime : '))
        a = True
        for i in range(2, n1):
            if n1 % i == 0:
                a = False
        if a:
            print('Yes , The given no. is prime ✌️')
        else:
            print('No , The given no. is not prime 🤷‍♂️')

    if n == 4:
        n2 = int(input('No. for factorial : '))
        f = 1
        for i in range(1, n2 + 1):
            f = f * i
        print(f)

    if n == 5:
        print(" 👉👉 Enter all the numbers using a single space ")
        n1 = input().split()
        a = []
        avr = 0
        len_n1 = len(n1)
        for i in n1:
            x = int(i)
            a.append(x)
        for j in a:
            avr = avr + j
        print('Average of the given no. is : ', avr // len_n1)

    if n == 6:
        print("👉👉 do sum using using '+' sign , eg.= 2+3+5 and it will answer 8")
        n1 = input().split('+')
        a = []
        sum = 0
        for i in n1:
            a.append(int(i))
        for j in a:
            sum = sum + j
        print('Sum of the given no. is : ', sum)

    if n == 7:
        print("👉👉 do substraction using using '-' sign , eg.= 5-2-3 and it will answer 0")
        n1 = input().split('-')
        a = []
        g = n1[0]
        sub = int(g)
        for i in n1:
            a.append(int(i))
        for j in a[1:]:
            sub = sub - j
        print('Substraction of the given no. is : ', sub)

    if n == 8:
        print('''
                1. A snail can sleep for three years.😮.
                2. Almonds are a member of peach family 🤔 . 
                3. Elephants are the only animals that can’t jump 😮.
                4. Coca-Cola was originally green because of fresh cocoa leaves 😮.
                5. Like fingerprints , everyone's tongue print is different 🤔.''')
