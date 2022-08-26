def visitor_counter():
    f = open("visitor_count.txt", "r")
    old_count = f.read()        
    old_count = int("".join(old_count))        
    new_count = old_count + 1
    f.close()
    return str(new_count)