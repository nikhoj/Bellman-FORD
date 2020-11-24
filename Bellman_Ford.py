def  bellman_ford(Graph, source):  #Graph = filepath, source = 1
    #code start here
    import time
    import numpy as np
    import pandas as pd
    
    start = time. time()
    file1 = Graph
    X = np.genfromtxt(file1, comments = 'c')
    l = len(X) - 1
    #adjacency list start from here
    vlist = []
    weightlist = []
    maxwt = 0
    for i in range(1,l):
        vlist.append(X[i,1])
        weightlist.append((X[i,1],X[i,2]))
        
    vdict = dict.fromkeys(vlist)
    wdict = dict.fromkeys(weightlist)
    
    for i in range(1,l):
        vdict[X[i,1]] = []
        wdict[(X[i,1],X[i,2])] = X[i,3]
        
    for i in range(1,l):
        vdict[X[i,1]].append(X[i,2])
        #wdict[(X[i,1],X[i,2])].append(X[i,3])
        if maxwt <= X[i,3]:
            maxwt = X[i,3]
        
    #adjacency list start from here
    
    #initialization  start
    n = len(vdict.keys())
    source = source
    dist = {}
    pred= {}
    for key in vdict:
        dist[key] = maxwt*n
        pred[key] = -1
    dist[source] = 0
    pred[source] = 0
    Q = [source]
    
    
    #initialization    end
    
    #Algorithm start here
    
    while Q != []:
        u = Q[0]
        Q.pop(0)
        for v in vdict[u]:
            if dist[v] > dist[u] + wdict[u,v]:
                dist[v] = dist[u] + wdict[u,v]
                pred[v] = u
                if v not in Q:
                    Q.append(v)
    
    #Algorithm end here
    #printing start here
    df = np.zeros((n, 3))
    i = 0
    for key in vdict:
        a = key
        b = dist[a]
        c = pred[a]
        df[i] = [a, b, c]
        i = i+1
    
    dataset = pd.DataFrame({'V' : df[:,0], 'Dist' : df[:,1],'Pred' : df[:,2]})
    dataset.to_csv('f.csv' , sep = '\t', index =False)
    #printing end here
    end = time. time()
    print(end - start)
    
    #code end here
    


