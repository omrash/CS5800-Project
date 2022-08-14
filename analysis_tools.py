INF = 9999999

def track_length(adj_matrix):
    '''
    Returns the total length of track from an input adjacency matrix
    '''
    n = len(adj_matrix)
    track = 0

    for u in range(n):
        for v in range(u + 1, n):
            track += adj_matrix[u][v]

    return track

def floyd_warshall(adj_matrix):
    '''
    Returns a matrix of distances between vertices based on the input adjacency
    matrix. Runs in O(n^3) time.
    '''
    n = len(adj_matrix)
    dist = [[INF for x in range(n)] for y in range(n)]

    for u in range(n):
        dist[u][u] = 0
        for v in range(n):
            if adj_matrix[u][v]:
                dist[u][v] = adj_matrix[u][v]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], (dist[i][k] + dist[k][j]))

    return dist


    
