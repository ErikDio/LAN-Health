import nmap
import ipaddress
import pandas
import os

def main():
    local_arquivo = os.path.dirname(os.path.realpath(__file__))
    print(local_arquivo)
    print(os.path.exists(local_arquivo+'/arquivo.txt'))
    alvo:str = ""
    fim:int = 255
    mapa:nmap.nmap.PortScanner
    conf:str = "-sn"
    ips:list = []
    ipzinho = {}

    #Coleta o IP que deve ser escaneado e informações adicionais caso fornecidas.
    while True:
        try:
            alvo = input("Digite o IPv4 que deve ser escaneado:\n")
            ipaddress.IPv4Address(alvo)
            break
        except ValueError:
            print("Ip inválido.")
    print(f"\n{"-"*50}\n")

    while True:
        try:
            fim = int(input("Qual o final do último IP que deve ser escaneado? (pressione ENTER para o padrão 255)\n"))
            break
        except ValueError:
            print("IP final definido para 255")
            fim = 255
            break
    mapa = scan(alvo + "-" + str(fim), conf)

    #Adiciona os IPs e MACs escaneados à variável "ips", em seguida os ordena em ordem crescente
    for host in mapa.all_hosts():
        mac = mac_detalhe = "Nan"
        items = mapa[host]['vendor'].items()
        if(items):
            for _mac, _macdet in items:
                mac = _mac
                mac_detalhe = _macdet
        ips.append([host, mapa[host].state(), mac, mac_detalhe])
        ipzinho[host] = {"status":mapa[host].state(),"mac":mac,"detalhe":mac_detalhe}
    ips_org = sorted(ips, key=lambda x: ipaddress.ip_address(x[0]))
    ipzinho = dict(sorted(ipzinho.items(), key=lambda item: int(ipaddress.ip_address(item[0]))))
    freelst = []
    prev = 1
    print(ipzinho)
    #Inicia o processo de identificação de endereços disponíveis
    for ip in ipzinho:
        curr = int(ip[0].split('.')[3])
        #print(*ip, sep="\t")
    #    if (curr>prev+1):
    #        freelst.extend(free_ip_handler(ip_alvo=alvo, ip_atual=curr, ip_anterior=prev))
    #    prev = curr
    for ip in ipzinho:
        print(f"{ip}\tstatus: {ipzinho[ip]['status']}\tmac: {ipzinho[ip]['mac'].ljust(20)}\tdetalhe: {ipzinho[ip]['detalhe']}")
    #Caso o último IP em uso tenha o final menor que a variável <fim> (geralmente .255), realiza-se mais uma checagem adicionando todos os IPs do último intervalo em uso até <fim> (.255)
    if (prev<255):
        freelst.extend(free_ip_handler(ip_alvo=alvo, ip_atual=fim+1, ip_anterior=prev)) 

    #print(f"\n{"-"*50}\n\nLIVRES: \n")
    #print(*freelst, sep='\n')

def scan(target, conf): #Responsável por executar o NMAP no IP fornecido
    resultado = nmap.PortScanner()
    try:
        resultado.scan(target, arguments=conf)
    except Exception as erro:
        input(f"O programa retornou o erro '{erro}' ao tentar escanear a rede solicitada.\nPressione ENTER para para sair.\n")
    return resultado

def free_ip_handler(ip_alvo:str, ip_atual:int, ip_anterior:int): #Detecta quais IPs estão livres e os retorna
    _ips = []
    for i in range(ip_anterior+1, ip_atual):
        base = ip_alvo.split(".")
        _ips.append(f"{".".join(base[:-1])}.{str(i)}")
    return _ips


if(__name__ == "__main__"):
    main()