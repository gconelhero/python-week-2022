# python-week-2022

Template Para a Python Week 2022 - 25 a 29 de Abril na Linux Tips

## Instruções

Este repositório é um template de um projeto Python minimo  
O programa se chama `beerlog` e está organizado com pastas
e módulos, porém a maioria dos arquivos encontra-se vazio.

A apartir deste template você poderá acompanhar as lives  
da Python week e programar junto com o Bruno e o Jeferson.

## Obtendo seu repositório

```
git clone https://github.com/gconelhero/python-week-2022
```
## Requisitos

```
cd python-week-2022
python3 -m pip install poetry
```

`Em outros ambientes pode instalar com`

```
pip install --user poetry
```

## Instalando o ambiente

```
poetry install
poetry shell
python3 -m pip install -r requirements.txt
```

Executando

```
beerlog --help
# ou
python -m beerlog --help
```
Utilizando o unicorn:
```
python3 -m pip install uvicorn
uvicorn beerlog.api:api
```

Exemplo de como adicionar uma cerveja pelo terminal:
```
beerlog add "Itaipava" "Pilsen" --flavor=4 --image=3 --cost=6
```
Exemplo de como adicionar uma cerveja pelo browser com uvicorn:
```
localhost:8000/docs
```