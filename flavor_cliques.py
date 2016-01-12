# coding: utf-8
from flavors import *
from flavor_matrix import *

MIN_CLIQUE_SIZE = 3


def get_neighbors(vertex):
    """Return an array of neighbors for a given vertex."""
    neighbors = []
    for idx, item in enumerate(FLAVOR_MATRIX[vertex]):
        if item == 1:
            neighbors.append(idx)

    return neighbors


# See https://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm for details.
def bron_kerbosch(R, P, X):
    """Bron-Kerbosch recursive algorithm."""
    if not P and not X:
        # P and X are empty, so yield R as a maximal clique if it is bigger
        # than the minimum allowed clique size.
        if len(R) >= MIN_CLIQUE_SIZE:
            yield R

    # Iterate over each vertex in a COPY of P
    for vertex in P[:]:
        # Recurse by running Bron-Kerbosch(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        R_i = R + [vertex]
        P_i = [i for i in P if i in get_neighbors(vertex)]
        X_i = [i for i in X if i in get_neighbors(vertex)]

        for r in bron_kerbosch(R_i, P_i, X_i):
            yield r

        # P := P \ {v}
        # X := X ⋃ {v}
        P.remove(vertex)
        X.append(vertex)


flavor_cliques = list(bron_kerbosch([], range(99), []))

for clique in flavor_cliques:
    for flavor_id in clique:
        print FLAVORS[flavor_id]
    print ""
