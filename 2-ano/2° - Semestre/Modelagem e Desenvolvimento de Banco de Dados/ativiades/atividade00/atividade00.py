from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

file_path = "atividades_fundamentos_bancos_de_dados.pdf"

doc = SimpleDocTemplate(
    file_path, pagesize=A4,
    rightMargin=1.7*cm, leftMargin=1.7*cm,
    topMargin=1.5*cm, bottomMargin=1.5*cm
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleCenter", parent=styles["Title"],
                          alignment=TA_CENTER, fontSize=20, leading=24, spaceAfter=14))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"],
                          fontSize=14, leading=18, spaceBefore=10, spaceAfter=8))
styles.add(ParagraphStyle(name="BodyCustom", parent=styles["BodyText"],
                          fontSize=10.5, leading=15, spaceAfter=6))

story = [
    Paragraph("Atividades — Fundamentos de Bancos de Dados", styles["TitleCenter"]),
    Paragraph("Aula de exercícios — Curso Técnico em Informática", styles["BodyCustom"]),
    Spacer(1, 8)
]

activities = [
("1. Complete as definições",
"""1. Um Banco de Dados é uma coleção ________________________________.<br/>
2. Um SGBD é ________________________________________________.<br/>
3. O minimundo representa ______________________________________.<br/>
4. CRUD significa:<br/>
C = ____________________ &nbsp;&nbsp; R = ____________________<br/>
U = ____________________ &nbsp;&nbsp; D = ____________________"""),

("2. Relacione as colunas",
"""<b>A)</b> Banco de Dados<br/><b>B)</b> SGBD<br/><b>C)</b> Minimundo<br/>
<b>D)</b> CRUD<br/><b>E)</b> Dado<br/><br/>
( ) Software responsável por gerenciar os dados.<br/>
( ) Parte da realidade que será representada pelo sistema.<br/>
( ) Coleção organizada de dados relacionados.<br/>
( ) Conjunto de operações para criar, consultar, atualizar e excluir dados.<br/>
( ) Fato ou valor que pode ser armazenado."""),

("3. Verdadeiro ou falso",
"""1. ( ) Todo conjunto de dados é um Banco de Dados.<br/>
2. ( ) Um Banco de Dados deve possuir significado e um propósito.<br/>
3. ( ) O SGBD é responsável por gerenciar o Banco de Dados.<br/>
4. ( ) Banco de Dados e SGBD são exatamente a mesma coisa.<br/>
5. ( ) O minimundo representa uma parte da realidade.<br/>
6. ( ) CRUD representa operações realizadas sobre os dados.<br/>
7. ( ) Um Banco de Dados serve somente para armazenar dados."""),

("4. Banco de Dados ou SGBD?",
"""Classifique cada item como BD (Banco de Dados) ou SGBD (Sistema de Gerenciamento de Banco de Dados):<br/><br/>
1. PostgreSQL<br/>2. Dados dos alunos<br/>3. MySQL<br/>4. Cadastro de clientes<br/>
5. Oracle Database<br/>6. Dados dos produtos<br/>7. SQLite<br/>8. Notas dos alunos."""),

("5. Identifique o CRUD",
"""Indique se cada situação representa C, R, U ou D.<br/><br/>
1. Cadastrar um novo aluno.<br/>2. Consultar os dados de um aluno.<br/>
3. Alterar o endereço de um aluno.<br/>4. Excluir um aluno.<br/>
5. Cadastrar um novo professor.<br/>6. Consultar todos os cursos.<br/>
7. Alterar o nome de um aluno.<br/>8. Excluir uma disciplina."""),

("6. Dados ou informação?",
"""Considere:<br/><br/>
João &nbsp;&nbsp; 17 &nbsp;&nbsp; Informática &nbsp;&nbsp; 12345<br/><br/>
Agora:<br/><br/>
Nome: João<br/>Idade: 17<br/>Curso: Informática<br/>Matrícula: 12345<br/><br/>
a) Qual é a diferença entre os dois exemplos?<br/>
b) Por que o segundo exemplo possui mais significado?<br/>
c) O que foi acrescentado aos dados?"""),

("7. Identificando o minimundo",
"""Uma escola possui: Alunos, Professores, Cursos, Disciplinas, Biblioteca, Cantina,
Laboratórios, Salas, Funcionários e Ônibus.<br/><br/>
Um sistema será desenvolvido exclusivamente para controlar as matrículas dos alunos.<br/><br/>
a) Qual é o minimundo desse sistema?<br/>
b) A cantina faz parte do minimundo? Justifique.<br/>
c) A biblioteca necessariamente faz parte do minimundo? Justifique."""),

("8. Situação-problema — Loja",
"""Uma loja deseja criar um sistema para controlar seus produtos.<br/><br/>
Dados: Código, Nome, Preço, Marca, Quantidade em estoque e Categoria.<br/><br/>
a) Qual é o objetivo do Banco de Dados?<br/>
b) Cite três operações que poderão ser realizadas.<br/>
c) Dê um exemplo de Create.<br/>d) Dê um exemplo de Read.<br/>
e) Dê um exemplo de Update.<br/>f) Dê um exemplo de Delete."""),

("9. Encontre o erro",
"""Leia a afirmação:<br/><br/>
“O PostgreSQL é o banco de dados onde estão armazenados os alunos.
O SGBD é formado pelos dados dos alunos.”<br/><br/>
a) Qual é o erro na afirmação?<br/>
b) Reescreva a afirmação corretamente."""),

("10. Situação-problema — Sistema acadêmico",
"""Uma instituição possui um sistema acadêmico que trabalha com:
Alunos, Professores, Cursos, Disciplinas, Matrículas e Notas.<br/><br/>
a) Qual é o minimundo?<br/>
b) Cite quatro dados que poderiam ser armazenados sobre um aluno.<br/>
c) Cite uma operação de Create.<br/>d) Cite uma operação de Read.<br/>
e) Cite uma operação de Update.<br/>f) Cite uma operação de Delete.<br/>
g) Qual é a função do SGBD nesse sistema?"""),

("11. Complete o esquema",
"""MUNDO REAL<br/>↓<br/>____________________<br/>↓<br/>BANCO DE DADOS<br/>↕<br/>
____________________<br/>↓<br/>APLICAÇÃO<br/>↓<br/>USUÁRIO<br/><br/>
Depois, explique com suas palavras o que representa cada elemento."""),

("12. Questão final",
"""Explique por que um Banco de Dados não é simplesmente um conjunto de dados armazenados.<br/><br/>
Em sua resposta, utilize pelo menos três dos seguintes conceitos:<br/>
• organização &nbsp; • significado &nbsp; • propósito &nbsp; • minimundo &nbsp; • SGBD &nbsp; • CRUD""")
]

