import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
NUMSTEPS = 200

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    for i in xrange(CURRENTRABBITPOP):
        if random.random() < 1.0 - CURRENTRABBITPOP * 1.0 / MAXRABBITPOP:
            CURRENTRABBITPOP += 1 if CURRENTRABBITPOP < 1000 else 0


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    for i in xrange(CURRENTFOXPOP):
        if random.random() < CURRENTRABBITPOP * 1.0 / MAXRABBITPOP:
            CURRENTRABBITPOP -= 1 if CURRENTRABBITPOP > 10 else 0
            if random.random() < 1.0 / 3:
                CURRENTFOXPOP += 1
        else:
            if random.random() < 0.9:
                CURRENTFOXPOP -= 1 if CURRENTFOXPOP > 10 else 0


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations = []
    fox_populations = []
    for i in xrange(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return rabbit_populations, fox_populations

if __name__ == '__main__':
    rabbit_populations, fox_populations = runSimulation(NUMSTEPS)
    # print rabbit_populations, fox_populations
    pylab.plot(rabbit_populations)
    pylab.plot(fox_populations)
    # pylab.xlabel('time step')
    # pylab.ylabel('# viruses')
    coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
    pylab.plot(pylab.polyval(coeff, range(len(rabbit_populations))))
    coeff = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)
    pylab.plot(pylab.polyval(coeff, range(len(fox_populations))))
    pylab.legend(('rabbit_populations', 'fox_populations','rabbit_populations_fit', 'fox_populations_fit'))
    pylab.show()

