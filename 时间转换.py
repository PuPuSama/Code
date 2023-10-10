import sys
def hours(s):
    if s<0:
        raise ValueError("Wrong Number!")
    else:
        print("{}H,{}M".format(*divmod(s,60)))
try:
    hours(int(sys.argv[1]))
except:
    print('Parameter Error')
