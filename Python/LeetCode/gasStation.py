"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""

class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}

    # Naive solution: will have TLE
    def canCompleteCircuit1(self, gas, cost):
        for i in xrange(len(gas)):
            ngas = gas[i:] + gas[0:i]
            ncost = cost[i:] + cost[0:i]
            remain = 0
            for j in xrange(len(ngas)):
                remain += (ngas[j] - ncost[j])
                if remain < 0:
                    break
            if remain >= 0:
                return i
        return -1

    # Revised one, a little more improved, but still not good enough (2000ms AC)
    def canCompleteCircuit2(self, gas, cost):
        for x in xrange(len(gas)):
            remain = 0
            fail = False
            for i in xrange(x, len(gas)):
                remain += (gas[i] - cost[i])
                if remain < 0:
                    fail = True
                    break
            print 1, remain, x
            if not fail:
                for j in xrange(0, x):
                    remain += (gas[j] - cost[j])
                    if remain < 0:
                        break
                print 2, remain, x
                if remain >= 0:
                    return x
        return -1

    # A real good solution
    # If i is solution for station[0..n], there must not exist a k that sum[k:i-1] > 0
    # otherwist the solution should be k. so sum[k:i-1] < 0
    # Which also means, sum[i:n] must > 0
    # Then the problem becomes: find the last k make sum[k:i-1] < 0, so [i:n] is the longest subarray
    # that fullfill sum[i:n] > 0
    # O(n) time, boom!
    def canCompleteCircuit(self, gas, cost):
        sum = 0
        total = 0
        for i in xrange(len(gas)):
            sum += (gas[i] - cost[i])
            total += (gas[i] - cost[i])
            if sum < 0:
                k = i
                sum = 0
        if total < 0:
            return -1
        else:
            return k + 1

so = Solution()
print so.canCompleteCircuit([2,3,1],[3,1,2])
