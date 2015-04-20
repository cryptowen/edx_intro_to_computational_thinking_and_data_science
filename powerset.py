# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2 ** N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """
    N = len(items)
    for i in xrange(3 ** N):
        combo1 = []
        combo2 = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i / 3 ** j) % 3 == 1:
                combo1.append(items[j])
            if (i / 3 ** j) % 3 == 2:
                combo2.append(items[j])
        yield combo1, combo2


if __name__ == '__main__':
    print('powerSet', list(powerSet([1, 2, 3, 4, 5])))
    print(list(yieldAllCombos([1, 2, 3])))
