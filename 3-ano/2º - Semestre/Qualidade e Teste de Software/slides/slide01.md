# Slide 1 — Aspectos de Testes em Aplicações Web e Móveis

**Testar uma aplicação significa verificar se ela funciona corretamente em diferentes condições de uso.**

Aplicações Web e móveis possuem características próprias e, por isso, exigem estratégias de teste diferentes.

Os principais aspectos são:

* Compatibilidade
* Desempenho
* Usabilidade
* Conectividade
* Estabilidade
* Diversidade de dispositivos e ambientes

---

# Slide 2 — Por que testar aplicações?

Os testes de software são fundamentais para garantir a **qualidade, confiabilidade e segurança** de uma aplicação.

Um sistema pode funcionar corretamente em uma situação e apresentar falhas em outra.

Por exemplo:

* Um site pode funcionar no Chrome e apresentar problemas no Safari.
* Um aplicativo pode funcionar em um smartphone novo e travar em um aparelho mais antigo.
* Uma aplicação pode apresentar problemas quando a conexão é interrompida.

**Testar significa buscar essas situações antes que elas afetem o usuário.**

---

# Slide 3 — Testes em Aplicações Web

**Aplicações Web** são sistemas acessados principalmente por meio de navegadores.

Exemplos:

* Sites
* Sistemas acadêmicos
* Lojas virtuais
* Redes sociais
* Sistemas empresariais

Os testes devem considerar que o usuário pode acessar a aplicação utilizando diferentes:

* Navegadores
* Sistemas operacionais
* Dispositivos
* Tamanhos de tela
* Velocidades de conexão

---

# Slide 4 — O que deve ser observado em uma aplicação Web?

Ao testar uma aplicação Web, é importante verificar:

**Compatibilidade:** a aplicação funciona corretamente em diferentes navegadores e sistemas?

**Responsividade:** a interface se adapta aos diferentes tamanhos de tela?

**Desempenho:** a aplicação carrega e responde em tempo adequado?

**Usabilidade:** o usuário consegue utilizar o sistema com facilidade?

**Conectividade:** o sistema reage corretamente a diferentes condições de rede?

---

# Slide 5 — Compatibilidade entre Navegadores

**Compatibilidade** é a capacidade de uma aplicação funcionar corretamente em diferentes ambientes.

Um mesmo site pode apresentar diferenças dependendo do navegador utilizado.

Os testes podem verificar:

* Aparência da página;
* Posicionamento dos elementos;
* Funcionamento de menus e botões;
* Formulários;
* Imagens e vídeos;
* Scripts e funcionalidades.

**O objetivo é garantir uma experiência consistente para diferentes usuários.**

---

# Slide 6 — Responsividade

**Responsividade** é a capacidade de uma aplicação adaptar sua interface ao tamanho e às características da tela utilizada.

Uma aplicação pode ser acessada em:

* Computadores;
* Tablets;
* Smartphones.

Durante os testes, deve-se verificar se:

* O conteúdo permanece visível;
* Os textos continuam legíveis;
* Os botões são acessíveis;
* Os menus funcionam;
* Não existem elementos sobrepostos;
* A navegação continua adequada.

---

# Slide 7 — Desempenho em Aplicações Web

**Desempenho** está relacionado à velocidade e à capacidade de resposta da aplicação.

Uma aplicação pode estar funcionalmente correta, mas ainda apresentar uma experiência ruim se for muito lenta.

É importante observar:

* Tempo de carregamento;
* Tempo de resposta;
* Consumo de recursos;
* Quantidade de dados transferidos;
* Comportamento com muitos acessos;
* Funcionamento em conexões lentas.

---

# Slide 8 — Testes de Conectividade

A qualidade da conexão pode alterar o comportamento de uma aplicação.

Por isso, os testes devem considerar situações como:

* Conexão rápida;
* Conexão lenta;
* Alta latência;
* Instabilidade;
* Perda de conexão;
* Recuperação da conexão.

**Uma aplicação bem projetada deve apresentar um comportamento adequado mesmo quando a rede apresenta problemas.**

---

# Slide 9 — Usabilidade

**Usabilidade** é a facilidade com que uma pessoa consegue aprender, compreender e utilizar uma aplicação para realizar suas tarefas.

Uma aplicação com boa usabilidade apresenta:

* Navegação intuitiva;
* Informações claras;
* Interface organizada;
* Botões e menus compreensíveis;
* Mensagens de erro úteis;
* Poucos obstáculos para realizar uma tarefa.

**Uma aplicação pode funcionar tecnicamente e ainda possuir problemas de usabilidade.**

---

# Slide 10 — Aplicações Web × Aplicações Móveis

Apesar de possuírem características em comum, as duas plataformas apresentam desafios diferentes.

### Web

O foco está principalmente em:

* Navegadores;
* Responsividade;
* Compatibilidade;
* Desempenho;
* Diferentes condições de rede.

### Móvel

Além desses aspectos, é necessário considerar:

* Fragmentação de dispositivos;
* Sistemas operacionais;
* Toque e gestos;
* Sensores;
* Bateria;
* Recursos do aparelho.

---

# Slide 11 — Testes em Aplicações Móveis

Aplicações móveis são executadas em dispositivos que apresentam diferentes características de hardware e software.

É necessário considerar:

