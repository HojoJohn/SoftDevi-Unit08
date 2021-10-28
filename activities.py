import random
import sorts

def tuples(a_tuple):

    print(len(a_tuple))
    print(a_tuple)

    for element in a_tuple:
        print(element)

def lists():

    a_list = [1,2,3]

    for element in a_list:
        print(element)

    for index in range(len(a_list)):
        print(index,": ", a_list[index], sep="")

    a_list[0] = 57

    return a_list
def make_list(a_sequence):

    a_list = []

    for element in a_sequence:
        a_list.append(element)

    return a_list

def scale(a_list,scalar):
    for index in range(len(a_list)):
        a_list[index] = a_list[index] * scalar
    
    return a_list

def mutater(a_list, an_int):
    print("mutater", an_int, a_list)
    an_int = an_int * 5
    a_list[0] *= 5

    print("mutater", an_int, a_list)

def cat(a_list, b_list):

    a_list = a_list + b_list
    return a_list

def extender(a_list, b_list):

    a_list += b_list
    return a_list

def inserter(a_list,value):
    
    middle = len(a_list) //2

    a_list.insert(middle,value)

def popper(a_list):
    length = len(a_list)
    if length > 0:
        index = random.randrange(length)
        popped = a_list.pop(index)
        print(a_list,popped)

        popper(a_list)

def rgb_tuple():

    red = random.random()
    green = random.random()
    blue = random.random()
    return(red,green,blue)
def tuple_equality(a_tuple, b_tuple):

    print(a_tuple)
    print(b_tuple)

    a_tuple = ("a",12,True)
    b_tuple = ("a",12,True)

    print(a_tuple is b_tuple)

    print(a_tuple == b_tuple)

def reverse_sequence(sequence):
    lst = []

    for value in reversed:
        lst.append(value)
    
    length = len(sequence)

    for index in range(length-1,-1,-1):
        lst.append(sequence[index])
    
    return lst

def slices():

    string = "Gucci gang, Gucci gang, Gucci gang, Gucci gang (Gucci gang) Gucci gang, Gucci gang, Gucci gang, Gucci gang (Gucci gang)"
    
    a_list = list(string)
    start = 0
    stop = 0

    for index in range(len(a_list)):
        if a_list[index] == ' ':
            stop = index
            word = a_list[start:stop]
            print(word)

            start = stop + 1
    word = a_list[start:]
    print(word)

def dices(a_list):
    if not a_list:
        return
    else:
        element = a_list[0:1]
        print(element)
        dices(a_list[1:])



def random_list(size):
   
    rand_list = []
    for _ in range(size):
       value = random.randint(0,100)
       rand_list.append(value)
    return rand_list

def sorted_test(a_list, backwards=False):
    print(a_list)
    b_list = sorted(a_list, reversed = backwards)
    print(b_list)

def sort_test(a_list):
    print(a_list)
    a_list.sort()
    print(a_list)

def sort_cards(hand):
    print(hand)
    hand.sort()
    print(hand)

def suit_key(card):
    RANK = 0
    SUIT = 1

def packer():

    a =1
    b =2
    c =3
    d = 4


    return a,b,c,d

def swapper(a_list):
    length = len(a_list)
    if length <2:
        return a_list
    else:
        half = length // 2
        swapped = []
    
    for index in range(half,length):
        swapped.append(a_list[index])


    for index in range(half):
        swapped.append(a_list[index])
    return swapped


def chunky(a_list,size):
    start = 0
    stop = size
    chunk = a_list[start:stop]

    while chunk:
        print(chunk)

        start = stop
        stop = start + size

        chunk = a_list[start:stop]

def sevens_key(number):
    string = str(value)

    if number == 7:
        return 0

def comprehension():
    print(letter for letter in "foobar")

    print([0 for _ in range(15)])

    print([number for number in range(13)])

    print([n for n in range(0,50) if n % 3 == 0 or n % 5 == 0])

def make_table(rows, columns, value):

    table = ([] for _ in range(rows))

    for row in table:
        row += [value for _ in range(columns)]


def main():
    tuples(("a",12,True))

    lists()
    a_sequence = range(0,11,12)
    make_list(a_sequence)

    a_list = make_list.append(1,5,11)
    print(a_list)

    a_list = [1,2,3]
    b_list = ["a","b","c"]
    c_list = cat(a_list,b_list)

    print(a_list)
    print(b_list)
    print(c_list)

    a_list = [1,2,3]
    b_list = ["a","b"]
    c_list = extender(a_list,b_list)
    print(a_list)
    print(b_list)
    print(c_list)

    a_list = []

    rgb_tuple()

    a_list = [1,5,True,"abc"]
    a_tuple = tuple(a_list)
    tuple_equality(a_tuple)

    packed = packer()
    w =packed[0]
    x =packed[1]
    y =packed[2]
    z =packed[3]

    print(w)
    print(x)
    print(y)
    print(z)


    print(swapper([]))
    print(swapper([1]))
    print(swapper[1,1,1,1])

        

    
chunky([1,2,3,4,5,6,7,8,9,10], 4)



main()