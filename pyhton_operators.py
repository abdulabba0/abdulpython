"""
We use python operators to operate on variables

1. Arithmetic operations
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators

Arithmetic operations:
+ : Addition 
- : Subtraction
* : Multiplication
 / : Division
 % : Modulus - Remainder after division
** : Exponentiation - raise to the power of
// : Floor Division - ignore the decimal side
"""

# a = 5
# b = 7
# print(f"Addition : {a + b}")
# print(f"Subration : {b - a}")
# print(f"Multiplition : {a * b}")
# print(f"Division : {b / a}")
# print(f"Modulus : {b % a}")
# print(f"Exponentiation : {a ** b}")
# print(f"Floor Division : {b // a}")

"""
Assignment operations are use to assign variable to a value

a = 5
a += 1
a -= 1
a *= 2
a /= 2
a //= 2
a %= 2
a **= 2
"""

assign = 9

# assign += 5
# assign -= 1
# assign /= 3
# assign *= 3
# assign **= 3
# assign %= 3
# assign //= 3
# print(f"Value of assign is {assign}")

#Comparison Operators

comp1 = 1
comp2 = 3

# if comp2 > comp1 :
#     print("Yes, it is greater")
# print(f"Greater than : {comp1 > comp2}")
# print(f"Less than : {comp1 < comp2}")
# print(f"Greater than or equal to : {comp1 >= comp2}")
# print(f"Less than ir equal to : {comp1 <= comp2}")
# print(f"Not equal to : {comp1 != comp2}")

"""
Logical Operators
1. and
2. or
3. not

Rules
1. AND: both side has to be true to get a true
TRUE AND TRUE : TRUE
TRUE AND FALSE : FALSE
FALSE AND TRUE : FALSE
FALSE AND FALSE : FALSE

2. OR: As long as one side is true, the expression is TRUE
TRUE OR TRUE : TRUE
TRUE OR FLASE : TRUE
FALSE OR TRUE : TRUE
FALSE OR FALSE : FALSE

3. NOT: Negates everything
"""
# AND Operator
# print(f"True and True : {True and True}")
# print(f"False and True : {False and True}")
# print(f"True and False : {True and False}")
# print(f"False and False : {False and False}")
# print('=======' * 5)

# # OR Operator
# print(f"True or True : {True or True}")
# print(f"False or True : {False or True}")
# print(f"True or False : {True or False}")
# print(f"False or False : {False or False}")
# print('=======' * 5)

# NOT Operator
# print(f"True and True : {not(True and True)}")
# print(f"False and True : {not(False and True)}")
# print(f"True and False : {not(True and False)}")
# print(f"False and False : {not(False or False)}")

# print(bool(""))

"Identity Operator"
# id1 = 4
# id2 = 6
# print(id1 is id2)
# print(id1 is not id2)

"""
Membership Operator
1. in
2. Not in
"""
# a = [1, 2, 3, 4, 5]
# print(3 in a)
# print(3 not in a)

"""
Bitwise operator used for binary comparism
1. & AND 
2. | OR
3. ^ XOR
4. ~ NOT

0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110

AND
6 & 3 
0110 & 0011
0010 = 2

OR
6 | 4 
0110 & 0100
0110 = 6

XOR
6 ^ 3 
0110 & 0011
0101 = 5

NOT
6 ~ 3 
0110 & 0011

"""
print(6 & 3 )