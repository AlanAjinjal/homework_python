def proc(string):                                   
    words = string.split(' ')   
    word_count = 0                               
    for word in words:                                
        char_count = 0                                  
        for char in word:                               
            if char.isupper():                          
                char_count += 1                          
        if char_count > len(word) // 2:                 
            word_count += 1                             
    return str(word_count / len(words) * 100) + '%'     

print(proc('ABc dbE FRl Ama'))
print(proc('NDp Lka nuR vtE'))