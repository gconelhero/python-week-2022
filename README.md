# python-week-2022

Template Para a Python Week 2022 - 25 a 29 de Abril na Linux Tips

## Instruções

Este repositório é um template de um projeto Python mínimo  
O programa se chama `beerlog` e está organizado por pastas
e módulos.

## Requisitos (mais informações no arquivo requirements.txt)

Testado com Python 3.8.10
***Não testado em outras versões***

Git
```
# Ambiente Linux (Debian/Ubuntu)
sudo apt-get install git

# Ambiente Windows (Siga as instruções do link abaixo)
https://git-scm.com/download/win
```

uvicorn **OPCIONAL!**

## Obtendo repositório e o poetry!

```
git clone https://github.com/gconelhero/python-week-2022
```
## Ambiente Linux (Debian/Ubuntu)
```
cd python-week-2022
python3 -m pip install poetry
```

## Ambiente Windows
```
cd python-week-2022
pip install --user poetry
```
### ou
```
python.exe -m pip install poetry
```

## Instalando o ambiente e requisitos!

```
poetry shell
python3 -m pip install -r requirements.txt
```

## Executando

```
python3 -m beerlog --help
python3 -m beerlog list # Para listar a tabela com os valores
# ou
poetry beerlog --help
poetry beerlog list
```

## Utilizando o uvicorn:

```
python3 -m pip install uvicorn
uvicorn beerlog.api:api
```

Exemplo de como adicionar uma cerveja pelo terminal:

```
python3 -m beerlog add "Itaipava" "Pilsen" --flavor=4 --image=3 --cost=6
poetry run beerlog add "Itaipava" "Pilsen" --flavor=4 --image=3 --cost=6
```
Exemplo de como adicionar uma cerveja pelo browser com uvicorn:

```
localhost:8000/docs
```