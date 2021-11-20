# 🐋 Baleia Azul 🐳

Uma ferramenta que permite o gerenciamento de imagens e containers para ser usada no navegador, utiliza a API do Docker para executar todas suas funcionalidades.

---

## 🚀 Funcionalidades

- Imagem
  - Baixar uma
  - Listar todas
  - Visualizar uma
  - Apagar todas
  - Apagar uma

- Container
  - Executar um
  - Parar um
  - Iniciar um
  - Reiniciar um
  - Apagar todos
  - Apagar um

---

## ❗ Requisitos (Ambiente de desenvolvimento)

- Docker Engine v19.03 (mínimo)
- Docker Compose
- Editor de texto qualquer
- Git
- Python v3.9 (não é garantido o funcionamento em versões anteriores)

---

## 🐔🥚 pra funcionar (Ambiente de desenvolvimento)

> ### ⚠ Avisos
>
> Todos comandos abaixo estão considerando que seu terminal esteja na pasta raiz do projeto. Ou seja, onde está este README.
>
> Caso esteja no Windows, utilize o `cmd` pois todos comandos foram usados apenas nele.

### Clone o projeto

```bash
git clone https://github.com/NathanReis/BaleiaAzul.git
```

### Configure variáveis ambiente

Faça uma cópia do arquivo `.env.example` dentro do diretório `api`.

#### Linux

```bash
cd api

cp .env.example .env
```

#### Windows

```bash
cd api

copy .env.example .env
```

Ele contém todas variáveis de ambiente usadas pela API e pelos containers.

Edite o arquivo `.env` que foi gerado passando os valores das seguintes varáveis:

- DOCKER_API_HOST
- DB_USERNAME
- DB_PASSWORD

### Inicie os containers

```bash
docker-compose up -d
```

Quando subir os container, os seguintes serviços estarão funcionando:

- **Grafana:** A aplicação responsável pelos dashboards das estatisticas dos containers.
- **MongoDB:** Responsável por armazenar os dados históricos dos containers.
- **Mongo Express:** Uma interface WEB para gerenciamento do MongoDB.
- **NGINX:** O servidor WEB que irá cuidar do front-end.

### Inicie a API

#### Linux

```bash
cd api

python3 -m venv venv
. venv/bin/activate

python3 -m ensurepip --upgrade
pip install -r requirements.txt

flask run
```

#### Windows

```cmd
cd api

py -3 -m venv venv
venv\Scripts\activate

venv\Scripts\python.exe -m ensurepip --upgrade
pip install -r requirements.txt

flask run
```

Para auxiliar no consumo dela, foi deixado do arquivo de sua collection dentro do diretório `api`, ele se chama `ApiCollection.json`.

**Obs.:** Após iniciar a API, o terminal onde os comandos foram executados ficará ocupado.

### Inicie o script para armazenar os dados históricos

#### Linux

```bash
cd api

. venv/bin/activate
python3 save_containers_stats_job.py
```

#### Windows

```cmd
cd api

venv\Scripts\activate
venv\Scripts\python.exe save_containers_stats_job.py
```

Este script cria um job que fica a cada 10 segundos consultando os status de todos containers e fazendo a persistência dos mesmos no MongoDB.

**Obs.:** Após iniciar o script, o terminal onde os comandos foram executados ficará opucado.

💥 **Tudo pronto para uso** 💥

---

## Aproveitando

- **Porta 80 (WEB):** O front-end feito utilizando HTML, CSS, JavaScript básico
- **Porta 3000 (WEB):** O dashboard feito utilizando o Grafana
- **Porta 5000 (API):** A API para gerenciamento das imagens e containers
- **Porta 8081 (WEB):** O Mongo Express para gerenciamento do banco via interface WEB
- **Porta 27017 (Serviço):** O MongoDB utilizado para armazenar os dados históricos

---

## 🤓🤓🤓🤓

| Nome                        | R.A.      |
| --------------------------- | --------- |
| Nathan da Silva Reis        | 082170036 |
| Silas Hikaru Hiuga          | 082170028 |
| Vitor de Oliveira Lupinetti | 082170031 |
| William de Almeida Oliveira | 082170032 |

---

## Demonstração

- [🎬 YouTube](https://youtu.be/RkHG-HO697Q) > Funcionamento
