import os
import pandas as pd

def executar_etl():
    print("=== [ETL] Iniciando o processamento dos dados da Matriz ===")
    
    # -------------------------------------------------------------------------
    # 1. EXTRAÇÃO (Extract)
    # -------------------------------------------------------------------------
    arquivo_origem = "matriz_conformidade_base.csv"
    arquivo_destino = "matriz_conformidade_limpa.csv"
    
    if not os.path.exists(arquivo_origem):
        print(f"Erro: O arquivo '{arquivo_origem}' nao foi encontrado no diretorio.")
        print("Verifique se o nome do arquivo esta correto ou faca o pull no Git.")
        return
        
    # Ajuste 1 e 2: Pula a primeira linha de vírgulas vazias para ler o cabecalho corretamente
    df = pd.read_csv(arquivo_origem, skiprows=1, skip_blank_lines=True)
    
    # Remove colunas fantasmas sem nome (como a Unnamed: 0 criada pela virgula inicial)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    # Remove linhas que sejam completamente nulas
    df = df.dropna(how="all")
    
    print(f"Dados extraidos com sucesso. Total inicial de registros: {len(df)}")
    
    print("Aplicando transformacoes de limpeza e mascaramento LGPD...")
    
    # Padronizacao dos nomes das colunas (removendo espacos extras)
    df.columns = df.columns.str.strip()
    
    # Ajuste 3: Correcao do select_dtypes para limpeza de strings e aspas extras
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()
        # Remove excesso de aspas que vieram da exportacao do arquivo original
        df[col] = df[col].str.replace('"""', '', regex=False)
        
    # Tratamento de Valores Nulos/Vazios e padronizacao do STATUS
    if "STATUS" in df.columns:
        df["STATUS"] = df["STATUS"].fillna("NAO AVALIADO")
        df["STATUS"] = df["STATUS"].str.upper().str.strip()
        
    if "PONTOS" in df.columns:
        df["PONTOS"] = pd.to_numeric(df["PONTOS"], errors="coerce").fillna(0).astype(int)
        
    # Mascaramento de Dados Sensiveis (Guardrail de Privacidade e LGPD)
    df["Responsavel_IP"] = "127.0.0.1"
    df["Email_Interno"] = "anonimo@clubedovalor.ficticio.com"
    
    # Salvando o arquivo tratado
    print("Salvando o arquivo tratado e anonimizado para o Power BI...")
    df.to_csv(arquivo_destino, index=False, encoding="utf-8")
    
    print(f"Arquivo '{arquivo_destino}' gerado com sucesso!")
    print(f"Total final de registros processados: {len(df)}")
    print("=== [ETL] Processo concluido com exito ===")

if __name__ == "__main__":
    executar_etl()
