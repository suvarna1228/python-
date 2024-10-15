def rearrange_alternate(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    
    result = []
    i, j = 0, 0
    pos_turn = True
    
    while i < len(pos) and j < len(neg):
        if pos_turn:
            result.append(pos[i])
            i += 1
        else:
            result.append(neg[j])
            j += 1
        pos_turn = not pos_turn
    
    result.extend(pos[i:])
    result.extend(neg[j:])
    
    return result

arr = [1, 2, 3, -1, -2, -3, -4, 4]
print(rearrange_alternate(arr))
