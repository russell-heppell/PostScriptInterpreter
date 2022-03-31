# Russell Heppell

# ------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  # assuming top of the stack is the end of the list

# Now define the helper functions to push and pop values on the opstack
# (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

import numbers
import re


def opPop():
    size = len(opstack) - 1
    if size >= 0:
        return opstack.pop(size)
    else:
        print("empty stack!")
        return None

    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.


def opPush(value):
    opstack.append(value)


# -------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  # assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name

def dictPop():
    size = len(dictstack) - 1
    if size >= 0:
        dictstack.pop(size)
    else:
        print("cannot pop an empty stack")

    # dictPop pops the top dictionary from the dictionary stack.


def dictPush(d):
    dictstack.append(d)

    # dictPush pushes the dictionary ‘d’ to the dictstack.
    # Note that, your interpreter will call dictPush only when Postscript
    # “begin” operator is called. “begin” should pop the empty dictionary from
    # the opstack and push it onto the dictstack by calling dictPush.


def define(name, value):
    if len(dictstack) == 0:
        dictstack.append({name: value})
    else:
        dictstack[len(dictstack) - 1].update({name: value})


    # add name:value pair to the top dictionary in the dictionary stack.
    # Keep the '/' in the name constant.
    # Your psDef function should pop the name and value from operand stack and
    # call the “define” function.


def lookup(name):
    if isinstance(name, str):
        if not name[0].isdigit():
            size = len(dictstack) - 1
            newname = '/' + name
            while size >= 0:
                if newname in dictstack[size].keys():
                    return dictstack[size][newname]
                else:
                    size -= 1
        else:
            print("variables don't start with numbers")
    else:
        print("name must be a string")

    print("variable name not in the dictionary stack!")     # only gets here if we found nothing to return

    # return the value associated with name
    # What is your design decision about what to do when there is no definition for
    # “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


# --------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.
def add():
    if len(opstack) >= 2:   # making sure stack has enough values
        val2 = opstack.pop()
        val1 = opstack.pop()
        if isinstance(val1, numbers.Number) and isinstance(val2, numbers.Number):
            val3 = val1 + val2
            opstack.append(val3)
        else:
            opstack.append(val1)
            opstack.append(val2)
            print("invalid add operation.")         # one of the values isn't a number
    else:
        print("not enough values on the stack.")    # less than 2 values on the stack


def sub():
    if len(opstack) >= 2:   # making sure stack has enough values
        val2 = opstack.pop()
        val1 = opstack.pop()
        if isinstance(val1, numbers.Number) and isinstance(val2, numbers.Number):
            val3 = val1 - val2
            opstack.append(val3)
        else:
            opstack.append(val1)
            opstack.append(val2)
            print("invalid subtract operation.")    # one of the values isn't a number
    else:
        print("not enough values on the stack.")    # less than 2 values on the stack


def mul():
    if len(opstack) >= 2:   # making sure stack has enough values
        val2 = opstack.pop()
        val1 = opstack.pop()
        if isinstance(val1, numbers.Number) and isinstance(val2, numbers.Number):
            val3 = val1 * val2
            opstack.append(val3)
        else:
            opstack.append(val1)
            opstack.append(val2)
            print("invalid multiply operation.")    # one of the values isn't a number
    else:
        print("not enough values on the stack.")   # less than 2 values on the stack


def div():
    if len(opstack) >= 2:   # making sure stack has enough values
        val2 = opstack.pop()
        val1 = opstack.pop()
        if isinstance(val1, numbers.Number) and isinstance(val2, numbers.Number):
            if val2 != 0:
                val3 = val1 / val2
                opstack.append(val3)
            else:
                opstack.append(val1)
                opstack.append(val2)
                print("divide by zero error.")
        else:
            opstack.append(val1)
            opstack.append(val2)
            print("invalid divide operation.")         # one of the values isn't a number
    else:
        print("not enough values on the stack.")    # less than 2 values on the stack


def mod():
    if len(opstack) >= 2:
        val2 = opstack.pop()
        val1 = opstack.pop()
        if isinstance(val1, numbers.Number) and isinstance(val2, numbers.Number):
            if val2 != 0:
                val3 = val1 % val2
                opstack.append(val3)
            else:
                print("divide by 0 error.")
        else:
            opstack.append(val1)
            opstack.append(val2)
            print("invalid mod operation.")
    else:
        print("not enough values on the stack.")


