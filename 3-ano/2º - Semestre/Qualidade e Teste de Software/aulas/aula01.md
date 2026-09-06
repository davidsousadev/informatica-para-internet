# Aspectos de Testes em Aplicações Web e Móveis

## Aula 1 — Testes em Aplicações Web

### 1. O que são testes em aplicações Web?

Aplicações Web são acessadas por meio de navegadores e podem ser utilizadas em diferentes sistemas operacionais, resoluções de tela, dispositivos e condições de rede.

Testar uma aplicação Web significa verificar se ela funciona corretamente em diferentes situações de uso, considerando não apenas suas funcionalidades, mas também aspectos como:

* Compatibilidade entre navegadores;
* Responsividade;
* Desempenho;
* Usabilidade;
* Acessibilidade;
* Segurança;
* Comportamento em diferentes condições de rede;
* Estabilidade.

Um sistema pode funcionar perfeitamente em um navegador e apresentar problemas em outro. Da mesma forma, uma página pode funcionar corretamente em um computador, mas apresentar problemas em uma tela menor.

### 2. Compatibilidade entre navegadores

Os usuários podem acessar uma aplicação utilizando diferentes navegadores, como Chrome, Firefox, Edge e Safari.

Cada navegador possui características próprias de interpretação e execução de tecnologias Web. Por isso, é importante verificar se a aplicação apresenta o mesmo comportamento nos principais ambientes utilizados pelo público.

Durante os testes, podem ser observadas diferenças em:

* Formatação e posicionamento dos elementos;
* Funcionamento de botões e menus;
* Execução de JavaScript;
* Carregamento de imagens e fontes;
* Formulários;
* Vídeos e outros conteúdos;
* Recursos de armazenamento local;
* Comportamento de elementos responsivos.

O objetivo não é apenas verificar se a página abre, mas se suas funcionalidades continuam corretas e sua apresentação permanece adequada.

### 3. Responsividade

Uma aplicação Web pode ser acessada por computadores, tablets e smartphones.

O conceito de responsividade está relacionado à capacidade da interface de se adaptar a diferentes tamanhos e orientações de tela.

Em um teste de responsividade, é importante observar:

* Tamanho e posicionamento dos elementos;
* Legibilidade dos textos;
* Organização dos menus;
* Tamanho dos botões;
* Imagens e vídeos;
* Rolagem da página;
* Formulários;
* Orientação vertical e horizontal.

Uma interface responsiva deve continuar utilizável mesmo quando o espaço disponível para apresentação do conteúdo muda.

### 4. Desempenho em aplicações Web

O desempenho influencia diretamente a experiência do usuário.

Uma aplicação pode apresentar problemas mesmo que todas as suas funcionalidades estejam corretas. Páginas que demoram muito para carregar ou apresentam lentidão podem levar o usuário a abandonar o sistema.

Entre os aspectos observados nos testes de desempenho estão:

* Tempo de carregamento;
* Velocidade de resposta;
* Quantidade de dados transferidos;
* Consumo de recursos;
* Comportamento com muitos usuários;
* Comportamento em conexões lentas ou instáveis.

Também é importante considerar que nem todos os usuários possuem computadores modernos ou conexões rápidas.

### 5. Testes em diferentes condições de rede

Uma aplicação Web deve ser avaliada considerando diferentes condições de conexão.

O comportamento pode variar entre:

* Conexão rápida e estável;
* Conexão lenta;
* Alta latência;
* Oscilações de conexão;
* Perda temporária de conexão;
* Recuperação da conexão.

O sistema deve apresentar um comportamento previsível quando a conexão é interrompida ou apresenta problemas.

### 6. Usabilidade em aplicações Web

Usabilidade representa a facilidade com que o usuário consegue compreender e utilizar uma aplicação.

Durante os testes, devem ser observados aspectos como:

* Clareza das informações;
* Facilidade de navegação;
* Organização dos elementos;
* Consistência dos menus e botões;
* Facilidade para realizar tarefas;
* Mensagens apresentadas ao usuário;
* Prevenção e tratamento de erros.

Uma aplicação pode estar tecnicamente correta e, ainda assim, apresentar problemas de usabilidade.

### 7. A importância da diversidade de ambientes

No ambiente Web, existe uma grande variedade de combinações entre:

**Dispositivo + Sistema operacional + Navegador + Resolução + Rede**

Essa diversidade faz com que os testes não possam considerar apenas um único ambiente.

Quanto maior a diversidade de usuários esperada, maior a necessidade de definir quais ambientes devem ser priorizados nos testes.

---

# Aula 2 — Testes em Aplicações Móveis

### 1. Características das aplicações móveis

Aplicações móveis apresentam desafios diferentes das aplicações Web porque são executadas em dispositivos com características variadas.

Existem diferenças entre smartphones e tablets relacionadas a:

* Tamanho da tela;
* Resolução;
* Memória;
* Processador;
* Sistema operacional;
* Versão do sistema;
* Capacidade de armazenamento;
* Bateria;
* Sensibilidade ao toque;
* Sensores;
* Qualidade da conexão.

Essa diversidade é conhecida como **fragmentação de dispositivos**.

### 2. Fragmentação de dispositivos

Uma aplicação móvel pode funcionar corretamente em determinado aparelho e apresentar problemas em outro.

Isso pode acontecer devido às diferenças entre:

* Modelos de dispositivos;
* Fabricantes;
* Tamanhos de tela;
* Resoluções;
* Versões do sistema operacional;
* Capacidade de processamento;
* Quantidade de memória;
* Configurações do dispositivo.

Por esse motivo, os testes precisam considerar uma seleção representativa dos dispositivos utilizados pelo público-alvo.

### 3. Sistemas operacionais e versões

Aplicações móveis podem ser executadas em diferentes versões de sistemas operacionais.

