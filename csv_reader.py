def dist(coords1, coords2):

    # one degree in coordinates is approx 69 mi
    MI = 69
    
    x1, y1 = coords1
    x2, y2 = coords2

    x = (x2 - x1) * MI
    y = (y2 - y1) * MI

    dist = (x ** 2 + y ** 2) ** 0.5

    return dist

def main():
    filename = "us2021census.csv"
    with open(filename, mode='r') as f:
        header = f.readline()
        data = f.readlines()

    states = {"AK", "HI", "DC"}
    top48 = []
    for i in range(len(data)):
        data[i] = data[i].strip('\n')
        data[i] = data[i].split(',')
        data[i][4] = int(data[i][4])
        data[i][5], data[i][6] = float(data[i][5]), float(data[i][6])
        lst = [data[i][0], data[i][5], data[i][6]]
        if data[i][1] not in states:
            states.add(data[i][1])
            top48.append(lst)

    '''
    'data' contains the whole dataset post-processing, 'top48' contains the
    most populous city in each state in CONUS. Currently using 'top48' to
    construct the graph.
    '''

    n = len(top48)

    adj_matrix = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(i, n):
            city1 = top48[i][1], top48[i][2]
            city2 = top48[j][1], top48[j][2]
            distance = dist(city1, city2)
            adj_matrix[i][j] = distance
            adj_matrix[j][i] = distance

    output = "top48.py"

    with open(output, mode='w') as o:
        o.write("top48 = " + str(top48) + '\n')
        o.write("g = " + str(adj_matrix))

if __name__ == "__main__":
    main()
