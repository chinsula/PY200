from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float],
                 occupied_volume: Union[int, float]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    glass_1 = Glass()

    # TODO попробовать инициализировать не корректные объекты
