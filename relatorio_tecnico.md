# RELATÓRIO TÉCNICO DE IMPLEMENTAÇÃO - GRUPO 23

**Curso:** Análise e Desenvolvimento de Sistemas  
**Disciplina:** Projeto Integrador  
**Professor(a):** Filipo Novo Mór  
**Título do Projeto:** Sistema de Business Intelligence para Gestão de Conformidade e Otimização de Atendimento a Requisitos de Cibersegurança (B2B)  

---

## 1. INTRODUÇÃO E ESCOPO DO PROJETO

Este relatório técnico consolida o desenvolvimento, a arquitetura e os mecanismos de governança aplicados no projeto integrador voltado ao Setor de Infraestrutura e Cibersegurança da empresa parceira **Clube do Valor**. 

O objetivo central do ecossistema foi mitigar a complexidade no atendimento a auditorias externas e questionários de *Due Diligence* de clientes corporativos (B2B). Para isso, estruturou-se uma solução analítica baseada em Business Intelligence (BI), capaz de centralizar matrizes de risco, avaliar níveis de maturidade em segurança da informação e transformar dados brutos em indicadores visuais claros, acionáveis e auditáveis.

---

## 2. GOVERNANÇA, ASPECTOS LEGAIS E LGPD

### 2.1. Termo de Autorização e Consentimento de Uso de Dados
Atendendo aos rigorosos critérios legais e éticos exigidos tanto pela instituição de ensino quanto pelas políticas de governança corporativa, formalizou-se o consentimento de uso de dados e imagem. A autorização foi assinada digitalmente por Leonardo Cardoso, responsável técnico na organização parceira.

**Evidência de Conformidade Jurídica (Termo de Consentimento Assinado):** *Nota: Caso o arquivo abaixo não renderize diretamente na sua tela por limitações do formato PDF, clique no link para abrir o documento original.* [Clique aqui para abrir o Termo de Consentimento Assinado (PDF)](Termo_assinado%20\(1\).pdf)

### 2.2. Adequação da Base de Dados e Versionamento Concluídos com Sucesso
Para mitigar riscos de vazamento de informações corporativas reais, foi executado e homologado com total sucesso o processo de governança e adequação de dados na pasta `Dados_brutos`. Os questionários de avaliação de segurança originais (baseados em modelos da XP Investimentos) foram integralmente tratados, limpos e povoados com valores sintéticos (aleatórios) estruturados em formato `.csv`. 

A conclusão bem-sucedida desta etapa é evidenciada pelos seguintes marcos no repositório:
1. **Integridade Estrutural:** A base de dados anonimizada mantém o mesmo mapeamento de chaves e colunas necessárias para alimentar perfeitamente o script de ETL, sem quebras no pipeline de dados.
2. **Versionamento e Rastreabilidade:** O histórico de *commits* individuais do repositório atesta o versionamento limpo e a autoria das modificações, respeitando as boas práticas de Git e garantindo que nenhum dado confidencial real ficasse retido no histórico de revisões.
3. **Consistência de Ambiente:** A segregação de pastas entre `Dados_brutos`, `Images` e `Imagens_Registro` foi validada pelo grupo, permitindo a reprodução exata da solução por qualquer membro do time ou avaliador externo.

Os dados reais foram substituídos por dados sintéticos (aleatórios) estruturados em formato `.csv` na pasta `Dados_brutos`. Esse processo garantiu que as regras de negócio, cálculos de conformidade e estruturas relacionais permanecessem funcionais para o pipeline de dados, sem expor ativos de informação ou vulnerabilidades reais da empresa parceira.

---

## 3. METODOLOGIA DE GESTÃO E EVIDÊNCIAS SÍNCRONAS

A coordenação interna do projeto adotou premissas do framework ágil para garantir entregas incrementais organizadas. A divisão de papéis e responsabilidades foi distribuída de forma equilibrada entre engenharia de dados, modelagem, conformidade e documentação técnica.

