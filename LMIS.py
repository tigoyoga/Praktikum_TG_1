def lis(arr):
    def _lis(n, max_ref):
        nonlocal arr
        if n == 1:
            return [arr[0]]

        result = [arr[0]]
        for i in range(1, n):
            res = _lis(i, max_ref)
            if arr[i - 1] < arr[n - 1] and len(res) + 1 > len(result):
                result = res + [arr[n - 1]]

        if len(max_ref) < len(result):
            max_ref[:] = result[:]

        return result

    max_result = [arr[0]]
    _lis(len(arr), max_result)

    return max_result


# Driver program to test above function
arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]

result = lis(arr)

print("Hasil Largest Monotonically Increasing Subsequence:", result)
