import nmap
import ipaddress
import pandas

def main():
    alvo: str = input("Digite o IP que deve ser escaneado: ")
    fim: str = "255"
    mapa: nmap = nmap.PortScanner()
    conf: str = "-sn"
    ips: list = []
    mapa.scan(alvo + "-" + fim, arguments=conf)
    
    #Adiciona os IPs escaneados à variável "ips", em seguida os ordena em ordem crescente
    for host in mapa.all_hosts():
        mac = mobo = "Nan"
        items = mapa[host]['vendor'].items()
        if(items):
            for _mac, _mobo in items:
                mac = _mac
                mobo = _mobo
        ips.append([host, mapa[host].state(), mac, mobo])
    org = sorted(ips, key=lambda x: ipaddress.ip_address(x[0]))
    freelst = []
    prev = 1

    #Inicia o processo de identificação de endereços disponíveis
    for ip in org:
        curr = int(ip[0].split('.')[3])
        print(*ip, sep="\t")
        if (curr>prev+1):
            freelst.extend(free_ip_handler(ip_alvo=alvo, ip_atual=curr, ip_anterior=prev))
        prev = curr

    #Caso o último IP em uso tenha o final menor que a variável <fim> (geralmente .255), realiza-se mais uma checagem adicionando todos os IPs do último intervalo em uso até <fim> (.255)
    if (prev<255):
        freelst.extend(free_ip_handler(ip_alvo=alvo, ip_atual=int(fim)+1, ip_anterior=prev)) 
    
    print(f"\n{"-"*50}\n\nLIVRES: \n")
    print(*freelst, sep='\n')

def free_ip_handler(ip_alvo:str, ip_atual:int, ip_anterior:int):
    _ips = []
    for i in range(ip_anterior+1, ip_atual):
        base = ip_alvo.split(".")
        _ips.append(f"{base[0]}.{base[1]}.{base[2]}.{str(i)}")
    return _ips



if(__name__ == "__main__"):
    main()