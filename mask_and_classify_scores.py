import numpy as np

def mask_and_classify_scores(arr):
    """
    write your solution here;
    follow the instructions in the README.
    """
    ### Replace with your own code (begin) ###
    if (not isinstance (arr, np.ndarray)) or (arr.ndim != 2 or arr.shape[0] != arr.shape[1]) or arr.shape[0] < 4:
        return None
    
    cleaned = np.array([[0 if x < 0 
                        else 100 if x > 100
                        else x 
                        for x in row]
                        for row in arr])
    
    levels = np.array([[0 if x < 40 
                         else 1 if 40 <= x < 70 
                         else 2 for x in row]
                         for row in arr])
    
    row_pass_counts = []
    for row in cleaned:
        count = 0
        for x in row:
            if x >= 50:
                count += 1
        row_pass_counts.append(count)
        
    row_pass_counts = np.array(row_pass_counts)
    
    return (cleaned, levels, row_pass_counts)
    
    ### Replace with your own code (end)   ###