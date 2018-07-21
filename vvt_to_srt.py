import os


directory = input()

lst = os.listdir(directory)
for i in [l for l in lst if l.endswith('.vtt')]:
    fi = open(os.path.join(directory, i), 'r')
    text = fi.read()
    
    fo = open(os.path.join(directory, i.replace('.vtt', '.srt')), 'w')
    
    counter = 0
    last_char = ''
    
    # get the first double \n
    for char in text:
        if char == '\n' and last_char == '\n':
            counter = counter + 1
            fo.write('\n' + str(counter))
        
        if counter==0:
            last_char = char
            continue
        
        fo.write(char)
        
        last_char = char
    
    fi.close()
    fo.close()
    print("Done for file ", i)