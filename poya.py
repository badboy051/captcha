import bs4
import requests
import random
import shutil


class Poya:
    rand2: str
    rand1: int
    file_name : str
    def __init__(self):
        self.se = requests.session()
        self.get_rands()
        self.get_image()

    def get_rands(self):
        result = self.se.get("https://pooya.sadjad.ac.ir/gateway/PuyaAuthenticate.php")
        bs = bs4.BeautifulSoup(result.text, "html.parser")
        self.rand2 = bs.find("input", {"id": "rand2"}).attrs.get("value")
        self.rand1 = random.randint(100000000, 999999999)

    def get_image(self):
        url = "https://pooya.sadjad.ac.ir/gateway/SecurityImage/ShowSecurityImage.php?rand1={}&rand2={}"
        url = url.format(self.rand1, self.rand2)
        print(url)
        result = self.se.get(url, stream=True)
        with open(str(self.rand1) + ".png", 'wb') as file:
            result.raw.decode_content = True
            shutil.copyfileobj(result.raw, file)
        self.file_name = str(self.rand1) + ".png"
