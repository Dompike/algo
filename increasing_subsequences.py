def count_increasing_subsequences(n, arr):
    MOD = 10 ** 9 + 7

    unique_vals = sorted(set(arr))
    val_map = {v: i + 1 for i, v in enumerate(unique_vals)}
    m = len(unique_vals)

    bit = [0] * (m + 1)

    def add(idx, val):
        while idx <= m:
            bit[idx] = (bit[idx] + val) % MOD
            idx += idx & -idx

    def sum_range(idx):
        result = 0
        while idx > 0:
            result = (result + bit[idx]) % MOD
            idx -= idx & -idx
        return result

    total = 0

    for num in arr:
        compressed_val = val_map[num]
        prev_count = sum_range(compressed_val - 1)
        curr_count = (prev_count + 1) % MOD
        total = (total + curr_count) % MOD
        add(compressed_val, curr_count)

    return total

n = int(input())
arr = list(map(int, input().split()))
result = count_increasing_subsequences(n, arr)
print(result)