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
        print(f"Erro: O arquivo '{arquivo_origem}' nao foi encontrado.")
        print("Certifique-se de realizar o pull da ultima versao do repositorio.")
        return
        
    df = pd.read_csv(arquivo_origem)
    print(f"Dados extraidos com sucesso. Total de registros: {len(df)}")
    
    # -------------------------------------------------------------------------
    # 2. TRANSFORMAÇÃO (Transform) - Guardrails de LGPD e Qualidade
    # -------------------------------------------------------------------------
    print("Aplicando transformacoes e regras de mascaramento (LGPD)...")
    
    # Padronizacao de strings (remover espacos em branco nas extremidades)
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
    # Mascaramento de Dados Sensiveis / Anonimizacao
    # Garante que dados de auditoria interna nao sejam expostos no BI
    df["Responsavel_IP"] = "127.0.0.1"
    df["Email_Interno"] = "anonimo@clubedovalor.ficticio.com"
    
    # Tratamento de valores nulos para evitar erros na modelagem do Power BI
    if "Status" in df.columns:
        df["Status"] = df["Status"].fillna("Nao Avaliado")
    else:
        print("Aviso: Coluna 'Status' nao encontrada na matriz de origem.")
        
    # Criacao de uma coluna de ID unico para os 117 controles caso nao exista
    if "ID_Controle" not in df.columns:
        df.insert(0, "ID_Controle", range(1, len(df) + 1))
        
    # -------------------------------------------------------------------------
    # 3. CARGA (Load)
    # -------------------------------------------------------------------------
    print("Salvando o arquivo limpo para consumo do Power BI...")
    df.to_csv(arquivo_destino, index=False, encoding="utf-8")
    print(f"Arquivo '{arquivo_destino}' gerado com sucesso.")
    print("=== [ETL] Processo concluido com exito ===")

if __name__ == "__main__":
    executar_etl()
