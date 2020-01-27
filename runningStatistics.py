import math 

def running_mean(x, i, mean, delta):
    delta = x - mean
    mean  = mean + delta / i
    return mean, delta

def running_variance(x, i, mean, msq):
    delta = x - mean
    mean  = mean + delta / i
    msq   = msq + delta * ( x - mean )
    return msq, mean, delta

def compute_statistics(samples):
    sum = 0
    sumsqrd = 0
    for i in range(n):
        sum = sum + samples[i]
        sumsqrd = sumsqrd + samples[i] * samples[i]

    average = sum/n
    print("mean:    ", average)

    variance = ( sumsqrd + n * average * average - 2 * average * sum ) / n
    print("variance:        ", variance)

if __name__ == "__main__":

    samples = [1640, 1640.5, 1640.3, 1641, 1640.7, 1640.5, 1640.7, 1640.9, 1640, 1641]
    n = len( samples )
    print("num samples: ", n)


    compute_statistics( samples )

    # Running algorithms
    i = 0
    mean = 0
    delta = 0
    for x in samples:
        i = i + 1
        mean, delta = running_mean(x, i, mean, delta)
    print("mean: ", mean)

    i = 0
    mean = 0
    delta = 0
    msq = 0
    for x in samples:
        i = i + 1
        msq, mean, delta = running_variance(x, i, mean, msq)
    print("variance: ", msq / n)
