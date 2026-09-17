from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="API de Patrimônio",
    description="API CRUD para gerenciamento de patrimônios",
    version="1.0.0"
)

class Patrimonio(BaseModel):
    nome: str
    categoria: str
    descricao: Optional[str] = None
    valor: float
    localizacao: str
    responsavel: str

class PatrimonioAtualizacao(BaseModel):
    nome: Optional[str] = None
    categoria: Optional[str] = None
    descricao: Optional[str] = None
    valor: Optional[float] = None
    localizacao: Optional[str] = None 
    responsavel: Optional[str] = None



Patrimonio = [
    {
    id = 1,
    nome = "Notebook Dell",
    categoria = "Informatica",
    descricao = "Notebook utilizado no setor administrativo",
    valor =  "3.799.00",
    localizacao = "Sala 01",
    responsavel = "Nicolas",
    },

    {
        id = 2,
    nome = "Mesa de Escritorio",
    categoria = "Movies",
    descricao = "Mesa de escritorio em madeira",
    valor =  "1.148.00",
    localizacao = "Sala 02",
    responsavel = "Vanessa",
    },
]

@app.get("/patrimonios")
def listar_patrimonios():
    return Patrimonio

@app.get("/patrimonios/{patrimonio_id}")
def buscar_patrimonio(patrimonio_id: int):

    for patrimonio in patrimonio:
        if patrimonio["id"] == patrimonio_id:
            return patrimonio

    raise HTTPException(
        status_code=404,
        detail="Patrimonio não encontrado"
    )


@app.post("/patrimonio", status_code=201)
def cadastrar_patrimonio(patrimonio: Patrimonio):

    novo_id = 1

    if patrimonio:
        novo_id = max(p["id"] for p in patrimonio) + 1

    novo_patrimonio = {
        "id": novo_id,
        ** patrimonio.model_dump()
    }

    patrimonio.append(novo_patrimonio)

    return {
        "mensagem": "Patrimonio cadastrado com sucesso!",
        "patrimonio": novo_patrimonio
    }


@app.put("/patrimonio/ {patrimonio_id}")
def atulizar_patrimonio(
    patrimonio_id: int,
    dados: PatrimonioAtualizacao
):

    for patrimonio in patrimonio:

        if patrimonio["id"] == patrimonio_id:

            dados_atualizacao = dados.model_dump(
                exclude_unset=True
            )

            patrimonio.update(dados_atualizacao)

        return {
            "mensagem": "Patrimonio atualizacao com sucesso!",
            "patrimonio": patrimonio
        }

    raise HTTPException(
        status_code=404,
        detail="Patrimônio não encontrado"
    )


@app.get("/")
def inico():
    return {
        "mensagem": "API de Patrimonio funcionado!"
        "documento": "/docs"
    }