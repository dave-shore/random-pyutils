def genealogy_chains(d, layer = 1, upstream = []):
    
    output = []
    
    for k,L in d.items():
        
        if len(L) == 0:
            output.append(upstream + [(k,layer)])
            continue
        
        if isinstance(L, list):
            for x in L:

                if isinstance(x, dict):
                    output.extend(genealogy_chains(x, layer+1, upstream + [(k,layer)]))

                elif isinstance(x, str) and "(C)" in x:
                    output.append(upstream + [(k,layer),(x,layer)])

                else:
                    pass
        
        elif isinstance(L, dict):
            for x in L.values():

                if isinstance(x, dict):
                    output.extend(genealogy_chains(x, layer+1, upstream + [(k,layer)]))

                elif isinstance(x, str) and "(C)" in x:
                    output.append(upstream + [(k,layer),(x,layer)])

                else:
                    pass
                
    return output  