def eq():
    if len(opstack) >= 2:
        val2 = opstack.pop()
        val1 = opstack.pop()
        if isinstance(val1, numbers.Number) and isinstance(val2, numbers.Number) or \
                isinstance(val1, str) and isinstance(val2, str):
            if val1 == val2:
                opstack.append(True)
            else:
                opstack.append(False)
        else:
            opstack.append(val1)
            opstack.append(val2)
            print("Invalid equality operation.")
    else:
        print("not enough values on the stack.")


def lt():
    if len(opstack) >= 2:
        val2 = opstack.pop()
        val1 = opstack.pop()
        if isinstance(val1, numbers.Number) and isinstance(val2, numbers.Number):
            if val1 < val2:
                opstack.append(True)
            else:
                opstack.append(False)
        else:
            opstack.append(val1)
            opstack.append(val2)
            print("Invalid less than operation.")
    else:
        print("not enough values on the stack.")


def gt():
    if len(opstack) >= 2:
        val2 = opstack.pop()
        val1 = opstack.pop()
        if isinstance(val1, numbers.Number) and isinstance(val2, numbers.Number):
            if val1 > val2:
                opstack.append(True)
            else:
                opstack.append(False)
        else:
            opstack.append(val1)
            opstack.append(val2)
            print("Invalid greater than operation.")
    else:
        print("not enough values on the stack.")


# --------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval, put

def validstr(string):
    if isinstance(string, str):
        if string[0] == '(' and string[len(string) - 1] == ')':
            return True
        else:
            return False
    else:
        return False


def length():
    if len(opstack) >= 1:
        string = opstack.pop()
        size = len(string)
        if validstr(string):
            opstack.append(size - 2)
        else:
            opstack.append(string)
            print("invalid string on stack")
    else:
        print("empty stack!")


def get():
    if len(opstack) >= 2:
        index = opstack.pop()
        str = opstack.pop()
        size = len(str)
        if validstr(str):
            if isinstance(index, int) and 0 <= index < (size - 2):
                opstack.append(ord(str[index + 1]))
            else:
                opstack.append(str)
                opstack.append(index)
                print("invalid index!")
        else:
            opstack.append(str)
            opstack.append(index)
            print("invalid string!")
    else:
        print("not enough operands on stack!")


def getinterval():
    if len(opstack) <= 3:
        count = opstack.pop()
        index = opstack.pop()
        string = opstack.pop()
        size = len(string)
        if validstr(string):
            if isinstance(index, int) and 0 <= index < (size - 2):
                if isinstance(count, int) and count > 0 and (index + count) <= (size - 2):
                    newstr = '(' + string[(index + 1): (index + count + 1)] + ')'
                    opstack.append(newstr)
                else:
                    opstack.append(string)
                    opstack.append(index)
                    opstack.append(count)
                    print("invalid count")
            else:
                opstack.append(string)
                opstack.append(index)
                opstack.append(count)
                print("invalid index")
        else:
            opstack.append(string)
            opstack.append(index)
            opstack.append(count)
            print("invalid string")
    else:
        print("not enough values on stack")


def put():
    if len(opstack) >= 3:
        charval = opPop()
        index = opPop()
        string = opPop()
        if validstr(string):
            if isinstance(index, int) and 0 <= index < (len(string) - 2):
                if isinstance(charval, int) and 0 <= charval <= 127:
                    newstring = list(string)
                    newstring[index + 1] = chr(charval)
                    newstring = "".join(newstring)              # s is the updated string

                    # now, look in opstack for same string
                    for val in opstack:
                        if id(val) == id(string):
                            ind = opstack.index(val)
                            opstack[ind] = newstring

                    # now search the dictstack, keys first
                    for dic in dictstack:
                        for key in dic.keys():
                            if id(key) == id(string):
                                dic[newstring] = dic.pop(string)

                    # now look at values
                    for dic in dictstack:
                        for key, val in dic.items():
                            if id(val) == id(string):
                                dic[key] = newstring

                else:
                    opPush(string)
                    opPush(index)
                    opPush(charval)
                    print("invalid ASCII value")
            else:
                opPush(string)
                opPush(index)
                opPush(charval)
                print("invalid index value")
        else:
            opPush(string)
            opPush(index)
            opPush(charval)
            print("invalid string")
    else:
        print("not enough values on the stack")


# --------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack
def dup():
    if len(opstack) >= 1:
        obj = opstack.pop()
        opstack.append(obj)
        opstack.append(obj)
    else:
        "not enough operands on stack!"


