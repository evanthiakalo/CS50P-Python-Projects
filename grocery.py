items ={}
try:
      while True:
           item = input().strip().upper()
           items[item]=items.get(item, 0)+1
except EOFError:
      pass
for item in sorted (items):
                print(items[item],item)
