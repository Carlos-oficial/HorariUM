import bs4


def fetch_cells(sopa):
    """
    separa um soup object da tabela do horario numa matriz de células individuais
    """
    lines = sopa.find_all("tr")
    cells = [line.find_all("td") for line in lines]
    return cells


class Class:
    """
    classe que representa uma aula
    """

    weekdays = ["mon", "tue", "wed", "thu", "fri"]

    def __init__(self, day, init_time, duration, subject, shift, room):
        self.day = day  # 0..4
        self.init_time = init_time  # (H,M)
        self.duration = duration  # (H,M)
        self.subject = subject
        self.shift = shift
        self.room = room

    def __repr__(self):
        return f"""
day:{Class.weekdays[self.day]}
from {self.init_time[0]}:{self.init_time[1]} to {self.init_time[0]+self.duration[0]+((self.init_time[1]+self.duration[1])>60)}:{self.init_time[1]+self.duration[1]%60}
subject: {self.subject}
shift: {self.shift}
room:{self.room}\n"""


def get_classes_from_cell(cell):
    """
    obtem as divs que contêm a informação das aulas numa célula da tabela
    """
    if cell.find("div"):
        child = [
            (x["title"], x["style"])
            for x in cell.find("div").find_all(
                "div", attrs={"class": "rsApt rsAptSimple"}
            )
        ]
        return child
    else:
        return []


def get_all_cells(soup):
    """
    obtém as todas as células da tabela html
    """
    sopa = soup.find("td", attrs={"class": "rsContentWrapper"})
    cells = fetch_cells(sopa)
    return [
        [get_classes_from_cell(cell) for cell in cells[x]] for x, _ in enumerate(cells)
    ]



def map_classes(matrix):
    """
    recebe uma matriz de pares (title,style) e retorna uma lista de objetos Class populados com a informação de cada par
    """
    li = []

    def get_duration(_class):
        return int(_class[1].split("height:")[1].split("px")[0]) / 236 * 2

    for h, hour in enumerate(matrix):
        for d, day in enumerate(hour):
            for _class in day:
                li.append(
                    Class(
                        d,
                        (8 + h // 2, 0 + (30 * h % 2)),
                        (
                            int(get_duration(_class)),
                            int(get_duration(_class) % 1 * 10) * 60,
                        ),
                        _class[0].split("\n")[0],
                        _class[0].split("\n")[2],
                        _class[0].split("\n")[1],
                    )
                )
    return li


if __name__ == "__main__":
    pass
