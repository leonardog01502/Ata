import sqlite3

def criar_banco_dados():
    conn = sqlite3.connect("atas_relatorios.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS atas (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, local TEXT, hora TEXT, participantes TEXT, assuntos TEXT, conclusoes TEXT, proximos_passos TEXT)''')
     
    cursor.execute('''CREATE TABLE IF NOT EXISTS sugestoes (id INTEGER PRIMARY KEY AUTOINCREMENT, conteudo TEXT)''')
    conn.commit()
    conn.close()

def emitir_ata():
    print("Opção selecionada: Emitir Ata")
    
    data = input("Data da reunião (DD/MM/AAAA): ")
    local = input("Local da reunião: ")
    hora = input("Hora da reunião: ")
    participantes = input("Participantes (separados por vírgula): ")
    assuntos = input("Assuntos discutidos (separados por ponto e vírgula): ")
    conclusoes = input("Conclusões ou decisões da reunião: ")
    proximos_passos = input("Próximos passos ou tarefas definidas: ")
    
    conn = sqlite3.connect("atas_relatorios.db")
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO atas (data, local, hora, participantes, assuntos, conclusoes, proximos_passos) VALUES (?, ?, ?, ?, ?, ?, ?)''',
    (data, local, hora, participantes, assuntos, conclusoes, proximos_passos))
    
    conn.commit()
    conn.close()
    
    print("Ata emitida e salva no banco de dados.")

def emitir_sugestao(ata_id):
    conn = sqlite3.connect("atas_relatorios.db")
    cursor = conn.cursor()

    cursor.execute('''SELECT id, data, local FROM atas''')
    atas = cursor.fetchall()
    for ata in atas:
        print(f"{ata[0]}. Data: {ata[1]} | Local: {ata[2]}")

    ata_id = int(input("Escolha o ID da ata para ver e dar sugestão: "))
    
    cursor.execute('''SELECT * FROM atas WHERE id = ?''', (ata_id,))
    ata = cursor.fetchone()

    print("\nDetalhes da Ata:")
    print(f"Data: {ata[1]}")
    print(f"Local: {ata[2]}")

    emitir_sugestao(ata_id)

    conn.close()

def concluir_ata(ata_id):
    conn = sqlite3.connect("atas_relatorios.db")
    cursor = conn.cursor()

    cursor.execute('''UPDATE atas SET concluida = 1 WHERE id = ?''', (ata_id,))

    conn.commit()
    conn.close()

def consultar_ata():
    conn = sqlite3.connect("atas_relatorios.db")
    cursor = conn.cursor()

    cursor.execute('''SELECT id, data, local FROM atas''')
    atas = cursor.fetchall()
    for ata in atas:
        print(f"{ata[0]}. Data: {ata[1]} | Local: {ata[2]}")

    ata_id = int(input("Escolha o ID da ata para consultar os detalhes: "))
    
    cursor.execute('''SELECT * FROM atas WHERE id = ?''', (ata_id,))
    ata = cursor.fetchone()

    print("\nDetalhes da Ata:")
    print(f"Data: {ata[1]}")
    print(f"Local: {ata[2]}")

    conn.close()

def emitir_relatorio_setor():
    print("Opção selecionada: Emitir Relatório por Setor")
    
    setor = input("Digite o nome do setor para gerar o relatório: ")

    conn = sqlite3.connect("atas_relatorios.db")
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM atas WHERE participantes LIKE ?''', (f"%{setor}%",))
    atas = cursor.fetchall()

    if len(atas) == 0:
        print("Nenhuma ata encontrada para o setor informado.")
    else:
        print("\nRelatório de Atas por Setor:")
        for ata in atas:
            print("\nDetalhes da Ata:")
            print(f"Data: {ata[1]}")
            print(f"Local: {ata[2]}")
            print("===")

    conn.close()

def emitir_relatorio_participante():
    print("Opção selecionada: Emitir Relatório por Participante")

def emitir_relatorio_reuniao():
    print("Opção selecionada: Emitir Relatório por Reunião")

def main():
    criar_banco_dados() 
    while True:
        print("\n--- Menu ---")
        print("1. Emitir Ata")
        print("2. Emitir Sugestão")
        print("3. Concluir Ata")
        print("4. Consultar Ata")
        print("5. Emitir Relatórios")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            emitir_ata()
        elif choice == "2":
            emitir_sugestao()
        elif choice == "3":
            concluir_ata()
        elif choice == "4":
            consultar_ata()
        elif choice == "5":
            print("\n--- Menu de Relatórios ---")
            print("1. Relatório por Setor")
            print("2. Relatório por Participante")
            print("3. Relatório por Reunião")

            report_choice = input("Escolha uma opção de relatório: ")

            if report_choice == "1":
                emitir_relatorio_setor()
            elif report_choice == "2":
                emitir_relatorio_participante()
            elif report_choice == "3":
                emitir_relatorio_reuniao()
            else:
                print("Opção inválida.")
        elif choice == "6":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    print("Bem-vindo ao Sistema de Emissão de Atas e Relatórios!")
    main()