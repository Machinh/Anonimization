import random
import requests
from stem import Signal
from stem.control import Controller

# Inicializa uma nova sessão Tor
def init_tor_session():
    with Controller.from_port() as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

# Configuração das opções de privacidade e segurança
def configure_privacy(session):
    session.proxies = {
        'http': 'socks5://localhost:9050',
        'https': 'socks5://localhost:9050'
    }
    session.headers.update({
        'User-Agent': generate_random_user_agent(),
        'Accept-Language': 'de-DE,de;q=0.9,en-US,en;q=0.8',
        'DNT': '1',
        'Referer': None
    })
    session.verify = False

# Gera um User-Agent aleatório
def generate_random_user_agent():
    with open('user-agent.txt', 'r') as file:
        user_agents = file.read().splitlines()
    return random.choice(user_agents)

# Envia uma solicitação HTTP segura
def send_secure_request(url):
    session = requests.session()
    configure_privacy(session)
    response = session.get(url)
    print(response.text)

# Uso das funções
init_tor_session()
user_url = input("Digite o URL do site que deseja acessar: ")
send_secure_request(user_url)
