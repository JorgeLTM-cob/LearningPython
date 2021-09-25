def getMedian(vec, b, e):
        pos = (e - b) // 2
        if ((e - b) % 2 == 0):
            return (vec[b + pos])
        else:
            thismed = (vec[b + pos] + vec[b + pos + 1]) // 2
            return (thismed) 

def quartiles(arr):
        N = len(arr)
        vec = []
        arr.sort()
        half = N // 2
        vec.append(getMedian(arr,0,(half - 1)))
        if (N % 2 == 0):
            vec.append(getMedian(arr,0,(N - 1)))
            vec.append(getMedian(arr,half,(N - 1)))
        else:
            vec.append(arr[(half)])
            vec.append(getMedian(arr,(half + 1),(N - 1)))
        return(vec)

test = [3, 7, 8, 5, 12, 14, 21, 15, 18, 14]
holi = quartiles(test)
print (holi)
