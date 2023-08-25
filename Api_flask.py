from fastapi import FastAPI
from flask import jsonify
import nest_asyncio
from pyngrok import ngrok
import uvicorn
import pandas as pd

app = FastAPI()

@app.get('/')
async def home():

    caminho_arquivo = 'arquivo.xlsx'
    df = pd.read_excel(caminho_arquivo)
    json_data = df.to_json(orient='records')

    return json_data


ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)