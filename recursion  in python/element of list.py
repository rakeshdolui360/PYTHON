
# whwn a recursion function is ongoing. if we want intermediate term then we give print statement inside recursion .
# if we want  final term ,then we give print statement to caliing function which is outside recursion.
def el(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    return el(list,idx+1)
    
fruit=["a","b","c","d"]
el(fruit)
    
    
    
        
        