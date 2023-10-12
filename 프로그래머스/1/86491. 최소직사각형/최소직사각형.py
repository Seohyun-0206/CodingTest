def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    
    max_h = -1
    max_w = -1
    for w, h in sizes:
        if max_h < h:
            max_h = h
        if max_w < w:
            max_w = w
    
    return max_w * max_h