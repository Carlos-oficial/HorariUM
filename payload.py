import bs4


def get_payload_info(soup):
    div = soup.find_all("form", attrs={"id": "aspnetForm"})
    return div


def map_payload_info(divs):
    inputs = []
    # print(divs)
    for x in divs:
        inputs.append(x.find_all("input"))
    print(inputs[0][0]["id"])
    
    # return {x["name"]: x["value"] for x in inputs}


def simulate_selection():
    return None


def payload():
    return None

if __name__ == '__main__':
    with open("landing.html",'r') as f:
        soup=bs4.BeautifulSoup(f.read(),"lxml")
    # print(soup)
    print((get_payload_info(soup)))