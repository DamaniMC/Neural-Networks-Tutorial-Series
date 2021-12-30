import numpy as np

class NeuralNetwork():
    def __init__(self,layer_sizes):
        self.activations=[np.zeros((num_rows,1)) for num_rows in layer_sizes]
        self.biases=[np.zeros((num_rows,1))for num_rows in layer_sizes[1:]]
        self.weight_shapes=[(a,b) for a,b in zip(layer_sizes[1:],layer_sizes[:-1])]
        self.weights=[np.random.standard_normal(shape) for shape in self.weight_shapes]        
    def outputActivations(self):
        print("\nActivations:")
        for a in self.activations:
            print(a,"\n")
    def outputBiases(self):
        print("\nBiases:")
        for b in self.biases:
            print(b,"\n")
    def outputWeights(self):
        print("\nWeights:")
        for w in self.weights:
            print(w,"\n")
    
    