Para assegurar a autoria, integridade e o rastreamento das contribuições, estabeleceu-se uma política rígida de controle de versão no GitHub baseada em *commits* individuais na branch principal. Os alinhamentos estratégicos com os *stakeholders* e as reuniões de progresso técnico (B2B) foram auditadas com capturas síncronas de tela contendo participantes, data e hora visíveis:

### Reunião de Alinhamento Inicial (12/04/2026)
![Reunião Alinhamento 12/04](Imagens_Registro/Reuniao%20Alinhamento%2012-04-26.jpeg)

### Segunda Reunião de Alinhamento (21/04/2026)
![Segunda Reunião Alinhamento 21/04](Imagens_Registro/Segunda%20reuniao%20de%20alinhamento%2021-04-26.jpeg)

### Terceira Reunião de Alinhamento (27/05/2026)
![Terceira Reunião 27/05](Imagens_Registro/Terceira%20Reuniao%2027-05-26.jpeg)

---

## 4. ARQUITETURA DO SISTEMA (C4 MODEL)

A engenharia de software e a modelagem do fluxo de dados da solução analítica foram mapeadas utilizando a metodologia **C4 Model**. Essa abordagem permite segmentar a complexidade do sistema em múltiplos níveis de abstração:

### 4.1. Diagrama C4 Nível 1: Contexto
O primeiro nível delimita as fronteiras do sistema. Ele ilustra como os analistas de segurança e os auditores B2B interagem com a solução de inteligência de conformidade, bem como a relação externa com as matrizes de segurança fornecidas pela organização.

**Modelagem de Contexto do Sistema:** ![Diagrama C4 Nível 1 - Contexto](Images/Nível-1_Contexto.png)

### 4.2. Diagrama C4 Nível 2: Contêiner
O nível de contêiner detalha a arquitetura tecnológica e a engenharia de dados aplicada. O fluxo compreende a extração dos arquivos `.csv` anonimizados, o processamento e tratamento lógico dos dados por meio de scripts automatizados em Python (ETL) e, finalmente, a carga e modelagem relacional dos dados para consumo analítico.

**Modelagem de Contêineres e Componentes:** ![Diagrama C4 Nível 2 - Contêiner](Images/Nível-2_Container.png)

---

## 5. RESULTADOS ALCANÇADOS E ENTREGA TÉCNICA

A conclusão do projeto resultou em um ambiente analítico robusto e integrado que atende plenamente aos objetivos propostos:

1. **Pipeline de Automação (ETL):** O script de Extração, Transformação e Carga desenvolvido em Python garantiu que o tratamento de dados brutos ocorresse sem intervenção manual, padronizando colunas essenciais como *Camada*, *Solução*, *Fabricante* e *Status de Implantação*.
2. **Modelo de Dados Relacional:** A base de dados estruturada no repositório permitiu cruzar os controles de cibersegurança com os frameworks exigidos pelo mercado, facilitando auditorias retroativas.
3. **Painel de Business Intelligence (Power BI):** O dashboard final consolidou métricas críticas, taxas percentuais de aderência a frameworks de segurança e lacunas (*gaps*) de conformidade em tempo real. Isso transformou tabelas densas em relatórios visuais dinâmicos para a tomada de decisão da diretoria.

---

## 6. CONSIDERAÇÕES FINAIS

O Projeto Integrador do Grupo 23 demonstram com sucesso a viabilidade de aplicar conceitos de Engenharia de Dados e Business Intelligence para resolver dores reais de governança e cibersegurança corporativa. 

A arquitetura desenvolvida não apenas cumpre as diretrizes da LGPD por meio de técnicas eficazes de anonimização, mas também entrega valor prático ao Clube do Valor ao reduzir drasticamente o tempo de resposta a auditorias B2B. A experiência prática consolidou competências fundamentais em desenvolvimento ágil, arquitetura de sistemas com C4 Model, automação de dados e conformidade regulatória no perfil profissional dos integrantes do grupo.