def copy():
    value = opstack.pop()
    leng = len(opstack)
    if isinstance(value, int):
        tempindex = leng - value
        if value <= len(opstack):
            while tempindex < leng:
                opstack.append(opstack[tempindex])
                tempindex += 1
        else:
            opPush(value)
            print("value too large!")
    else:
        opPush(value)
        print("invalid value, must be an integer")


def pop():
    opPop()


def clear():
    size = len(opstack)
    while size > 0:
        pop()
        size -= 1


def exch():
    if len(opstack) >= 2:
        val1 = opstack.pop()
        val2 = opstack.pop()
        opPush(val1)
        opPush(val2)
    else:
        print("not enough values on stack!")


def roll():
    rollcount = opPop() # this is j
    numelems = opPop()  # this is n
    length = len(opstack) - 1
    if length >= 0:
        if isinstance(rollcount, int) and isinstance(numelems, int):
            if numelems <= len(opstack):
                if rollcount < 0:
                    rollcount = numelems - (rollcount * -1)

                for r in range(rollcount):
                    length = len(opstack) - 1
                    for e in range(numelems - 1):
                        temp = opstack[length]
                        opstack[length] = opstack[length - 1]
                        opstack[length - 1] = temp
                        length -= 1
            else:
                opPush(numelems)
                opPush(rollcount)
                print("number of elements to roll cant exceed length of the stack")
        else:
            opPush(numelems)
            opPush(rollcount)
            print("roll count and number of elements must be an integer")
    else:
        opPush(numelems)
        opPush(rollcount)
        print("length of the stack has to be greater than 0")


def stack():
    size = len(opstack)
    while size > 0:
        print(opstack[(size - 1)])
        size -= 1


# --------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python.
# Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your
# own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.


def psDict():
    opPop()
    opPush({})


def begin():
    if len(opstack) >= 1:
        dict = opPop()
        if dict == {}:
            dictPush(dict)
        else:
            print("invalid dictionary!")
    else:
        print("empty stack!")


def end():
    dictPop()


def psDef():
    if len(opstack) >= 2:
        value = opPop()
        name = opPop()
        if isinstance(name, str):
            if name[0] == '/':
                define(name, value)
            else:
                opPush(name)
                opPush(value)
                print("variable name must start with '/'. error in psDef")
        else:
            opPush(name)
            opPush(value)
            print("variable name must be a string. error in psDef")
    else:
        print("not enough values on stack!")


def psIf():
    if len(opstack) >= 2:
        code = opPop()
        boolean = opPop()

        if isinstance(code, list) and boolean == True or boolean == False:
            if boolean:
                interpretSPS(code)
        else:
            opPush(boolean)
            opPush(code)
            print("error in format of if statement.")

    else:
        print("not enough elements on stack for if statement.")


def psIfelse():
    if len(opstack) >= 3:
        code1 = opPop()
        code2 = opPop()
        boolean = opPop()

        if isinstance(code1, list) and isinstance(code2, list) and boolean == True or boolean == False:
            if boolean:
                interpretSPS(code2)
            else:
                interpretSPS(code1)
        else:
            opPush(boolean)
            opPush(code2)
            opPush(code1)
            print("error in format of ifelse statement.")
    else:
        print("not enough elements on stack for ifelse statement.")


def psFor():
    if len(opstack) >= 4:
        code = opPop()
        final = opPop()
        increment = opPop()
        initial = opPop()

        if isinstance(code,list) and isinstance(final, int) and isinstance(increment, int) and isinstance(initial, int):
            if initial < final:
                if increment > 0:
                    while initial <= final:
                        opPush(initial)
                        interpretSPS(code)
                        initial += increment
                else:
                    opPush(initial)
                    opPush(increment)
                    opPush(final)
                    opPush(code)
                    print("invalid increment amount.")

            elif initial > final:
                if increment < 0:
                    while initial >= final:
                        opPush(initial)
                        interpretSPS(code)
                        initial += increment
                else:
                    opPush(initial)
                    opPush(increment)
                    opPush(final)
                    opPush(code)
                    print("invalid decrement amount")
            else:
                interpretSPS(code)
        else:
            opPush(initial)
            opPush(increment)
            opPush(final)
            opPush(code)
            print("error in format of for loop.")
    else:
        print("not enough elements on stack for a for loop.")


def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested # tokens, where the
# tokens between '{' and '}' is included as a sublist. If the # parenteses in the input iterator is
# not properly nested, returns False.


def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c == '{':
            # Note how we use a recursive call to group the tokens inside the # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner
            # parenthesis, it will be appended to the list we are constructing # as a whole.
            res.append(groupMatching2(it))
        else:
            if c.lstrip('-').isdigit():
                res.append(int(c))
            elif c == 'True':
                res.append(True)
            elif c == 'False':
                res.append(False)
            else:
                res.append(c)
    return False


