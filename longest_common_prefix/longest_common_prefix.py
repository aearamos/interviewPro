# test cases
#words = ['helloworld', 'hellokitty', 'hell']
#words = ['akshat', 'akash', 'akshay', 'akshita']
#words = ['car', 'camel']

first_input = input ("Enter the names you want to find a common prefix: ")
words = list(first_input.split(' '))

prefix = words[0]
#print(len(prefix))
for word in words[1:]:    
    while word[:len(prefix)] != prefix:
        prefix = prefix[:len(prefix)-1]
#        print (prefix)
    if not prefix:
        print ("no common prefix")
res = prefix

print('The common prefix between '+ str(words) + ' is '+str(res)+'.')
