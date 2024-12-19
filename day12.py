from collections import defaultdict


class Node:
    def __init__(self, i, j, token):
        self.i = i
        self.j = j
        self.token = token
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None

    def dist(self, node):
        return abs(node.i - self.i) + abs(node.j - self.j)

    def siblings(self):
        return [k for k in [self.left, self.right, self.top, self.bottom] if k is not None]

    def family(self, visited=[]):
        visited.append(self)
        for sibling in self.siblings():
            if sibling in visited:
                continue

            sibling.family(visited)

        return visited

    def vertical_sides(self):
        count = 0
        if self.left == None:
            count += 1

        if self.right == None:
            count += 1

        return count

    def horizontal_sides(self):
        count = 0
        if self.top == None:
            count += 1

        if self.bottom == None:
            count += 1

        return count

    def corners(self):
        hcount = self.horizontal_sides()
        vcount = self.vertical_sides()

        if hcount + vcount == 4:
            return 4

        counter = 0

        if hcount + vcount == 3:
            counter += 2

        if hcount == 1 and vcount == 1:
            counter += 1

        # inner corners
        if self.top and self.left:
            if self.top.left == None and self.left.top == None:
                counter += 1

        if self.left and self.bottom:
            if self.left.bottom == None and self.bottom.left == None:
                counter += 1

        if self.bottom and self.right:
            if self.bottom.right == None and self.right.bottom == None:
                counter += 1

        if self.right and self.top:
            if self.right.top == None and self.top.right == None:
                counter += 1

        return counter

    def perimeter(self):
        return 4 - len(self.siblings())


def run_part1():
    with open("day12.txt") as file:
        map = [list(line.strip()) for line in file.readlines()]

    coords_per_token = defaultdict(lambda: [])
    subgraphs = defaultdict(lambda: [])

    for i in range(len(map)):
        for j in range(len(map[0])):
            coords_per_token[map[i][j]].append((i, j))

    def in_bound(i, j):
        return i >= 0 and i < len(map) and j >= 0 and j < len(map[0])

    def build_graph(token, node, coords):
        if in_bound(node.i, node.j - 1) and map[node.i][node.j - 1] == node.token and (node.i, node.j - 1) in coords:
            coords.remove((node.i, node.j - 1))
            new_node = Node(node.i, node.j - 1, token)
            node.left = new_node
            new_node.right = node
            build_graph(token, new_node, coords)

        if in_bound(node.i, node.j + 1) and map[node.i][node.j + 1] == node.token and (node.i, node.j + 1) in coords:
            coords.remove((node.i, node.j + 1))
            new_node = Node(node.i, node.j + 1, token)
            node.right = new_node
            new_node.left = node
            build_graph(token, new_node, coords)

        if in_bound(node.i - 1, node.j) and map[node.i - 1][node.j] == node.token and (node.i - 1, node.j) in coords:
            coords.remove((node.i - 1, node.j))
            new_node = Node(node.i - 1, node.j, token)
            node.top = new_node
            new_node.bottom = node
            build_graph(token, new_node, coords)

        if in_bound(node.i + 1, node.j) and map[node.i + 1][node.j] == node.token and (node.i + 1, node.j) in coords:
            coords.remove((node.i + 1, node.j))
            new_node = Node(node.i + 1, node.j, token)
            node.bottom = new_node
            new_node.top = node
            build_graph(token, new_node, coords)

        return node

    def make_fully_connected(subgraph):
        visited = []
        family = subgraph.family(visited)
        for k in range(len(family)):
            node_k = family[k]
            for l in range(k + 1, len(family)):
                node_l = family[l]
                if node_k.dist(node_l) == 1:
                    if node_k.i < node_l.i:
                        node_k.bottom = node_l
                        node_l.top = node_k
                    elif node_k.i > node_l.i:
                        node_k.top = node_l
                        node_l.bottom = node_k
                    elif node_k.j < node_l.j:
                        node_k.right = node_l
                        node_l.left = node_k
                    elif node_k.j > node_l.j:
                        node_k.left = node_l
                        node_l.right = node_k

                    pass

    for token, coords in coords_per_token.items():
        copied_coords = coords.copy()
        while len(copied_coords) > 0:
            start = copied_coords.pop()
            start_node = Node(start[0], start[1], token)
            subgraph = build_graph(token, start_node, copied_coords)
            make_fully_connected(subgraph)
            subgraphs[token].append(subgraph)

    total = 0
    for token in subgraphs.keys():
        for token_subgraph in subgraphs[token]:
            visited = []
            family = token_subgraph.family(visited)
            family_perimeter = sum([f.perimeter() for f in family])

            chk_sum = family_perimeter * len(family)
            total += chk_sum

    print("Part 1: ", total)

    total = 0
    for token in subgraphs.keys():
        for token_subgraph in subgraphs[token]:
            visited = []
            family = token_subgraph.family(visited)
            corner_count = sum([n.corners() for n in family])
            chk_sum = corner_count * len(family)
            total += chk_sum
    print("Part 2: ", total)


def main():
    run_part1()


if __name__ == "__main__":
    main()
