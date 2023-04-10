

f = open('s3.gr','r')
raw = f.readlines()
edges = raw[8:]

edges = [edge.split()[1:] for edge in edges]
print(edges)