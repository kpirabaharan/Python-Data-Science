from sklearn.datasets import load_boston

boston = load_boston()
boston.keys()
print(boston['DESCR'])