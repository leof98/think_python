def linha():
    menos = '----'
    print('+' + menos + '+' + menos + '+')

def do_four(f):
    f()
    f()
    f()
    f()

def serio():
    space = '    '
    s = '|' + space + '|' + space + '|'
    print(s)

linha()
do_four(serio)
linha()
do_four(serio)
linha()
#09.07
