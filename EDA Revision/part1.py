import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError ("List must contain nine numbers.")
        
    lst = np.reshape(lst,(3,3))
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    calculations ={'mean':m.copy(),
          'variance':m.copy(),
          'standard deviation':m.copy(),
          'max':m.copy(),
          'min':m.copy(),
          'sum':m.copy() }
    #columns statistics
    col_mean,col_var ,col_std ,col_max ,col_min,col_sum=[],[],[],[],[],[]
    for i in range (3):
        col_mean.append(np.mean(lst[:,i]))
        col_var.append((np.var(lst[:,i])))
        col_std.append(np.std(lst[:,i]))
        col_max.append(np.max(lst[:,i]))
        col_min.append(np.min(lst[:,i]))
        col_sum.append(np.sum(lst[:,i]))

    calculations['mean'][0] = col_mean
    calculations['variance'][0] = col_var
    calculations['standard deviation'][0] = col_std
    calculations['max'][0] = col_max
    calculations['min'][0] = col_min
    calculations['sum'][0] = col_sum

    #rows statistics
    calculations['mean'][1] = [np.mean(row) for row in lst]
    calculations['variance'][1] = [np.var(row) for row in lst]
    calculations['standard deviation'][1] = [np.std(row) for row in lst]
    calculations['max'][1] = [max(row) for row in lst]
    calculations['min'][1] =[min(row) for row in lst]
    calculations['sum'][1] =[sum(row) for row in lst]

    #all elements statistics
    calculations['mean'][2] = np.mean(lst)
    calculations['variance'][2] = np.var(lst)
    calculations['standard deviation'][2] = np.std(lst)
    calculations['max'][2] = np.max(lst)
    calculations['min'][2] = np.min(lst)
    calculations['sum'][2] = np.sum(lst)
    return calculations


calculate([0,1,2,3,4,5,6,7,8])