# Projeto Integrador - ADS LaSalle (2026)

Este projeto consiste no desenvolvimento de uma solução de Business Intelligence (Power BI) integrada a um pipeline de dados em Python. O objetivo é monitorar e auditar o nível de adequação regulatória da infraestrutura de TI do Clube do Valor frente aos controles de cibersegurança exigidos pela XP Inc., ANBIMA, LGPD e NIST CSF 2.0.

---

## Integrantes e Papéis
* **Isaak:** Product Owner & Arquiteto de Soluções
* **Chrys:** Engenheiro de Dados
* **Andrean:** Desenvolvedor BI
* **José:** Tech Writer & Governança do Repositório
* **Savana:** Analista de Compliance
* **Márcia:** Gestora de Riscos

---

## Estrutura de Arquivos do Repositório
* [`Dashboard.pbix`](Dashboard.pbix): Painel do Power BI focado na gestão de conformidade.
* [`etl_matriz_conformidade.py`](etl_matriz_conformidade.py): Script em Python utilizado para a limpeza e tratamento dos dados.
* `matriz_conformidade_limpa.csv` / `matriz_importacao_pbi.csv`: Bases de dados tratadas e anonimizadas.
* [`atas_de_reuniao.md`](atas_de_reuniao.md): Registro das reuniões síncronas do grupo (Diário de Campo).
* [`relatorio_tecnico.md`](relatorio_tecnico.md): Relatório técnico final de implementação (com arquitetura C4 Model). 
* `Relatorio de Auditoria.docx` / [`analise_lgpd.md`](analise_lgpd.md): Documentação analítica sobre riscos e privacidade.
* [`Termo_assinado (1).pdf`](Termo_assinado%20\(1\).pdf): Termo de aceite do projeto.
* `Images/` / `Imagens_Registro/`: Pastas com os diagramas de arquitetura e capturas de tela das reuniões.

*Nota de Compliance: Para garantir a conformidade com a LGPD, todos os dados sensíveis de infraestrutura, e-mails ou IPs foram macronados ou anonimizados na etapa de tratamento de dados.*

---

## 🚀 Guia de Implantação B2B

Este repositório contém a versão acadêmica e sanitizada do Sistema de BI de Conformidade. Para implantar a solução no ambiente de produção da empresa, siga os passos abaixo:

1. **Clonagem do Repositório:** 
   Clone este projeto para um ambiente local seguro utilizando `git clone`.

2. **Ingestão de Dados Reais:**
   Substitua os arquivos `matriz_conformidade_limpa.csv` da pasta `/dados` pelas planilhas reais de auditoria (sem passar pelo script de anonimização, caso o uso seja estritamente interno e em conformidade com as políticas de TI da empresa).

3. **Configuração do Power BI:**
   - Abra o arquivo `BI_Conformidade_B2B.pbix`.
   - Acesse `Página Inicial > Transformar Dados > Configurações da Fonte de Dados`.
   - Altere o caminho (`Path`) para o diretório onde os CSVs reais foram salvos.
   - Clique em **Aplicar Alterações** e aguarde o recálculo das medidas DAX.

4. **Publicação:**
   Publique o relatório em um Workspace seguro do Power BI com controle de acesso (Row-Level Security) habilitado para os perfis de CISO e Analistas.
