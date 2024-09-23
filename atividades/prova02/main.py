Para realizar as operações solicitadas usando o Play with Docker com MySQL e phpMyAdmin via Docker Compose, siga as etapas abaixo.

Passo 1: Criar o arquivo docker-compose.yml
Criar um novo diretório no Play with Docker para o seu projeto:
mkdir avaliacao_pratica_2
cd avaliacao_pratica_2

Criar o arquivo docker-compose.yml no diretório:
version: '3.1'

services:
  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: alunos_db
      MYSQL_USER: user
      MYSQL_PASSWORD: userpassword
    volumes:
      - db_data:/var/lib/mysql

  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    restart: always
    ports:
      - 8080:80
    environment:
      PMA_HOST: db
      PMA_USER: user
      PMA_PASSWORD: userpassword

volumes:
  db_data:

  -- PRA SAIR DO CODIGO NO PLAY WITH DOCKER É: Shift : wq!

Passo 2: Executar o Docker Compose
No terminal do Play with Docker, execute o seguinte comando para iniciar os containers:

docker-compose up -d
Verifique se os containers estão em execução:
docker-compose ps

Passo 3: Conectar ao phpMyAdmin
Acesse o phpMyAdmin em http://localhost:8080.
Use as credenciais:
Usuário: nagylafr
Senha: nagyla2006

(SQL)
Passo 4: Criar a Tabela e Inserir Dados
Criar a tabela TB_ALUNO com os seguintes campos:

CREATE TABLE TB_ALUNO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_nome VARCHAR(50),
    endereco VARCHAR(100),
    n1 FLOAT,
    n2 FLOAT,
    faltas INT,
    aprovado_sn VARCHAR(10)
);

Inserir dados de exemplo para evidenciar várias situações de aprovação/reprovação:
INSERT INTO TB_ALUNO (aluno_nome, endereco, n1, n2, faltas, aprovado_sn) VALUES
('João Silva', 'Rua A, 123', 7.0, 6.5, 10, 'VERDADEIRO'),
('Maria Oliveira', 'Rua B, 456', 5.0, 5.5, 21, 'FALSO'),
('Carlos Pereira', 'Rua C, 789', 4.0, 5.0, 5, 'FALSO'),
('Ana Costa', 'Rua D, 321', 8.5, 9.0, 0, 'VERDADEIRO');


Passo 5: Executar Scripts
Você pode executar scripts SQL diretamente pelo phpMyAdmin para manipular os dados conforme necessário.

Passo 6: Captura de Imagem da Saída do Script
Tire uma captura de tela da tela do phpMyAdmin mostrando os registros inseridos e seus status de aprovação.


SO COLOCAR AS IMAGENS NA PASTA DO GITHUB - PROVA PRATICA N2 







