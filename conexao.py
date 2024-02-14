# importando a biblioteca
import sqlite3

# apontando qual arquivo iremos utilizar
conexao = sqlite3.connect('banco')
# passando para uma nova variavel
cursor = conexao.cursor()

# execução dos comandos
#cursor.execute('CREATE TABLE usuario(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
# criamos tabela gerentes para utilizar os join's
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')


# para testar o comando DROP criaremos uma nova tabela para excluir depois
#cursor.execute('CREATE TABLE produtos (id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

# comando que podemos utilizar para modificar algo na nossa tabela (devera comentar o comando anterior)
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')

# para inserir mais uma coluna
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')

# caso tenhamos escrito algo errado
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

# para excluir uma tabela
#cursor.execute('DROP TABLE produtos')

# para inserir infos na tabela
#cursor.execute('INSERT INTO usuario (id,nome,endereco,email,telefone) VALUES(1,"Isadora","França","isa@gmail.com",21993564890)')
#cursor.execute('INSERT INTO usuario (id,nome,endereco,email,telefone) VALUES(2,"Maria","Salvador","isa@gmail.com",21993564890)')
#cursor.execute('INSERT INTO usuario (id,nome,endereco,email,telefone) VALUES(3,"José","Curitiba","isa@gmail.com",21993564890)')
#cursor.execute('INSERT INTO usuario (id,nome,endereco,email,telefone) VALUES(4,"Márcia","São Paulo","isa@gmail.com",21993564890)')
#cursor.execute('INSERT INTO gerentes (id,nome,endereco,email) VALUES(4,"Márcia","São Paulo","isa@gmail.com")')
#cursor.execute('INSERT INTO gerentes (id,nome,endereco,email) VALUES(1,"João","São Paulo","isa@gmail.com")')
#cursor.execute('INSERT INTO gerentes (id,nome,endereco,email) VALUES(8,"Cynthia","Inglaterra","cy@gmail.com")')

# para deletar alguma informação específica da tabela (nesses caso todo id que for igual a 1)
#cursor.execute('DELETE FROM usuario where id=1')

# para selecionar todos os dados da tabela
#dados = cursor.execute('SELECT * FROM usuario')
# para cada usuario em dados mostre quem é o usuario
#for usuario in dados:
#    print(usuario)

# para um dado específico
#dados = cursor.execute('SELECT nome FROM usuario')
# para cada usuario em dados mostre quem é o usuario
#for usuario in dados:
#    print(usuario)   

# para mais de um dado específico
#dados = cursor.execute('SELECT nome,telefone FROM usuario')
# para cada usuario em dados mostre quem é o usuario
#for usuario in dados:
#    print(usuario)   

# para um dado específico e alguma condição
#dados = cursor.execute('SELECT nome,telefone FROM usuario WHERE id>2')
# para cada usuario em dados mostre quem é o usuario
#for usuario in dados:
#    print(usuario)  
# para atualizar algum dado da tabela
#cursor.execute('UPDATE usuario SET endereco="MINAS GERAIS" WHERE nome="José"') 

# para ordenar os dados por nome de forma decrescente
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')
#for usuario in dados:
#    print(usuario)   

# para delimitar e distinguir
#dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 2') # limitou para apenas 2 informações
#for usuario in dados:
#    print(usuario)   

# GROUP BY (para agrupar os dados baseados em condições específicas, pode aplicar op mat e etc) 
#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome') 
#dados = cursor.execute('SELECT id,nome FROM usuario GROUP BY nome') 

# HAVING
#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3') 

# JOIN's (quando queremos retornar informações agrupadas de duas ou mais tabelas em condições específicas)
# criamos mais uma tabela lá em cima
# JOIN - INNER JOIN (vai retornar apenas as linhas em correspondencia para ambas as tabelas, onde os ids forem iguais nas tabelas ele vai juntar)
#dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id') 
#for usuario in dados:
#    print(usuario)  

# JOIN - LEFT JOIN (ele vai ler e preencher (com none) os dados vazios à esquerda e juntar todos os dados de acordo com a nossa especificação)
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.nome = gerentes.nome') 

# JOIN - RIGHT JOIN (contrario da LEFT)
#dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome') 

# JOIN - FULL JOIN (faz a comparação e retorna de todas as tabelas)
#dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome') 


# SUB-CONSULTAS (permite utilizar o resultado de uma consulta como parte da condição de criterio de uma outra consulta )
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)') # como se fosse uma consulta dentro de uma consulta
for usuario in dados:
    print(usuario)  


# para enviar os dados
conexao.commit()
# para fechar a conexão
conexao.close