for title, body in activities:
    story.append(Paragraph(title, styles["Section"]))
    story.append(Paragraph(body, styles["BodyCustom"]))

story.append(PageBreak())
story.append(Paragraph("Gabarito / orientação para correção", styles["TitleCenter"]))

answers = [
("1", "BD: coleção organizada de dados relacionados, com significado e propósito. SGBD: software/conjunto de programas que gerencia o BD. Minimundo: parte da realidade representada pelo sistema. CRUD: Create, Read, Update, Delete."),
("2", "B, C, A, D, E."),
("3", "F, V, V, F, V, V, F."),
("4", "1 SGBD; 2 BD; 3 SGBD; 4 BD; 5 SGBD; 6 BD; 7 SGBD; 8 BD."),
("5", "1 C; 2 R; 3 U; 4 D; 5 C; 6 R; 7 U; 8 D."),
("6", "O segundo exemplo acrescenta contexto e identificação aos valores, tornando seu significado explícito."),
("7", "Minimundo: elementos relacionados ao controle de matrículas, como alunos, cursos, disciplinas e matrículas. Cantina e biblioteca não precisam fazer parte se não forem relevantes ao propósito do sistema."),
("8", "O BD organiza e armazena os dados dos produtos para permitir consulta e manipulação. Exemplos: cadastrar, consultar, alterar e excluir produtos."),
("9", "PostgreSQL é um SGBD, não o conjunto dos dados. O SGBD gerencia o Banco de Dados, que contém os dados."),
("10", "Minimundo: elementos necessários ao sistema acadêmico. As demais respostas devem ser coerentes com o cenário."),
("11", "MINIMUNDO e SGBD."),
("12", "Resposta discursiva. Deve relacionar organização, significado, propósito e/ou os demais conceitos de forma coerente.")
]

for num, ans in answers:
    story.append(Paragraph(f"<b>{num}.</b> {ans}", styles["BodyCustom"]))

doc.build(story)

print(file_path)