* Modelo do aparelho;
* Fabricante;
* Sistema operacional;
* Versão do sistema;
* Tamanho da tela;
* Resolução;
* Memória;
* Processador;
* Bateria;
* Conexão.

Essa variedade torna os testes móveis especialmente desafiadores.

---

# Slide 12 — Fragmentação de Dispositivos

**Fragmentação** é a existência de uma grande variedade de dispositivos, configurações e versões de sistemas capazes de executar uma mesma aplicação.

Dois smartphones podem possuir:

* Diferentes tamanhos de tela;
* Diferentes resoluções;
* Diferentes quantidades de memória;
* Diferentes processadores;
* Diferentes versões do sistema operacional.

Por isso, uma aplicação pode funcionar corretamente em um aparelho e apresentar problemas em outro.

---

# Slide 13 — Sistemas Operacionais

As diferentes versões dos sistemas operacionais também precisam ser consideradas nos testes.

Uma atualização pode modificar o funcionamento de:

* Permissões;
* Notificações;
* Armazenamento;
* Câmera;
* Localização;
* Aplicações em segundo plano;
* Recursos de segurança.

**O teste deve considerar as versões do sistema operacional utilizadas pelo público da aplicação.**

---

# Slide 14 — Interação por Toque

A interação em dispositivos móveis acontece principalmente por meio de **toques e gestos**.

Entre as interações mais comuns estão:

* Toque;
* Toque prolongado;
* Deslizar;
* Arrastar;
* Pinça para ampliar ou reduzir;
* Rotação da tela.

Os elementos da interface precisam possuir tamanho e espaçamento adequados para facilitar a interação.

---

# Slide 15 — Sensores e Recursos do Dispositivo

Aplicações móveis podem utilizar recursos específicos do aparelho.

Exemplos:

* Câmera;
* Microfone;
* GPS;
* Bluetooth;
* Biometria;
* Acelerômetro;
* Giroscópio;
* Notificações.

Esses recursos também precisam ser testados, incluindo situações em que o usuário **nega uma permissão ou desativa determinado recurso**.

---

# Slide 16 — Conectividade em Aplicações Móveis

O usuário pode utilizar o aplicativo em diferentes condições de conexão.

Durante o uso pode ocorrer:

**Wi-Fi → perda de sinal → rede móvel → recuperação da conexão**

Os testes devem verificar:

* O que acontece quando a conexão é perdida;
* Se os dados são preservados;
* Se o usuário recebe uma mensagem adequada;
* Se a operação pode ser retomada;
* Se o aplicativo volta ao funcionamento normal após a recuperação da conexão.

---

# Slide 17 — Desempenho e Bateria

Em dispositivos móveis, o desempenho está diretamente relacionado ao consumo de recursos.

Uma aplicação pode consumir:

* Processador;
* Memória;
* Armazenamento;
* Dados móveis;
* GPS;
* Câmera;
* Bateria.

**Uma aplicação eficiente deve apresentar bom desempenho sem utilizar recursos de maneira excessiva.**

---

# Slide 18 — Usabilidade em Aplicações Móveis

A usabilidade móvel precisa considerar o contexto real em que o usuário utiliza o dispositivo.

O usuário pode estar:

* Caminhando;
* Em movimento;
* Utilizando apenas uma mão;
* Em um ambiente muito iluminado;
* Com pouco tempo;
* Com conexão instável.

Por isso, a interface deve ser **simples, clara, acessível e adequada ao toque**.

---

# Slide 19 — O que muda entre Web e Mobile?

| Aplicações Web          | Aplicações Móveis             |
| ----------------------- | ----------------------------- |
| Diferentes navegadores  | Diferentes dispositivos       |
| Diferentes sistemas     | Diferentes versões do sistema |
| Responsividade          | Fragmentação                  |
| Compatibilidade         | Toque e gestos                |
| Condições de rede       | Sensores                      |
| Desempenho no navegador | Bateria e recursos            |

**A estratégia de testes deve considerar as características específicas de cada plataforma.**

---

# Slide 20 — Mentalidade do Testador

O testador não deve pensar apenas:

> “A funcionalidade funciona?”

Também deve pensar:

> “O que acontece se o ambiente mudar?”

Algumas situações importantes:

* Outro navegador;
* Outra resolução;
* Outro dispositivo;
* Sistema operacional diferente;
* Pouca memória;
* Conexão lenta;
* Perda de conexão;
* Permissão negada;
* Mudança de orientação da tela.

**Testar é explorar diferentes condições para descobrir comportamentos inesperados.**

---

# Slide 21 — Qualidade da Aplicação

Os testes ajudam a garantir diferentes características de qualidade:

**Confiabilidade**
A aplicação apresenta o comportamento esperado?

**Compatibilidade**
Funciona nos ambientes previstos?

**Usabilidade**
É fácil de utilizar?

**Desempenho**
Responde adequadamente?

**Estabilidade**
Evita travamentos e falhas?

**Resiliência**
Consegue lidar com situações adversas?

---

# Slide 22 — Conceito Final

**Testar aplicações Web e móveis é verificar o comportamento do software em diferentes ambientes, dispositivos e condições de uso.**

O objetivo não é apenas descobrir se uma funcionalidade funciona.

É garantir que a aplicação continue:

* **Funcional**
* **Compatível**
* **Estável**
* **Usável**
* **Performática**
* **Confiável**

mesmo diante da diversidade encontrada no ambiente real.
