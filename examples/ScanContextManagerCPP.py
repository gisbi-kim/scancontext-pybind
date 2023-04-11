import pyscancontext as sc

import numpy as np
np.set_printoptions(precision=4)


scm = sc.SCManager()


# ScanContextManager using python binding

class ScanContextManagerCPP:
    def __init__(self, shape=[20,60], num_candidates=10, threshold=0.15): # defualt configs are same as the original paper 
        self.shape = shape
        self.num_candidates = num_candidates
        self.threshold = threshold

        self.max_length = 80 # recommended but other (e.g., 100m) is also ok.

        self.ENOUGH_LARGE = 15000 # capable of up to ENOUGH_LARGE number of nodes 
        self.ptclouds = [None] * self.ENOUGH_LARGE
      
        self.curr_node_idx = 0

    def addNode(self, node_idx, ptcloud):
        scm.add_node(ptcloud)
        self.curr_node_idx = node_idx
        self.ptclouds[node_idx] = ptcloud
       
     
    def getPtcloud(self, node_idx):
        return self.ptclouds[node_idx]

    def detectLoop(self): 
        return scm.detect_loop()