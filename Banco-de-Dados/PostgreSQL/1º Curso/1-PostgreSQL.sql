/*
#Inserindo na tabela as colunas com seus valores
*/
INSERT INTO aluno(
	nome,
	cpf,
	observacao,
	idade,
	dinheiro,
	altura,
	ativo,
	data_nascimento,
	hora_aula,
	matriculado_em) 
VALUES (
	'Diogo',
	'12345678901',
	'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras finibus mollis justo in congue. Curabitur eget malesuada lorem, posuere varius ante. Mauris in est orci. Sed semper pretium velit vitae egestas. Donec finibus semper eleifend. Ut id velit ultricies, pellentesque purus nec, maximus risus. Nulla tristique tellus nec quam condimentum, sit amet convallis erat fermentum. Mauris in dictum dui. In et ante quam. Suspendisse tempor leo nec elementum mattis. Vestibulum rutrum quam risus, eu aliquam sem rhoncus eu.Vestibulum facilisis nunc at viverra luctus. Vestibulum quis tortor lacus. Sed at euismod mauris. Praesent sed neque risus. Donec sed cursus ligula. Nam cursus porttitor purus auctor consequat. In vitae turpis aliquet, euismod quam eu, finibus lacus. Curabitur volutpat tellus et pretium volutpat.',
	35,
	100.50,
	1.81,
	TRUE,
	'1984-08-27',
	'17:30:00',
	'2020-02-08 12:32:45'
);

 SELECT * FROM aluno;
 
 
 SELECT * 
   FROM aluno
  WHERE ID = 14;

 UPDATE aluno
 	SET nome = 'Nico',
	cpf = '10987654321',
	observacao ='Teste',
	idade = 38,
	dinheiro = 15.32,
	altura = 1.90,
	ativo = FALSE,
	data_nascimento = '1980-01-15',
	hora_aula = '13:00:00',
	matriculado_em = '2020-01-02 15:00:00'
  	WHERE id = 1;
  
  
 SELECT *  FROM aluno ;
 
 SELECT * 
   FROM aluno
  WHERE nome = 'Diogo';

DELETE 
   FROM aluno
  WHERE ID = 26;
 
/* 
#Pegar na tabela aluno o nome,idade e matriculado_em
#E modificar o nome que vai aparecer 
*/
SELECT nome AS "Nome do Aluno",
 		idade,
		matriculado_em AS quando_se_matriculou
		FROM aluno;

INSERT INTO aluno (nome) VALUES ('Vinicius Dias');
INSERT INTO aluno (nome) VALUES ('Nico');
INSERT INTO aluno (nome) VALUES ('Diogo');
INSERT INTO aluno (nome) VALUES ('Diego');


/*
#Selecionar na tabela aluno qualquer nome que possua espaço
*/
SELECT * 
	FROM aluno
	WHERE nome LIKE '% %'
	

/*
#Selecionar na tabela aluno qualquer idade
#Que não seja 19 e nulo
*/
SELECT * 
	FROM aluno	
	WHERE idade != 19;

SELECT * 
	FROM aluno	
	WHERE idade < 19;

#Idade entre 19 e 35
SELECT * 
	FROM aluno	
	WHERE idade BETWEEN 19 AND 35;

SELECT *
	FROM aluno
	WHERE nome LIKE 'Diogo'
	OR nome LIKE 'J%';
	
/*	
#Chave Primária, basicmaente o PRIMARY KEY faz 
#com que o id tenha que ser único, não pode ser
#repetido e nem nulo
*/

/*Exemplo de criação de tabela sem usar a PRIMARY KEY, utilizando o NOT NULL E UNIQUE, para
não aceitar nulo e nem repetido*/

CREATE TABLE exemplo(
	id INTEGER NOT NULL UNIQUE,
	nome VARCHAR (255) NOT NULL
);


/*UTILIZANDO A PRIMARY KEY, basicamente a PRIMARY KEY possui o NOT NULL e o UNIQUE*/

DROP TABLE curso;
CREATE TABLE curso(
	id INTEGER PRIMARY KEY,
	nome VARCHAR(255) NOT NULL
);
	
INSERT INTO curso (id,nome) VALUES (NULL,NULL);
INSERT INTO curso (id,nome) VALUES (1,NULL);
INSERT INTO curso (id,nome) VALUES (NULL,'PYTHON');

INSERT INTO curso (id,nome) VALUES (1,'PYTHON');

INSERT INTO curso (id,nome) VALUES (2,'DJANGO');
SELECT *
	FROM curso
	

/*
Chave Estrangeira
*/	

DROP TABLE aluno;
	
CREATE TABLE aluno(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL
);

INSERT INTO aluno (nome) VALUES ('Diogo');
INSERT INTO aluno (nome) VALUES ('Vinicius');
	
SELECT *
	FROM aluno;

DROP TABLE aluno_curso;

CREATE TABLE aluno_curso(
	aluno_id INTEGER,
	curso_id INTEGER,
	PRIMARY KEY (aluno_id, curso_id),
	
	/*A Chave estrangeira obrigada que tanto o id 
	do aluno quanto do curso existam*/
 	FOREIGN KEY (aluno_id) REFERENCES aluno (id),
	FOREIGN KEY (curso_id) REFERENCES curso (id)
);

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (1,1);

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (2,1);

