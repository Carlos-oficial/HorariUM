import requests
import ast


def fetch_landing_html():
    """
    obtem o html da landing page
    """
    reqUrl = "https://alunos.uminho.pt/pt/estudantes/paginas/infouteishorarios.aspx"

    response = requests.request("GET", reqUrl)
    return response.text


def fetch_2nd_stage(form_data):
    reqUrl = "https://alunos.uminho.pt/pt/estudantes/paginas/infouteishorarios.aspx"

    headersList = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.request("POST", reqUrl,headers=headersList,files=form_data)
    return response.text


def fetch_time_sheet_html(form_data):
    reqUrl = "https://alunos.uminho.pt/pt/estudantes/paginas/infouteishorarios.aspx"

    headersList = {
        "Host": "alunos.uminho.pt",
        # "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
        # "Accept": "*/*",
        # "Accept-Language": "en-US,en;q=0.5",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Content-Type": "application/x-www-form-urlencoded",
        # "Content-Length": "68303",
        # "Origin": "https://alunos.uminho.pt",
        # "Connection": "keep-alive",
        # "Referer": "https://alunos.uminho.pt/pt/estudantes/paginas/infouteishorarios.aspx",
        # "Cookie": "_ga=GA1.2.702951698.1636131350; _gid=GA1.2.1022322018.1665494847; _gat=1; WSS_FullScreenMode=false",
        # "Upgrade-Insecure-Requests": "1",
        # "Sec-Fetch-Dest": "document",
        # "Sec-Fetch-Mode": "navigate",
        # "Sec-Fetch-Site": "same-origin",
        # "Sec-Fetch-User": "?1",
        # "Pragma": "no-cache",
        # "Cache-Control": "no-cache"
    }

    # with open("payload2.txt",'r') as f:
    #     payload = f.read()

    response = requests.request("POST", reqUrl, files=form_data, headers=headersList)

    return response.text


if __name__ == "__main__":
    print(fetch_landing_html())
