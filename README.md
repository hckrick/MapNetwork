# RickScript

RickScript é uma ferramenta Python de diagnóstico de redes e simulação de ataques DDoS. O script oferece várias funcionalidades para análise de rede, incluindo escaneamento com Nmap e simulação de ataques com hping3. Ele também vem com uma interface interativa e colorida, melhorando a experiência do usuário.

## Funcionalidades

- **Diagnóstico de Rede**: Realize varreduras de rede usando Nmap com diferentes tipos de escaneamento.
- **Exibição de IPs Ativos**: Mostre os endereços IP ativos na rede local.
- **Simulação de Ataque DDoS**: Simule ataques DDoS usando hping3.
- **Easter Egg**: Divirta-se com um Easter Egg escondido no menu.

## Instalação

Antes de usar o script, você precisa garantir que as dependências estejam instaladas. Execute o seguinte comando para instalar as bibliotecas Python necessárias:

```bash
pip install colorama


Instalação do Nmap e hping3
O script verificará se nmap e hping3 estão instalados. Se não estiverem, ele oferecerá a opção de instalá-los. Aqui está como instalar manualmente:

Nmap:

Linux (Debian/Ubuntu): sudo apt install nmap
Linux (CentOS/Red Hat): sudo yum install nmap
macOS: brew install nmap
Windows: Baixe e instale a partir de Nmap.org
hping3:

Linux: sudo apt install hping3
macOS: brew install hping
Windows: Baixe e instale a partir de hping.org
Uso
Para executar o script, use o seguinte comando:

bash
Copiar código
python rickscript.py
Menu Principal
Diagnóstico de Rede (Nmap): Escolha o tipo de varredura e insira o endereço IP ou range para escanear.
Exibir Endereços IP Ativos: Mostre os IPs ativos na rede local.
Simular Ataque DDoS (hping3): Insira o IP do alvo e a duração do ataque.
Sair: Encerre o script.
Easter Egg: Descubra uma surpresa divertida!
Aviso de Responsabilidade
A simulação de ataques DDoS deve ser realizada com responsabilidade e somente em ambientes controlados e com permissão apropriada. O uso inadequado de ferramentas de rede pode ser ilegal e antiético. Utilize este script para fins educacionais e de teste apenas.

Licença
Este projeto é licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contribuições
Se você deseja contribuir para este projeto, sinta-se à vontade para enviar um pull request. Sugestões e melhorias são bem-vindas!
