# 📑 Engenharia de Dados e Diretrizes de Modelagem (Power BI)

Este documento estabelece o Dicionário de Dados, a Arquitetura de Modelagem e os Guardrails de Governança para o desenvolvimento do Dashboard de Conformidade de Segurança da Informação, atendendo aos requisitos B2B do setor de Infraestrutura e Operações do **Clube do Valor**.

---

## 🛡️ 1. Guardrails Inegociáveis (LGPD & Edital)
*   **Anonimização Estrita:** Todas as credenciais, e-mails reais, senhas, chaves de API e IPs verdadeiros da infraestrutura do Clube do Valor foram totalmente mascarados e substituídos por dados fictícios/estáticos no pipeline de dados (`matriz_importacao_pbi.csv`).
*   **Regra de Links Internos (Sistema Lex):** É expressamente proibido embutir hiperlinks e URLs externas no modelo de relatório final. Quaisquer validações de tela ou do Power BI deverão ser documentadas via Captura de Tela (Print Screen) estática no PDF.

---

## 🗺️ 2. Dicionário de Dados (`matriz_importacao_pbi.csv`)

O arquivo limpo e otimizado via script Python (`pandas`) possui a seguinte estrutura e tipagem obrigatória para importação no Power Query:

| Nome da Coluna | Tipo no PBI | Descrição / Regra de Negócio | Exemplo |
| :--- | :--- | :--- | :--- |
| **`SK_CONTROLE`** | Texto | **Surrogate Key (Chave Substituta):** Identificador único gerado por algoritmo a partir da concatenação do código do Domínio com o ID para blindar relacionamentos no Modelo Estrela. | `PRI_1`, `MON_12` |
| **`ID`** | Número Inteiro | Identificador sequencial da questão dentro do seu respectivo macrodomínio. | `1`, `2` |
| **`DOMÍNIO`** | Texto | Macrodomínio de Segurança da Informação baseado nos frameworks (XP Inc., ANBIMA, NIST CSF 2.0). Padronizado em CAIXA ALTA. | `PRIVACIDADE`, `CONTROLE DE ACESSO` |
| **`QUESTÃO`** | Texto | Enunciado técnico do controle ou pergunta da auditoria B2B. | *"A empresa mantém registro de..."* |
| **`STATUS`** | Texto | Situação atual do controle no ambiente interno. Padronizado para categorização limpa em filtros. | `IMPLEMENTADO`, `PARCIALMENTE`, `NÃO IMPLEMENTADO` |
| **`CRITICIDADE DO CONTROLE`**| Texto | Peso do controle no apetite de risco da instituição. | `ALTA`, `MÉDIA`, `BAIXA` |
| **`PONTOS`** | Número Inteiro | Pontuação bruta atribuída ao nível de maturidade do controle (Nulos tratados para `0`). | `0`, `10`, `20` |
| **`Ref. Política`** | Texto | Código de referência da norma ou política de SI de terceiros. | `7.2.1`, `7.2.2` |
| **`Responsavel_IP`** | Texto | Dado controlado de segurança (Mapeado estritamente como `127.0.0.1` para conformidade). | `127.0.0.1` |
| **`Email_Interno`** | Texto | E-mail corporativo mascarado para governança de auditoria. | `anonimo@clubedovalor...` |

---

## 📐 3. Arquitetura DAX para o Desenvolvedor de BI (Andrean)

Para garantir que as métricas gerenciais reflitam fielmente os 117 controles avaliados da Matriz XP Investimentos, as seguintes medidas DAX devem ser implementadas no repositório `.pbix`:

### A. Percentual Geral de Adequação (%)
Calcula a taxa de conformidade desconsiderando os itens marcados como "Não Aplicável", evitando distorções no score de segurança:

```dax
% Adequacao SI = 
DIVIDE(
    CALCULATE(COUNT(matriz_importacao_pbi[SK_CONTROLE]), matriz_importacao_pbi[STATUS] = "IMPLEMENTADO"),
    CALCULATE(COUNT(matriz_importacao_pbi[SK_CONTROLE]), matriz_importacao_pbi[STATUS] <> "NÃO APLICÁVEL"),
    0
)

Status Risco = 
SWITCH(
    TRUE(),
    [% Adequacao SI] <= 0.59, "RISCO ALTO",
    [% Adequacao SI] > 0.59 && [% Adequacao SI] <= 0.75, "RISCO MODERADO",
    [% Adequacao SI] >= 0.76, "RISCO BAIXO",
    "NÃO AVALIADO"
)
