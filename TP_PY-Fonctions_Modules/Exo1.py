# Quaestion 1:
def maximum(a, b):
    if a > b :
        return a
    elif a < b :
        return b


# Question 2:
def est_pair(n):
    if n % 2 == 0:
        return True
    elif n % 2 != 0 :
        return False
    else:
        return 0

#Question 3:
def moyenne(note):
    if len(note) == 0:
        return None

    return sum(note) / len(note)



#appelle:

#1
print(maximum(15, 20))
#2
print(est_pair(20))
#3
print(moyenne([12, 15, 18])) 