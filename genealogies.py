def genealogy_chains(d, layer = 1, upstream = []):
  
    '''
    Function to retrieve genealogy chains in a dict-list mixed structure.
    
    :param d: dict, Genealogy data structure.
    :param layer: int, Layer counter NOT TO BE CHANGED UNLESS YOU WANT THE COUNTER TO START FROM N > 1.
    :param upstream: list, List of upstream nodes NOT TO BE CHANGED UNLESS YOU WANT TO INCLUDE NODES A-PRIORI.
    
    :return: list(list)
    '''
    
    output = []
    
    for k,L in d.items():
        
        upstream += [(k,layer)]
        
        if len(L) == 0:
            output.append(upstream)
            continue
            
        if isinstance(L, list):
        
            for x in L:

                if isinstance(x, dict) or is:
                    output.extend(genealogy_chains(x, layer+1, upstream))

                elif isinstance(x, str) and "(C)" in x:
                    output.append(upstream + [(x,layer)])

                else:
                    pass
                  
        elif isinstance(L, dict):
          
            for x in L.values():

                if isinstance(x, dict) or is:
                    output.extend(genealogy_chains(x, layer+1, upstream))

                elif isinstance(x, str) and "(C)" in x:
                    output.append(upstream + [(x,layer)])

                else:
                    pass
                
    return output  
