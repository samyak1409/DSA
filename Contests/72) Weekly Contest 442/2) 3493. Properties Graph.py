"""
https://leetcode.com/problems/properties-graph
"""


def number_of_components(properties: list[list[int]], k: int) -> int:
    """"""

    # 1) Sub-optimal (HashSet, HashMap): TC = O(n^2 * (m+n)); SC = O(n*m)
    # [Came up with myself.]
    # Looping on all the ~n^2 pairs, and using a hashmap to track each node is part of which component.

    # Since we'd be needing to do `set(a).intersection(set(b))` for all the pairs in `properties`, it'd be O(n^2), so
    # instead of having to do `set()` `n^2` times, just convert all the arrays to hashsets once (so only `n` times
    # instead of `n^2`): TC = SC = O(n*m)
    properties = [set(arr) for arr in properties]

    ans = 0
    hm = {}  # mapping of node_idx (`i` or `j`) -> component_id (`c_id`); SC = O(n)
    c_id = 0
    # For each pair: TC = O(n^2)
    for i in range(n:=len(properties)):
        for j in range(i+1, n):
            # print(i, j)  # debug
            # If common distinct >= k, then we need to connect nodes `i` & `j`: TC = SC = O(m)
            if len(properties[i].intersection(properties[j])) >= k:
                # print('k satisfy')  # debug
                # So, we've 4 cases:
                # Case 1: Both nodes aren't in any component:
                if i not in hm and j not in hm:
                    # print('no i, no j')  # debug
                    # Assign them a component id:
                    hm[i] = hm[j] = c_id
                    c_id += 1
                    # No. of components increased, so:
                    ans += 1
                # Case 2 & 3: One node is in a component, other is not:
                # In these cases, we need to add the node to the same component:
                elif i in hm and j not in hm:
                    # print('i, no j')  # debug
                    hm[j] = hm[i]
                elif i not in hm and j in hm:
                    # print('no i, j')  # debug
                    hm[i] = hm[j]
                # Case 4: Both the nodes are in some component:
                else:  # (if i in hm and j in hm)
                    # print('i, j')  # debug
                    # In this case, we need to check if both are not in the same component:
                    if hm[i] != hm[j]:
                        # If not, we need to merge the two components:
                        # (We're changing component id of all the nodes in `j`'s component to `i`'s component id, we can
                        # do vice versa as well.)
                        c_id_to_change = hm[j]  # store since `hm[j]` would be changed in between
                        # Loop on all the nodes to find the nodes which need the change: TC = O(n)
                        for node_idx, component_id in hm.items():
                            if component_id == c_id_to_change:
                                hm[node_idx] = hm[i]
                        # No. of components decreased, so:
                        ans -= 1
                # print(hm, ans)  # debug

    # `n-len(hm)` is the no. of nodes which didn't make any edge from and to some node, so these would have 1 component
    # for each of them:
    return ans + (n-len(hm))

    # 2) Optimal (Disjoint-set): TC = O(); SC = O()
    # https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    # https://leetcode.com/problems/properties-graph/solutions
