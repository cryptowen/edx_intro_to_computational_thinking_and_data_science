import random
import pylab

balls = [0] * 500 + [1] * 500
random.shuffle(balls)

def lv_method():
    steps = 0
    while True:
        steps += 1
        if random.choice(balls):
            return steps

def mc_method():
    steps = 0
    start_pos = random.choice(range(1000))
    while True:
        steps += 1
        if balls[start_pos]:
            return steps
        start_pos = (start_pos + 1) % 1000

def lv_sim():
    histogram = [0 for i in range(1, 1000)]
    for i in range(1000):
        result = mc_method()
        histogram[result] += 1
    # pylab.plot(histogram)
    # pylab.show()
    return histogram

if __name__ == '__main__':
    print lv_sim()
