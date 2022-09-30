def main():
    torso = int(input('put in me:\n'))
    shoe = input('put in me:\n')
    head = input('put in me:\n')
    arms = input('put in me:\n')
    print()
    if head == 'girl':
        print_head()
    print_arms(arms)
    print_big_face(torso)
    print_shoe(shoe)


def print_big_face(torso):
    i = 0
    while i < torso:
        print('  ', end='   ')
        print('|-X-|')
        i += 1

def print_shoe(shoe):
    print('  ', end='   ')
    print(shoe)

def print_head():
    print('  "|"""""""|" ')
    print('  "| *   * |" ')
    print('  "|   V   |" ')
    print('  "|  ~~~  |" ')
    print('  " \_____/ " ')


def print_arms(arms):
    print('0' + arms, end='|---|')
    print(arms + '0')



