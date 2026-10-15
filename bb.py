# Задание №3.8

X = False
Y = False
Z = True

# Решение

set_a = X and not(Z or Y) or not(Z) # F and not(T or F) or not(T) -> F or F -> F
set_b = not(X) or X and (Y or Z) # not(F) or F and (F or T) -> T and T -> T
set_c = (X or Y and not(Z)) and Z # (F or F and not(T)) and T -> F and T -> F

# Задание №3.14

# Первый вариант

A = False
B = True
C = True

set_a1 = not(A and B) and (not(A) or not(C)) # not(F and T) and (not(F) or not(T) -> 
set_b1 = not(A and not(B)) or (A or not(C))
set_c1 = A and not(B) or not(A or not C)