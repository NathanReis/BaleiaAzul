# Docker Manager

## Iniciando API

Todos comandos abaixo estão considerando que seu terminal está na pasta raiz do projeto.

### Windows

```cmd
cd api

py -3 -m venv venv
venv\Scripts\activate

venv\Scripts\python.exe -m ensurepip --upgrade
pip install -r requirements.txt

flask run
```

**Obs. 1:** Execute no `cmd` pois seu `PowerShell` pode bloquear a execução do `venv`.

**Obs. 2:** Não foi criado um script para `Windows` pois após ativar o `venv`, os próximos comandos não são executados.

### Linux

```bash
bash ./start.sh
```
