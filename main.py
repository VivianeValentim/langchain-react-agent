from src.agent import build_agent_executor

def main():
    print("\n" + "="*50)
    print("Agentic Query Router Iniciado")
    print("Digite 'sair' para encerrar a aplicação.")
    print("="*50 + "\n")
    
    agent_executor = build_agent_executor()
    
    while True:
        try:
            user_input = input("\nVocê: ")
            
            if user_input.lower() in ['sair', 'exit', 'quit']:
                print("Encerrando o agente. Até logo!")
                break
                
            if not user_input.strip():
                continue
                
            # Invoca o agente com a pergunta do usuário
            response = agent_executor.invoke({"input": user_input})
            
            print(f"\nIA: {response['output']}\n")
            print("-" * 50)
            
        except KeyboardInterrupt:
            print("\nEncerrando o agente. Até logo!")
            break
        except Exception as e:
            print(f"\n[Erro inesperado]: {e}\n")

if __name__ == "__main__":
    main()