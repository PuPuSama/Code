import sys
def demo(s,data=[]):
    with open(s) as fd:
        de = fd.read()
        for i in de:
            if i.isdigit():
                data.append(i)
        print(data)
if __name__ == '__main__':
    demo(sys.argv[1])