/*Irá dar erro, pois tanto o aluno com id 3, quanto o curso
com id 3 não existe */

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (3,1);

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (1,3);

SELECT * FROM aluno WHERE id = 1;

SELECT * FROM curso WHERE id = 1;


SELECT * FROM aluno WHERE id = 2;

SELECT * FROM curso WHERE id = 1;

SELECT * FROM aluno WHERE id = 3;

SELECT * FROM curso WHERE id = 1;

SELECT * FROM aluno;
SELECT * FROM curso;
SELECT * FROM aluno_curso;

/*
CONSULTAS COM RELACIONAMENTOS
*/

SELECT aluno.nome as aluno_nome,
	   curso.nome as curso
	FROM aluno
	JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id
	JOIN curso ON curso.id 					 = aluno_curso.curso_id

INSERT INTO aluno_curso (aluno_id,curso_id) VALUES (2,2);

/*
LEFT,RIGHT,CROSS E FULL JOINS
*/

INSERT INTO aluno (nome) VALUES ('Nico');

INSERT INTO curso (id,nome) VALUES (3,'JAVA');


/* LEFT JOIN, eu posso ter os dados da tabela esquerda, mas
não da direita, no caso deste exemplo ele mostrará o Nico, mas 
na tabela de Curso estará nulo. No exemplo a eseguir vemos que o LEFT JOIN ele dá
prioridade para o aluno
*/

SELECT aluno.nome as aluno_nome,
	   curso.nome as curso
	FROM aluno
	LEFT JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id
	LEFT JOIN curso ON curso.id 					 = aluno_curso.curso_id


/* RIGHT JOIN, é o contrário do LEFT JOIN, ele precisa ter os dados da direita, e não tem
problema não ter os dados da esquerda, no exemplo a seguir irá mostrar o Curso JAVA, mas 
na tabela do nome vai ficar o NULL. No exemplo a seguir vemos que o RIGHT JOIN ele dá
prioridade para o curso
*/

SELECT aluno.nome as aluno_nome,
	   curso.nome as curso
	FROM aluno
	RIGHT JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id
	RIGHT JOIN curso ON curso.id 					 = aluno_curso.curso_id
	
/*FULL JOIN, para o full join não importa se um dos dois lados está ou não com 
dados preenchidos, no exemplo podemos ver que ele mostra 2 linhas, tanto a com nome nulo
e curso JAVA, quanto a com nome NICO e curso nulo. No Exemplo a seguir vemos que o FULL
JOIN não importa, ele vai ignorar ambos os dois
*/

SELECT aluno.nome as aluno_nome,
	   curso.nome as curso
	FROM aluno
	FULL JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id
	FULL JOIN curso ON curso.id 					 = aluno_curso.curso_id
	
	
/*CROSS JOIN, já multipla cada linha de uma tabela com a outra, como podemos ver no exemplo
as 3 pessoas da tabela aluno, vai aparecer com os 3 cursos da tabela curso. Interessante
que mesmo que o aluno 'João' não esteja matriculado na tabela aluno_curso ele vai aparecer
com os 3 cursos. No exemplo a seguir vemos que no CROSS JOIN ele vai multiplicar a linha de
uma tabela pelas linhas da outra tabela
*/

SELECT aluno.nome as aluno_nome,
	   curso.nome as curso
	FROM aluno
	CROSS JOIN curso

INSERT INTO aluno (nome) VALUES ('João');



/*DELETE CASCADE*/

SELECT * FROM aluno;
SELECT * FROM curso;
SELECT * FROM aluno_curso;

/* Caso eu utilize a seguinte linha de código:
DELETE FROM aluno WHERE id = 1;
O Programa da erro pois o aluno de id tb está na tabela curso, para isso adicionamos
o ON DELETE CASCADE na criação da tabela */

DROP TABLE aluno_curso;

CREATE TABLE aluno_curso(
	aluno_id INTEGER,
	curso_id INTEGER,
	PRIMARY KEY (aluno_id, curso_id),
	/*Depois de adicionar o ON DELETE CASCADE fica possível excluir uma linha da tabela
	aluno que automaticamente esse aluno será excluido de todas as outras tabelas que
	ele fizer parte*/
 	FOREIGN KEY (aluno_id) REFERENCES aluno (id)
	ON DELETE CASCADE,
	FOREIGN KEY (curso_id) REFERENCES curso (id)
	
);

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (1,1);

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (2,1);

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (3,1);

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (1,3);

SELECT *
	FROM aluno_curso;
	
SELECT aluno.nome as aluno_nome,
	   curso.nome as curso
	FROM aluno
	JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id
	JOIN curso ON curso.id 					 = aluno_curso.curso_id
	
DELETE FROM aluno WHERE id = 1;


/*UPDATE CASCADE*/

