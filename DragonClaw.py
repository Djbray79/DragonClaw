class Map1:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def set_grid(graph, width=2):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % '.', end="")
    print()

def main1():
    g = Map1(30, 15)
    set_grid(g)

if __name__ == '__main1__':
    main1()
