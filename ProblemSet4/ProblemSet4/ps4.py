# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#


def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    result = {}
    for index, delay in enumerate([0, 75, 150, 300], 1):
        patients_trial = [TreatedPatient([ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for _ in range(numViruses)], maxPop) for _ in range(numTrials)]
        final_virus_pop = []
        for p in patients_trial:
            for i in range(delay):
                p.update()
            p.addPrescription('guttagonol')
            for i in range(150):
                p.update()
            final_virus_pop.append(p.getTotalPop())
        result[delay] = final_virus_pop
        pylab.subplot(2, 2, index)
        pylab.hist(final_virus_pop)
    pylab.show()
    # return result

# result = simulationDelayedTreatment(1000)
# for k, v in result.iteritems():
#     print k, ":", 1.0*len([c for c in v if 0<=c<=50])/len(v)
#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    result = {}
    for index, delay in enumerate([0, 75, 150, 300], 1):
        final_virus_pop = []
        for i in range(numTrials):
            p = TreatedPatient([ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for _ in range(numViruses)], maxPop)
            for i in range(150):
                p.update()
            p.addPrescription('guttagonol')
            for i in range(delay):
                p.update()
            p.addPrescription('grimpex')
            for i in range(150):
                p.update()
            final_virus_pop.append(p.getTotalPop())
        result[delay] = final_virus_pop
    #     pylab.subplot(2, 2, index)
    #     pylab.hist(final_virus_pop)
    # pylab.show()
    return result

# print simulationTwoDrugsDelayedTreatment(10)
# result = simulationTwoDrugsDelayedTreatment(10)
# for k, v in result.iteritems():
#     print k, ":", 1.0*len([c for c in v if 0<=c<=50])/len(v)

