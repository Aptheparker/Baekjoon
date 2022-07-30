#input

input = input()

#control
if input == 'A+':
    output = 4.3
elif input == 'A0':
    output = 4.0
elif input == 'A-':
    output = 3.7

elif input == 'B+':
    output = 3.3
elif input == 'B0':
    output = 3.0
elif input == 'B-':
    output = 2.7

elif input == 'C+':
    output = 2.3
elif input == 'C0':
    output = 2.0
elif input == 'C-':
    output = 1.7

elif input == 'D+':
    output = 1.3
elif input == 'D0':
    output = 1.0
elif input == 'D-':
    output = 0.7

else:
    output = 0.0

#output
print(output)