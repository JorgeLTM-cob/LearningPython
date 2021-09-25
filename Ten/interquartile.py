def getMedian(vec, b, e):
    pos = (e - b) // 2
    if (((e - b) % 2 ) == 0):
        return(vec[b + pos]/1)
    else:
        thismed = (vec[b + pos] + vec[e - pos]) / 2
        return(thismed)

def interQuartile(values, freqs):
    N = len(freqs)
    S = []
    q3 = 0

    for i in range(0,N):
       for j in range(0,freqs[i]):
          S.append(values[i])
    S.sort()
    N = len(S)
    half = N//2
    q1 = getMedian(S,0,(half - 1))
    if ((N % 2) == 0):
        q3 = getMedian(S,half,(N - 1))
    else:
        q3 = getMedian(S,(half + 1), (N - 1))
    
    q3 -= q1
    print(round(q3,1))

values = [3, 18, 13, 12, 5, 7]
freqs = [1, 1, 1, 1, 1, 1]
interQuartile(values, freqs)
