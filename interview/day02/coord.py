def check_step(step):
    if (step[0] in ['A', 'S', 'W', 'D']
            and step[1:].isdigit()
            and str(int(step[1:])) == step[1:]):
        return True
    return False


def move(start, action):
    if action[0] == 'A':
        start[0] -= int(action[1:])
    elif action[0] == 'S':
        start[1] -= int(action[1:])
    elif action[0] == 'W':
        start[1] += int(action[1:])
    elif action[0] == 'D':
        start[0] += int(action[1:])


while True:
    try:
        s = input()
        steps = filter(check_step, s.split(';'))
        start = [0, 0]
        for step in steps:
            move(start, step)
        print(','.join(map(str, start)))
    except:
        break