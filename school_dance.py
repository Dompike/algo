def solve_dance_pairs():
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(k):
        boy, girl = map(int, input().split())
        adj[boy].append(girl)
    pair_boy = [0] * (n + 1)
    pair_girl = [0] * (m + 1)

    def find_augmenting_path(u, visited):
        for v in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            if pair_girl[v] == 0 or find_augmenting_path(pair_girl[v], visited):
                pair_boy[u] = v
                pair_girl[v] = u
                return True
        return False

    matching_size = 0

    for boy in range(1, n + 1):
        visited = [False] * (m + 1)
        if find_augmenting_path(boy, visited):
            matching_size += 1
    print(matching_size)

    for boy in range(1, n + 1):
        if pair_boy[boy] != 0:
            print(boy, pair_boy[boy])

solve_dance_pairs()