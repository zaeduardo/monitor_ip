import requests
import time

def get_public_ip(retries=3):
    for _ in range(retries):
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=1)
            response.raise_for_status()  # Lança uma exceção para códigos de status HTTP 4xx/5xx
            ip_address = response.json()['ip']
            return ip_address
        except requests.RequestException as e:
            print(f"Erro ao obter o endereço IP: {e}")
            time.sleep(2)  # Espera 2 segundos antes de tentar novamente
    return None

def main():
    try:
        while True:
            ip_address = get_public_ip()
            if ip_address:
                print(f"Seu endereço IP público é: {ip_address}")
            else:
                print("Não foi possível obter o endereço IP após múltiplas tentativas.")
            
            time.sleep(5)
    except KeyboardInterrupt:
        print("Execução interrompida pelo usuário.")

if __name__ == "__main__":
    main()
