# RickScript

RickScript é uma ferramenta Python interativa projetada para diagnóstico de redes e simulação de ataques DDoS. Ele oferece funcionalidades para análise de rede utilizando Nmap e simulação de ataques com hping3, além de uma interface colorida e divertida.

## Funcionalidades

- **Diagnóstico de Rede (Nmap)**: Realize varreduras de rede com diferentes tipos de escaneamento.
- **Exibição de IPs Ativos**: Mostre os endereços IP ativos na rede local.
- **Simulação de Ataque DDoS (hping3)**: Simule ataques DDoS para fins educacionais e de teste.
- **Easter Egg**: Descubra uma surpresa divertida oculta no menu!

## Instalação

### Requisitos

- **Python**: Certifique-se de que o Python 3 está instalado no seu sistema.
- **Dependências Python**: Você precisa instalar a biblioteca `colorama`.

### Instalação das Dependências

Instale as dependências Python usando o seguinte comando:

```bash
pip install colorama

```
## Instalação do Nmap e hping3
O script verifica se nmap e hping3 estão instalados e oferece a opção de instalá-los automaticamente. Se preferir instalar manualmente, siga as instruções abaixo:

Nmap:

Linux (Debian/Ubuntu): sudo apt install nmap
Linux (CentOS/Red Hat): sudo yum install nmap
macOS: brew install nmap
Windows: Baixe e instale a partir de Nmap.org
hping3:

Linux: sudo apt install hping3
macOS: brew install hping
Windows: Baixe e instale a partir de hping.org

### Uso
Para executar o script, use o seguinte comando:

```bash
python rickscript.py
```
### Menu Principal
Diagnóstico de Rede (Nmap): Escolha o tipo de varredura e insira o endereço IP ou range para escanear.
Exibir Endereços IP Ativos: Mostre os IPs ativos na rede local.
Simular Ataque DDoS (hping3): Insira o IP do alvo e a duração do ataque.
Sair: Encerre o script.
Easter Egg: Descubra uma surpresa divertida!
Aviso de Responsabilidade

A simulação de ataques DDoS deve ser realizada com responsabilidade e somente em ambientes controlados e com permissão apropriada. O uso inadequado de ferramentas de rede pode ser ilegal e antiético. Utilize este script para fins educacionais e de teste apenas.

### Licença
Este projeto é licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

### Contribuições
Se você deseja contribuir para este projeto, sinta-se à vontade para enviar um pull request. Sugestões e melhorias são bem-vindas!

