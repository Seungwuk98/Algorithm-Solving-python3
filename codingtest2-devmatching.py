def solution(names, homes, grades):
    st = [x+1 for x in range(len(names))]

    def qsort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if compare(pivot, x)]
        right = [x for x in arr[1:] if not compare(pivot, x)]
        return qsort(left) + [pivot] + qsort(right)

    def compare(i1, i2):
        i1 -= 1
        i2 -= 1
        if int(grades[i1]) < int(grades[i2]):
            return 1
        elif int(grades[i1]) > int(grades[i2]):
            return 0
        else:
            if homes[i1][0]**2+homes[i1][1]**2 < homes[i2][0]**2 + homes[i2][1]**2:
                return 1
            elif homes[i1][0]**2+homes[i1][1]**2 > homes[i2][0]**2 + homes[i2][1]**2:
                return 0
            else:
                if names[i1] > names[i2]:
                    return 1
                else:
                    return 0
    s = qsort(st)
    result = [0]*len(names)
    for i in range(len(names)):
        result[s[i]-1] = i+1
    return result


names, homes, gredes = ["azad", "andy", "louis", "will", "edward"], [
    [3, 4], [-1, 5], [-4, 4], [3, 4], [-5, 0]], [4.19, 3.77, 4.41, 3.65, 3.58]
print(solution(names, homes, gredes))
names, homes, gredes = ["clanguage", "csharp", "java", "python"], [
    [3, -3], [-2, 7], [-1, -1], [5, 4]], [1.27, 4.31, 4.26, 3.99]
names, homes, gredes = ["zzzzzzzzzz"], [[9999, -9999]], [1.0]
