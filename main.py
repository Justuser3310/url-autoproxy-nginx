from fastapi import FastAPI, HTTPException
from uuid import uuid4
app = FastAPI()

# If you don't need domain check (jetwork):
# --- comment
# multi-comments uncomment

from db import *
from domain_check import *

def set_nginx(url: str, port: int):
	f = open('/etc/nginx/nginx.conf')
	

@app.post('/api/create/{domain}/{port}')
def create(domain: str, port: int):
	# ---
	if domain_ok(domain):
		db = read()
		if domain not in db:
			token = str(uuid4())
			db[domain] = token
			write(db)
			return {'token': token}
		else:
			raise HTTPException(status_code=400, detail="Domain exist")
	else:
		raise HTTPException(status_code=400, detail="Bad domain")
	# ---
	'''
	db = read()
	if domain not in db:
		token = str(uuid4())
		db[domain] = token
		write(db)
		return {'token': token}
	else:
		raise HTTPException(status_code=400, detail="Domain exist")
	'''

@app.post('/api/set/{domain}/{port}/{token}')
def set(domain: str, port: int, token: str):
	return 200

@app.post('/api/del/{domain}/{port}/{token}')
def set(domain: str, port: int, token: str):
	return 200

if __name__ == '__main__':
	import uvicorn
	uvicorn.run(app, host='127.0.0.1', port=8000)
