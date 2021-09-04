def Qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                # swap
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1

        # pivot 값 자리 이동
        arr[rt], arr[pos] = arr[pos], arr[rt]
        Qsort(lt, pos - 1)
        Qsort(pos + 1, rt)


if __name__ == "__main__":
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print("Before Sort : ", end=' ')
    print(arr)
    Qsort(0, 7)
    print()
    print("After Sort : ", end=' ')
    print(arr)