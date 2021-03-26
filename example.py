import numpy as np
import h5py

def getWeightsFromLabels(labelStack):
	h = h5py.File(labelStack, 'r')
	data = np.array(h['dataset_1'])
	h.close()
	unique, counts = np.unique(data, return_counts=True)
	d = dict(zip(unique, counts))
	zeros = d[0]
	ones = d[1]
	twos = d[2]
	nSamples = [zeros, ones, twos]
	m = max(nSamples)
	zeroWeight = zeros / m
	oneWeight = ones / m
	twoWeight = twos / m
	normedWeights = [1 - (x / sum(nSamples)) for x in nSamples]
	return normedWeights

print(getWeightsFromLabels("profLabels.h5"))