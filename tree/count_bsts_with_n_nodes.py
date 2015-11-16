def count_bsts_with_n_nodes(n):
    """Unoptimized (Non-DP) solution"""
    if n == 0 or n == 1:
        return 1
    count = 0
    for i in range(1, n + 1):
        left_count = count_bsts_with_n_nodes(i-1)
        right_count = count_bsts_with_n_nodes(n - i)
        count += left_count * right_count
    return count

print count_bsts_with_n_nodes(n=4) # 14
