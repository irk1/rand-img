import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
#userseed = int(input())
#userseed=int('2')
def makeIMG():
    userseed=np.random.randint(0,10)
    rng = np.random.default_rng(seed=userseed)

    print(userseed)
    arr1 = rng.integers(0,256,(375, 500))
    plt.imshow(arr1,cmap='gray', vmin=0, vmax=255, interpolation='none')
    plt.show()
    print (arr1)
def findSeed():
    img = np.asarray(Image.open('stinkbug.png'))
    print(repr(img))
findSeed()
