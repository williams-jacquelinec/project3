import numpy as np
import heapq
from typing import Union

class Graph:
    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """ Unlike project 2, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or the path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """ Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. 
        Note that because we assume our input graph is undirected, `self.adj_mat` is symmetric. 
        Row i and column j represents the edge weight between vertex i and vertex j. An edge weight of zero indicates that no edge exists. 
        
        TODO: 
            This function does not return anything. Instead, store the adjacency matrix 
        representation of the minimum spanning tree of `self.adj_mat` in `self.mst`.
        We highly encourage the use of priority queues in your implementation. See the heapq
        module, particularly the `heapify`, `heappop`, and `heappush` functions.
        """

        # initiating the visited list and the adjacency matrix object
        visited = []
        adj_mat = self.adj_mat

        # determining how many vertices there are by looking at the shape of the array
        vertices = adj_mat.shape[0]

        # creating an object to reflect every vertex in the adj_mat
        all_vertices = list(range(vertices))

        # creating a new matrix for MST to exist
        mst_mat = np.array([[0 for column in range(vertices)] for row in range(vertices)])

        # creating a priority queue to start out with
        # it is a list structured as such: [ (edge weight, start node, end node), etc.]
        start = 0
        queue = []
        for i in range(0,vertices):
            if adj_mat[start][i] != 0:
                element = adj_mat[start][i], start, i
                queue.append(tuple(element))

        heapq.heapify(queue)

        # appending the start node to visited
        visited.append(start)


        # begin the while statement
        while len(visited) != len(all_vertices):

            # pop the lowest weight edge from the queue
            weight, vertex_start, vertex_end = heapq.heappop(queue)

            # if dest vertex not in visited:
                # add edge to mst matrix
                # add dest vertex to visited list
                # add outgoing edges of dest vertex to priority queue

            if vertex_end not in visited:
                mst_mat[vertex_start][vertex_end] = weight
                mst_mat[vertex_end][vertex_start] = weight
                visited.append(vertex_end)
                
                for i in all_vertices:
                    # if adj_mat[vertex_end][i] != 0:
                    heapq.heappush(queue, (adj_mat[vertex_end][i], vertex_end, i))


        self.mst = mst_mat
        # return self.mst

