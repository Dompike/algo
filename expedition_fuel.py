import heapq

def min_fuel_stops(n, stations, L, P):
    for i in range(n):
        stations[i] = (L - stations[i][0], stations[i][1])
    stations.sort()
    max_heap = []
    current_fuel = P
    current_pos = 0
    stops = 0
    station_idx = 0
    
    while current_pos + current_fuel < L:
        while station_idx < n and stations[station_idx][0] <= current_pos + current_fuel:
            heapq.heappush(max_heap, -stations[station_idx][1])
            station_idx += 1
        
        if not max_heap:
            return -1
        
        max_fuel = -heapq.heappop(max_heap)
        current_fuel += max_fuel
        stops += 1
    
    return stops

t = int(input())

for _ in range(t):
    n = int(input())
    
    stations = []
    for _ in range(n):
        dist, fuel = map(int, input().split())
        stations.append((dist, fuel))
    
    L, P = map(int, input().split())
    
    result = min_fuel_stops(n, stations, L, P)
    print(result)