/*VAMOS TROCAR O ID DO VINICIUS DE 2 PARA 10, para isso devemos adicionar o ON UPDATE
CASCADE NA CRIAÇÃO DA TABELA
*/
DROP TABLE aluno_curso;
CREATE TABLE aluno_curso(
	aluno_id INTEGER,
	curso_id INTEGER,
	PRIMARY KEY (aluno_id, curso_id),
 	FOREIGN KEY (aluno_id) REFERENCES aluno (id)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
	FOREIGN KEY (curso_id) REFERENCES curso (id)
);
INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (1,1);

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (2,1);

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (3,1);

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (1,3);

SELECT * FROM aluno;
SELECT * FROM curso;
SELECT * FROM aluno_curso;

SELECT aluno.id AS aluno_id,
	   aluno.nome AS "NOME do ALUNO",
	   curso.id AS curso_id,
	   curso.nome AS "NOME do CURSO"
	   FROM aluno
	   JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id
	   JOIN curso       ON curso.id             = aluno_curso.curso_id
	   
UPDATE aluno SET id = 10 WHERE id = 2;





/*
Avançando nas Consultas
*/

/*Ordenando as Consultas*/

DROP TABLE funcionarios;
CREATE TABLE funcionarios(
	id SERIAL PRIMARY KEY,
	matricula VARCHAR(10),
	nome VARCHAR(255),
	sobrenome VARCHAR(255)
);

INSERT INTO funcionarios (matricula,nome,sobrenome) VALUES ('M001','Diogo','Mascarenhas');
INSERT INTO funcionarios (matricula,nome,sobrenome) VALUES ('M002','Vinicius','Dias');
INSERT INTO funcionarios (matricula,nome,sobrenome) VALUES ('M003','Nico','Steppat');
INSERT INTO funcionarios (matricula,nome,sobrenome) VALUES ('M004','João','Roberto');
INSERT INTO funcionarios (matricula,nome,sobrenome) VALUES ('M005','Diogo','Mascarenhas');
INSERT INTO funcionarios (matricula,nome,sobrenome) VALUES ('M006','Alberto','Martins');
INSERT INTO funcionarios (matricula,nome,sobrenome) VALUES ('M007','Diogo','Oliveira');

/*O ORDER BY, ordena do menor para o maior
O DESC ordena do maior para o menor, enquanto o ASC do menor para o maior*/

SELECT * FROM funcionarios
	ORDER BY nome DESC

/*Ordernar pro mais de um paramêtro*/

SELECT * FROM funcionarios
	ORDER BY nome, matricula
	
/* Ordernar pelo valor da coluna, exemplo ordenando pelo sobrenome
que está na coluna 4 da tabela*/

SELECT * FROM funcionarios
	ORDER BY 4


/*Limitando as consultas*/
/*O LIMIT, limita a quantidade de linhas que irá mostrar na tabela*/
/*O Offset anda a quantidade de registros para 'frente'*/

SELECT * FROM funcionarios 
	ORDER BY id
	LIMIT 5
	/*Exemplo de uso do OFFSET, ele vai pegar na tabela depois do 
	valor informador, no exemplo abaixo irá iniciar a partir do 2*/
	OFFSET ;


/*Funções de agregação, são funções que podemos agrupar registros 
em um único resultado*/

/*Funções mais utilizandas
--COUNT - Retorna a quantidade de registros
--SUM - Retorna a soma dos registros
--MAX - Retorna o maior valor dos registros
--MIN - Retorna o menor valor dos registros
--AVG - Retorna a média dos registros
*/

SELECT COUNT(id),
	SUM (id),
	MAX (id),
	MIN (id),
	/*Round arredonda valores*/
	ROUND(AVG (id),0)
	FROM funcionarios;

/*Agrupando consultas
Para podermos tirar nome repetido temos duas formas,
a clausula DISTINCT, Caso seja necessário utilizar alguma função de
agregação ai devemos utilizar o GROUP BY*/

SELECT DISTINCT nome, SOBRENOME,
	COUNT(id)
	FROM funcionarios
	GROUP BY nome, sobrenome
	ORDER BY nome;

SELECT curso.nome,
	COUNT(aluno.id)
	FROM aluno
	JOIN aluno_curso ON aluno.id = aluno_curso.aluno_id
	JOIN curso ON curso.id = aluno_curso.curso_id
	GROUP BY 1
	ORDER BY 1


/*Filtando consultas agrupadas*/

SELECT * FROM aluno;
SELECT * FROM aluno_curso;
SELECT * FROM curso;

/*Saber se um curso não possui ninguem matriculado*/

SELECT curso.nome,
	COUNT (aluno.id)
	FROM curso
	LEFT JOIN aluno_curso ON aluno_curso.curso_id = curso.id
	LEFT JOIN aluno ON aluno.id = aluno_curso.aluno_id
	--WHERE COUNT(aluno.id) = 0
	GROUP BY 1
	--O HAVING é quase igual o Where, mas ele funciona para consultas
	--agrupadas
	HAVING COUNT (aluno.id) > 1;


SELECT nome,
	   COUNT(ID)
	FROM funcionarios
	GROUP BY nome
	HAVING COUNT(id) = 1;