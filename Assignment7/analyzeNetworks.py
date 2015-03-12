from io import open
import pandas as pd
import networkx as nx
import numpy

def readEdgeList(filename):
	dataframe = pd.read_csv(filename)
	if len(dataframe.columns) > 2:
		print "Warning: Contains more than two columns"
		return dataframe.iloc[:,:2]
	return dataframe

def degree(edgeList, in_or_out):
	if in_or_out == 'in':
		return edgeList.ix[:,'1'].value_counts()
	elif in_or_out =='out':
		return edgeList.ix[:,'0'].value_counts()

def combineEdgeLists(edgeList1, edgeList2):
	return pd.concat([edgeList1,edgeList2]).drop_duplicates()

def pandasToNetworkX(edgelist):
	g = nx.DiGraph()
	edgeList = edgelist.to_records(index=False)
	g.add_edges_from(edgeList) 
	return g
		
def randomCentralNode(inputDiGraph):
	eig = nx.eigenvector_centrality(inputDiGraph)
	total = sum(eig.values())
	dic = {}
	for v1,v2 in eig.items():
		dic[v1] = v2/total
	return numpy.random.choice(dic.keys(), p=dic.values())

