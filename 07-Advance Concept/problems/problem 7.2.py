l = ['python', 'rocks', 'ai']

result = [n for w in l if (n:=len(w))>4]
print(result)