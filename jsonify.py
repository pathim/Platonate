import json

res={}

with open("concepts.txt") as f:
	for i,line in enumerate(f):
		line=line.strip()
		key=i
		res[key]={'description':line}

print(json.dumps(res))
