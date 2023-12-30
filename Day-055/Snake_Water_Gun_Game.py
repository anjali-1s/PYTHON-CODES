'''                               S W G
computer =                     0 1 2
player =             S 0       D W L
                     W 1       L D W
                     G 2       W L D
'''

import random

def check(comp,user):
     if comp == user:
          return 0

     if (comp == 0 and user == 1):
          return -1

     if (comp == 1 and user == 2):
          return -1

     if (comp == 2 and user == 0):
          return -1
     return 1

comp = random.randint(0,2)
user = int(input("0 for snake, 1 for water and 2 for gun:\n"))

score = check(comp,user)

print("You",user)
print("Computer",comp)

if score == 0:
     print("Draw")

elif score == 1:
     print("Winner")

else:
     print("Looser")