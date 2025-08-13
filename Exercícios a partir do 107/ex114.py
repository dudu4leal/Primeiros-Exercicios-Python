#código em Python que testa se o site pudim está acessível pelo computador usado.

import requests


def verificar_site(url):

    try:

        response = requests.get(url, timeout=5) 

        if response.status_code == 200:

            print('O site do pudim está acessível no momento')

    except:

        print('O site do pudim não está acessível neste momento')

siteUrl = 'https://www.pudim.com.br'

verificar_site(siteUrl)




