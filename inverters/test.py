#!/usr/bin/env python3
from .inverter import Inverter


def get_data(d) -> dict:
    return d


class Test(Inverter):
    def __init__(self, d={'watt': 42, 'kwh': 100}, name='Test'):
        """
        Test inverter class
        """
        super().__init__(name, typ='Test')
        self.d = d

    def _get_data(self):
        return get_data(self.d)


if __name__ == '__main__':
    t = Test()
    print(t.get_data())