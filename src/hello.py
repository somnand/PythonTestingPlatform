import sys
import scipy
import numpy
from sklearn import svm
from sklearn import datasets 
#Python version
print('Python: {}'.format(sys.version))
#Scipy version
#print('Scipy: {}'.format(scipy.__version__))
#numpy version 
print('Numpy: {}'.format(numpy.__version__))
#Sci-Kit Learn
#print("Scikit Learn: {}".format(sklearn.__version__))

#Iris - Dataset - Supervised ML
iris = datasets.load_iris() 
print('Type of Iris data-set {} '.format(type(iris)))



