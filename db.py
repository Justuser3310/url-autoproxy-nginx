import os
import json

if not os.path.exists('domains.json'):
	db = {}
	js = json.dumps(db, indent=2)
	with open("domains.json", "w") as outfile:
		outfile.write(js)
	print('Created new domains.json')

def read(file = 'domains.json'):
	with open(file, "r", encoding="utf-8") as openfile:
		db = json.load(openfile)
	return db

def write(db, file = 'domains.json'):
	js = json.dumps(db, indent=2, ensure_ascii=False)
	with open(file, "w", encoding="utf-8") as outfile:
		outfile.write(js)
