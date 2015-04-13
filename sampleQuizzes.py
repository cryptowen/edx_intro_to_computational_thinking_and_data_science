import random
import pylab

def sampleQuizzes():
    # Your code here
    scores = generateScores(10000)
    count = 0
    for score in scores:
        if 70 <= score <= 75:
            count += 1
    return count/10000.0

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of
    the three exams, then calculates the final score and
    appends it to a list of scores.

    Returns: A list of numTrials scores.
    """
    scores = []
    for i in range(numTrials):
        mid1 = random.choice(range(50, 81))
        mid2 = random.choice(range(60, 91))
        final = random.choice(range(55, 96))
        score = (mid1+mid2) * 0.25 + final * 0.5
        scores.append(score)
    return scores

def plotQuizzes():
    scores = generateScores(10000)
    pylab.hist(scores, 7)
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()

def probTest(limit):
    count = 1
    prob = 1 / 6.0
    while prob > limit:
        prob *= 5.0 / 6
        count += 1
    return count

if __name__ == '__main__':
    print probTest(0.5)
    print probTest(0.1)
    print probTest(0.01)
    print probTest(0.001)
    print probTest(0.0001)
