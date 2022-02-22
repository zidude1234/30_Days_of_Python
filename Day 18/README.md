#  💻 Lets Go!!🚀 🚀 🚀 

#  3️⃣0️⃣ Days of Python - Day Eighteen

## 📚 Table of Contents
- [Objective](#objective)
  - [💻 Exercises - Day 18](#-exercises-day-18)
    - [Exercises: Level 1](#exercises-level-1)
    - [Exercises: Level 2](#exercises-level-2)
    - [Exercises: Level 3](#exercises-level-3)
- [Solution on Github](https://github.com/zidude1234/30_Days_of_Python/blob/main/Day%2018/Python%20Syntax/Day18%20Syntax.py)

## Objective
This repository contains the solution for the Day Eighteen of the "30 Days of Python Challenge"!
Thanks @Asabaneh for the excellent Python Content! 👋🏻

## 💻 Exercises: Day 18

### Exercises: Level 1
 1. What is the most frequent word in the following paragraph?
```py
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```

```sh
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
```

2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

```py
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) # 12
```

### Exercises: Level 2

1. Write a pattern which identifies if a string is a valid python variable

    ```sh
    is_valid_variable('first_name') # True
    is_valid_variable('first-name') # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname') # True
    ```

### Exercises: Level 3

1. Clean the following text. After cleaning, count three most frequent words in the string.

    ```py
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

    print(clean_text(sentence));
    I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
    ```

 [<< Day 17](../Day%2017/README.md) | [Day 19 >>](../Day%2019/README.md)

--#### [Go to Top of Page](#objective)
