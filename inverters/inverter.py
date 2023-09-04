#!/usr/bin/env python3
from abc import abstractmethod


class Inverter:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ

    def get_data(self):
        return self._get_data()

    @property
    def type(self) -> str:
        return self.typ

    @abstractmethod
    def _get_data(self):
        raise NotImplemented


