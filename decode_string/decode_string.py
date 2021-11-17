import re
def decodeString(strin):
    temp = ""
    j = 0
    i = 0
    while strin.count('[') > 1:
        last = strin.rfind('[')
        multiplier = strin[last - 1]
        m = re.search(r"[0-9]\[(\w+)\]", strin[last-1:])
        par = m.group(1)*int(multiplier)
        test = strin.replace(m.group(0), par)
        strin = test
    else:
        strin = strin
        
    while(i < len(strin)):
        if (strin[i] >= "0"):
             
            # Subtract '0' to convert char to int
            num = ord(strin[i])-ord("0")
           
            if (strin[i+1] == '['):
                 
                # Characters within brackets
                j = i + 1
                while(strin[j] != ']'):
                    if ((strin[j] >= 'a' and strin[j] <= 'z') or \
                        (strin[j] >= 'A' and strin[j] <= 'Z')):
                        temp += strin[j]
                    j += 1
                     
                # Expanding
                for k in range(1, num + 1):
                    print(temp,end="")
                     
                # Reset the variables
                num = 0
                temp = ""
                if (j < len(strin)):
                    i = j
            
        i += 1
        return temp
decodeString('2[a2[b]4[c]]')
# abbcabbc
