from dataclasses import dataclass

@dataclass
class Progect:
    name: str
    descripiton: str
    strat_time : str
    task_list: list[dict]
    liguage: str 
