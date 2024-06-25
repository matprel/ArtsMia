from dataclasses import dataclass

from model.oggetto import Oggetto


@dataclass
class Arco:
    o1: Oggetto
    o2: Oggetto
    peso: int