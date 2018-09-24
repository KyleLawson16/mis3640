def move(n, source, bridge, destination):
    if n == 1:
        print(f'{source} --> {destination}')
    else:
        move(n - 1, source, destination, bridge)
        print(f'{source} --> {destination}')
        move(n - 1, bridge, source, destination)

move(4, 'A', 'B', 'C')
