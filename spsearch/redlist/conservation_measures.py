from typing import Mapping
from .translator import Translator
from pathlib import Path

translator = Translator(Path(__file__).parent/'dictionary/conservation_measures/')


class ConservationMeasure:
    """Represents a conservation measure.

    Attributes
    ----------
    code : str
        Conservation measure code.
        See details here: https://www.iucnredlist.org/resources/conservation-actions-classification-scheme
    title : str
        English description of the conservation measure.
    conservation_measure : str
        alias for title
    """

    def __init__(self, code: str =None, title: str =None, data: Mapping[str, str] =None):
        self._data = data

        self.code = code or data and data['code']  # Conservation measure code
        self.title = title or data and data['title']  # Conservation measure type
        self.measure = self.title  # alias for title

        # Conservation measure code
        # https://www.iucnredlist.org/resources/conservation-actions-classification-scheme
        self.rank = len(self.code.split('.')) - 1

    def __str__(self):
        return f"{self.code}: {self.title}"

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.code}: {self.title}>"

    def translate(self, lang: str) -> str:
        return translator.translate(lang, self.code)
