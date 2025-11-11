# (IDE) LiteLLM — Guia de Instalação e Execução Local

> **TFC DEISI APPS — Confluence**

---

## Pré-requisitos

1. Ter **Docker** e **Docker Compose**
2. **Python 3.13**
3. Ter o **Pip** atualizado
4. Ter o **Git** instalado
5. **PyCharm Ultimate Edition** (de preferência)

> “A simplicidade é o último nível de sofisticação.” — *Prof. Martim Mourão*

---

## Passo-a-Passo

### 1️⃣ Clonar o Repositório

Abrir o **PyCharm** → “New Project From Version Control”  
e colocar o link do repositório:

```
https://github.com/BerriAI/litellm
```

> ⚠️ Pode demorar um bocado — é normal.

O PyCharm vai criar um **Virtual Environment**.  
É importante que o **base interpreter** esteja em **Python 3.13**.

---

### 2️⃣ Configurar o Interpreter

No canto inferior direito, onde diz “No Interpreter”:

1. Clicar em **Add new Interpreter**
2. Selecionar **Add local Interpreter**
3. Escolher **Select existing interpreter**  
   → a localização tem de estar na pasta `.venv`

Depois é só escolher o ambiente que criaste. (Python 3.13 virtualenv at …)

---

### 3️⃣ Criar o ficheiro `.env` na raiz do projeto

Adicionar o seguinte conteúdo:

```env
DATABASE_URL=postgresql://llmproxy:dbpassword9090@localhost:5432/litellm
LITELLM_MASTER_KEY=palvesadminkey     # (podes definir uma password à tua escolha)
STORE_MODEL_IN_DB=True                # opcional
```

---

### 4️⃣ Ativar o Ambiente Virtual

No terminal do PyCharm, ativa o `.venv` (se ainda não estiver ativo):

**Windows**
```
.venv\Scripts\activate
```

**macOS / Linux**
```
source .venv/bin/activate
```

---

### 5️⃣ Atualizar e Instalar Dependências

Verifica se o `pip` está atualizado:

```
python.exe -m pip install --upgrade pip
```

Depois instala os pacotes base:

```
pip install --upgrade pip setuptools wheel
```

Agora instala os requisitos do projeto:

```
pip install -r requirements.txt --no-build-isolation
```

> Tivemos de usar `--no-build-isolation` porque o `uvloop` não tem suporte nativo para Windows.

Se aparecer o erro:

```
RuntimeError: uvloop does not support Windows at the moment
```

Ignora — é normal.

---

### 6️⃣ Instalar e Configurar o Prisma

```
pip install prisma
prisma generate
```

---

### 7️⃣ Instalar o LiteLLM

```
pip install litellm
pip install 'litellm[proxy]'
```

---

### 8️⃣ Configurar Execução no PyCharm

No menu superior, vai a:

**Run → Edit Configurations**

1. Clicar no ícone “+” → escolher **Python**
2. **Name:** `LiteLLM-Local` (por exemplo)
3. **Escolher:** o Python 3.13 virtualenv (`.venv`)
4. Mudar de **Script** para **Module**, e meter:
   ```
   litellm.proxy.proxy_cli
   ```
5. **Working directory:** escolher a pasta raiz do projeto
6. **Environment variables:**
   ```
   PYTHONUNBUFFERED=1;LITELLM_MASTER_KEY=palvesadminkey
   ```
7. **Path to ".env" files:** escolher o ficheiro `.env`
8. Deve ficar algo assim:

<img src="exemplo-config.png" alt="Exemplo de configuração no PyCharm" width="550">




---

## Base de Dados (Docker Compose)

Executar o comando para criar apenas a base de dados usada pelo LiteLLM:

```
docker compose up db -d
```

Depois:

```
prisma generate --schema=./litellm/proxy/schema.prisma
prisma db push --schema=./litellm/proxy/schema.prisma
```

---

## Aceder à Aplicação

Depois de tudo configurado, podes **dar Run no PyCharm**  
e aceder a:

```
http://localhost:4000
```

Credenciais de login:

```
username : admin
password : palvesadminkey   # (definida no .env)
```

---

## Extra

Se quiseres visualizar a base de dados, podes usar o **DBeaver**:

<img src="exemplo-dbeaver.png" alt="Config Dbeaver" width="550">


| Campo | Valor |
|--------|-------|
| **HOST** | localhost |
| **DATABASE** | litellm |
| **PORT** | 5432 |
| **USERNAME** | llmproxy |
| **PASSWORD** | dbpassword9090 |

Pode ser útil criares um novo utilizador e atribuir-lhe uma password,  
já que na dashboard do localhost só consegues definir o email e o *role*.

---

## Autores

**Afonso Sá** — a22304875  
**Lucas Martins** — a22403073
