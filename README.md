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
