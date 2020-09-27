class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def set_grid(graph, width=2):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % '.', end="")
    print()

def main():
    g = Map(30, 30)
    set_grid(g)

if __name__ == '__main__':
    main()
