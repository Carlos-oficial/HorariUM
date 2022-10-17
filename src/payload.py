import bs4


def get_payload_info(soup):
    div = soup.find("form", attrs={"id": "aspnetForm"})
    return div


def map_payload_info(form):
    inputs = form.find_all("input")

    def get_value(x):
        if "value" in x.attrs:
            return x["value"]
        else:
            return ""

    return {x["id"]: get_value(x) for x in inputs}


def simulate_selection(form):
    form = dict(list(form.items())[:-5])
    form.update(
        {
            "ctl00$ctl40$g_e84a3962_8ce0_47bf_a5c3_d5f9dd3927ef$ctl00$dataCurso": "Licenciatura+em+Engenharia+Informática",
            "ctl00_ctl40_g_e84a3962_8ce0_47bf_a5c3_d5f9dd3927ef_ctl00_dataCurso_ClientState": '{"logEntries":[],"value":"1295","text":"Licenciatura+em+Engenharia+Informática","enabled":true,"checkedIndices":[],"checkedItemsTextOverflows":false}',
        }
    )
    return form


def payload():
    return None


if __name__ == "__main__":
    with open("landing.html", "r") as f:
        soup = bs4.BeautifulSoup(f.read(), "lxml")
    print(simulate_selection(map_payload_info(get_payload_info(soup))))
