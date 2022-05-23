print("really?")
exit()
from compile import compile
from prep import prep



def both(pth):
    prep(pth)
    compile(pth)


if __name__ == '__main__':
    pth="#DEAN"
    pth="#ether"
    pth="#fair"
    pth="#yano"

    pth=pth.replace("#","../")
    both(pth)

