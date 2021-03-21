# Interpolações Polinomiais

## Instalação

### Requisitos


* [Python 3.8+](https://tecadmin.net/install-python-3-8-ubuntu/)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

### Script

Na raiz do projeto, executar no terminal:
```bash
$ virtualenv --python=python3 venv \
&& source venv/bin/activate \
&& pip install --upgrade pip \
&& pip install -r requirements.txt --no-cache-dir
```

## Execução

Na raiz do projeto, executar no terminal o script:
```bash
$ ./main.py
```

O gráfico das interpolações é gerado em `img/interpolations.png`.