# Function to parse a list of tokens and arrange the tokens between { and } braces # as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c == '}':  # non matching closing parenthesis; return false since there is
                      # a syntax error in the Postscript code.
            return False
        elif c == '{':
            res.append(groupMatching2(it))
        else:
            if c.lstrip('-').isdigit():
                res.append(int(c))
            elif c == 'True':
                res.append(True)
            elif c == 'False':
                res.append(False)
            else:
                res.append(c)
    return res


def varexists(name):
    size = len(dictstack) - 1
    newname = '/' + name
    while size >= 0:
        if newname in dictstack[size].keys():
            return True
        else:
            size -= 1
    return False


def interpretSPS(code):  # code is a code-array
    for element in code:
        if isinstance(element, list):
            opPush(element)
        elif element in psCommand.keys():
            psCommand[element]()
        elif len(dictstack) > 0 and isinstance(element, str) and varexists(element):
            code = lookup(element)
            if isinstance(code, list):
                interpretSPS(code)
            else:
                opPush(code)
        else:
            opPush(element)


def interpreter(s):  # s is a string
    interpretSPS(parse(tokenize(s)))


# Dictionary that maps GhostScript commands to our interpreter functions.
psCommand = {'dict': psDict, "pop": pop, "def": psDef, "add": add, "sub": sub, "mul": mul,
             "div": div, "mod": mod, "eq": eq, "lt": lt, "gt": gt, "length": length,
             "get": get, "getinterval": getinterval, "put": put, "dup": dup, "copy": copy,
             "clear": clear, "exch": exch, "roll": roll, "stack": stack, "begin": begin,
             "end": end, "if": psIf, "ifelse": psIfelse, "for": psFor}


if __name__ == '__main__':

    input1 = """ /square {
    dup mul } def
        (square)
        4 square
        dup 16 eq
        {(pass)} {(fail)} ifelse
    stack """

    print("         \n\ninput 1: ")
    print(tokenize(input1))
    print("----NEXT CHECK----")
    print(parse(tokenize(input1)))

    input2 = """
    (facto) dup length /n exch def /fact {
        0 dict begin
           /n exch def
           n 2 lt
           { 1}
           {n 1 sub fact n mul }
           ifelse
    end } def
    n fact stack
    """

    print("         \n\ninput 2: ")
    print(tokenize(input2))
    print("----NEXT CHECK----")
    print(parse(tokenize(input2)))

    input3 = """ 
        /fact{
        0 dict
                begin 
                        /n exch def
                        1
                        n -1 1 {mul} for
                end
    
        } def
        6 
        fact 
        stack
    """

    print("         \n\ninput 3: ")
    print(tokenize(input3))
    print("----NEXT CHECK----")
    print(parse(tokenize(input3)))

    input4 = """
    /lt6 { 6 lt } def
    1 2 3 4 5 6 4 -3 roll
    dup dup lt6 {mul mul mul} if stack
    clear
    """

    print("         \n\ninput 4: ")
    print(tokenize(input4))
    print("----NEXT CHECK----")
    print(parse(tokenize(input4)))

    input5 = """
    (CptS355_HW5) 4 3 getinterval (355) eq {(You_are_in_CptS355)} if
    stack """

    print("         \n\ninput 5: ")
    print(tokenize(input5))
    print("----NEXT CHECK----")
    print(parse(tokenize(input5)))

    input6 = """
    /pow2 {/n exch def
    (pow2_of_n_is) dup 8 n 48 add put 1 n -1 1 {pop 2 mul} for
    } def
    (Calculating_pow2_of_9) dup 20 get 48 sub pow2 stack
    """

    print("         \n\ninput 6: ")
    print(tokenize(input6))
    print("----NEXT CHECK----")
    print(parse(tokenize(input6)))

    # ------------ NOW TESTING INTERPRETER ----------------

    print("\n\n--------Now testing interpreter on input 1-------")
    clear()
    interpreter(input1)

    print("\n\n--------Now testing interpreter on input 2-------")
    clear()
    interpreter(input2)

    print("\n\n--------Now testing interpreter on input 3-------")
    clear()
    interpreter(input3)

    print("\n\n--------Now testing interpreter on input 4-------")
    clear()
    interpreter(input4)

    print("\n\n--------Now testing interpreter on input 5-------")
    clear()
    interpreter(input5)

    print("\n\n--------Now testing interpreter on input 6-------")
    clear()
    interpreter(input6)

