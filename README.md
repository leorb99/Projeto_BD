# Projeto individual da disciplina Bancos de Dados 2023/1
O projeto foi desenvolvido em python usando o framework Flask.

## Setup do ambiente

É necessário alguns procedimentos antes de rodar o programa.

Antes de tudo, clone o repositório
```
git clone https://github.com/leorb99/Projeto_BD
```
Recomendo que instale o virtualenv, mas antes certifique-se de que tem o pip3 instalado, caso não tenha instale com
```
sudo apt install python3-pip
```
```
pip3 install virtaulenv
```
Vá para o diretório do projeto e inicie o ambiente virtual 
```
virtualenv -p python3 venv
```
Ative o ambiente virtual
```
. venv/bin/activate
```
Instale as bibliotecas que estão no arquivo requirements.txt
```
pip3 install -r requirements.txt
```
Certifique-se de que o MySQL esteja instalado, caso não tenha instalado siga o tutorial
 [neste link](https://ubuntu.com/server/docs/databases-mysql).

Para criar o banco de dados e as tabelas, execute o comando no terminal.
```
mysql -u <seu_usuario_mysql> -p < CREATE.sql
```
Depois de executar entre com sua senha e o banco de dados deve ser criado.
Confira se o banco de dados foi criado. Você pode fazer isso no MySQL Workbench ou pelo terminal.
```
mysql -u <seu_usuario_mysql> -p
```
Entre com sua senha e execute os seguintes comandos
```
SHOW DATABASES;
```
AvaliaUnB deve aparecer entre os databases
```
USE AvaliaUnB;
```
Assim você deve conseguir ver as tabelas do banco de dados.
Execute o próximo comando para popular o banco de dados.
```
mysql -u <seu_usuario_mysql> -p < MIGRATE.sql
```
Com o MySQL instalado execute o comando
```
echo "<seu_usuario_mysql> <sua_senha_mysql>" > login.txt
```
Substituindo "<seu_usuario_mysql> <sua_senha_mysql>" com seus dados de acesso ao MySQL. Esse passo é opcional, se você tiver problemas ou preferir pode apenas fazer as devidas alterações colocando seus dados de acesso nos arquivos **"feeder.py"** e **"/app/models/__init\__.py"**, e comentando o código que abre o arquivo login.txt.

Com o MySQL configurado e o banco de dados criado você pode executar o programa **"feeder.py"** esse programa deve incluir algumas informações no banco de dados. (Isso pode levar alguns minutos)
```
python feeder.py
```
Depois disso você pode executar o **"run.py"**
```
python run.py runserver
```
Deve ser mostrado no terminal o link de acesso, basta copiar e colar no navegador
```
* Running on <http://<localhost>:4002>
```