__author__ = 'evgen'

while 1:
    reply = input('Enter the text:')
    if reply == 'stop':
        break
    print(reply)

#
while 1:
    reply = input("Enter digit:")
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Not digit')
    else:
        print(num ** 2)
print('Bye')

#
while True:
    reply = input('Enter digit > 20:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Not digit!')
    else:
        num = int(reply)
        if num < 20:
            print("Digit low than 20")
        else:
            print(num**2)
print('Bye')