Uma atualização do sistema pode alterar comportamentos relacionados a:

* Permissões;
* Notificações;
* Armazenamento;
* Câmera;
* Localização;
* Funcionamento em segundo plano;
* Interface;
* Segurança.

Por isso, é importante verificar a compatibilidade da aplicação com as versões de sistema operacional que fazem parte do público-alvo.

### 4. Interfaces baseadas em toque

Diferentemente do computador, o dispositivo móvel utiliza principalmente interações por toque.

Os testes devem considerar ações como:

* Toque;
* Toque prolongado;
* Deslize;
* Arraste;
* Pinça para ampliar ou reduzir;
* Rotação da tela.

Os elementos da interface precisam apresentar tamanho e espaçamento adequados para permitir uma interação confortável.

Também devem ser avaliados possíveis problemas de resposta ao toque, sobreposição de elementos e dificuldade para selecionar componentes pequenos.

### 5. Orientação e tamanho da tela

Dispositivos móveis podem ser utilizados na orientação vertical ou horizontal.

A mudança de orientação pode alterar a disposição dos elementos da interface.

É necessário verificar se:

* O conteúdo permanece visível;
* Os elementos continuam acessíveis;
* Os textos não ficam cortados;
* Os componentes não se sobrepõem;
* A navegação continua funcionando;
* O estado da aplicação é preservado quando necessário.

### 6. Sensores e recursos do dispositivo

Aplicações móveis podem utilizar recursos específicos do aparelho, como:

* Câmera;
* Microfone;
* GPS;
* Acelerômetro;
* Giroscópio;
* Bluetooth;
* Biometria;
* Notificações.

Quando esses recursos fazem parte da aplicação, eles também precisam ser testados.

É importante verificar tanto o funcionamento normal quanto situações em que o usuário nega uma permissão, desativa determinado recurso ou utiliza o aplicativo em condições diferentes das esperadas.

### 7. Conectividade em aplicações móveis

O usuário de um aplicativo móvel pode mudar constantemente de ambiente.

Durante o uso, pode ocorrer:

* Perda de Wi-Fi;
* Troca entre Wi-Fi e rede móvel;
* Sinal fraco;
* Ausência temporária de Internet;
* Recuperação da conexão.

O aplicativo deve tratar essas situações adequadamente, evitando perda desnecessária de dados ou comportamentos inesperados.

Um aspecto importante é verificar o que acontece quando uma operação é iniciada com conexão e a conexão é interrompida durante sua execução.

### 8. Desempenho e consumo de bateria

Em dispositivos móveis, desempenho também está relacionado ao consumo de recursos.

Uma aplicação que utiliza excessivamente:

* Processador;
* Memória;
* Armazenamento;
* Rede;
* GPS;
* Câmera;
* Bateria;

pode prejudicar a experiência do usuário.

Por isso, os testes devem verificar se a aplicação permanece estável e responsiva sem consumir recursos de maneira excessiva.

### 9. Usabilidade em aplicações móveis

A usabilidade móvel precisa considerar o contexto em que o usuário utiliza o dispositivo.

O usuário pode estar:

* Caminhando;
* Em um ambiente com muita iluminação;
* Utilizando apenas uma mão;
* Com conexão instável;
* Em movimento;
* Com pouco tempo disponível.

Por isso, uma boa aplicação móvel deve apresentar:

* Navegação simples;
* Informações claras;
* Botões adequados ao toque;
* Feedback das ações;
* Mensagens de erro compreensíveis;
* Poucos passos desnecessários;
* Adaptação a diferentes tamanhos de tela.

### 10. Web x Mobile

Embora aplicações Web e móveis compartilhem diversos princípios de qualidade, os testes precisam considerar características específicas de cada plataforma.

| Aplicações Web                    | Aplicações móveis                    |
| --------------------------------- | ------------------------------------ |
| Diferentes navegadores            | Diferentes dispositivos              |
| Diferentes sistemas operacionais  | Diferentes versões do sistema        |
| Diferentes resoluções             | Diferentes tamanhos e resoluções     |
| Compatibilidade entre navegadores | Fragmentação de dispositivos         |
| Responsividade                    | Interação por toque e gestos         |
| Condições de rede                 | Mudanças frequentes de conectividade |
| Desempenho do navegador           | Desempenho e consumo de bateria      |
| Acessibilidade e usabilidade      | Sensores e recursos do dispositivo   |

### 11. Mentalidade de testes

Testar não significa apenas verificar se a funcionalidade principal funciona.

É necessário pensar em diferentes situações de uso e perguntar:

* O que acontece em outro navegador?
* O que acontece em uma tela menor?
* O que acontece em um dispositivo com menos recursos?
* O que acontece quando a conexão fica lenta?
* O que acontece quando a conexão é perdida?
* O que acontece quando uma permissão é negada?
* O que acontece quando o usuário muda a orientação da tela?
* O que acontece quando o sistema operacional é diferente ou está em outra versão?

Essa visão amplia a capacidade de identificar problemas antes que eles cheguem aos usuários.

### 12. Qualidade e experiência do usuário

Os testes de aplicações Web e móveis têm como objetivo contribuir para que o software seja:

* **Compatível**, funcionando nos ambientes previstos;
* **Confiável**, mantendo seu comportamento esperado;
* **Estável**, evitando falhas e travamentos;
* **Usável**, permitindo que o usuário realize suas tarefas com facilidade;
* **Responsivo**, adaptando-se aos diferentes dispositivos e tamanhos de tela;
* **Performático**, oferecendo respostas adequadas;
* **Resiliente**, reagindo corretamente a falhas de conexão e outras condições adversas.

Testar diferentes cenários significa aproximar o processo de desenvolvimento das condições reais de utilização do software.
