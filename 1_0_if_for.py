## IF statement

x = int(input('Please enter an integer: '))

if x < 0:
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
## FOR statement

# Measure some strings:
words = ['cavin', 'windows', 'categorization']
for w in words:
    print(w, len(w))

print(words[0])

## The range() Function

for i in range (5):
    print(i)

# The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices
# for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a differ
# ent increment (even negative; sometimes this is called the ‘step’):
my_list = list(range(5, 10))
my_list_1 = list(range(0, 10, 3))
my_list_2 = list(range(-10, -100, -30))
print(my_list, my_list_1, my_list_2)

print(list(range(6, 12)))