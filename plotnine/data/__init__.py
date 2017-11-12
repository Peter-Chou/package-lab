# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import pandas as pd
import os

__all__ = ['pg_mean', 'BOD', 'cabbage_exp', 'diamonds', 'upc',
           'csub', 'tophitters2001', 'worldpop', 'ToothGrowth',
           'uspopage', 'climate', 'heightweight', 'biopsy',
           'faithful', 'countries', 'birthwt', 'countries2009',
           'PlantGrowth', 'mpg', 'marathon', 'Animals', 'wind',
           'economics', 'mtcars']

__all__ = [str(u) for u in __all__]
_ROOT = os.path.abspath(os.path.dirname(__file__))

pg_mean = pd.read_csv(os.path.join(_ROOT, "pg_mean.csv"), index_col=0)
BOD = pd.DataFrame({"Time": [1, 2, 3, 4, 5, 7], 'demand': [8.3, 10.3, 19.0, 16.0, 15.6, 19.8]})
cabbage_exp = pd.read_csv(os.path.join(_ROOT, "cabbage_exp.csv"), index_col=0)
diamonds = pd.read_csv(os.path.join(_ROOT, "diamonds.csv"), index_col=0)
upc = pd.read_csv(os.path.join(_ROOT, "upc.csv"))
csub = pd.read_csv(os.path.join(_ROOT, "csub.csv"), index_col=0)
tophitters2001 = pd.read_csv(os.path.join(_ROOT, "tophitters2001.csv"), index_col=0)
worldpop = pd.read_csv(os.path.join(_ROOT, "worldpop.csv"), index_col=0)
ToothGrowth = pd.read_csv(os.path.join(_ROOT, "ToothGrowth.csv"), index_col=0)
uspopage = pd.read_csv(os.path.join(_ROOT, "uspopage.csv"), index_col=0)
climate = pd.read_csv(os.path.join(_ROOT, "climate.csv"), index_col=0)
heightweight = pd.read_csv(os.path.join(_ROOT, "heightweight.csv"), index_col=0)
biopsy = pd.read_csv(os.path.join(_ROOT, "biopsy.csv"), index_col=0)
faithful = pd.read_csv(os.path.join(_ROOT, "faithful.csv"), index_col=0)
countries = pd.read_csv(os.path.join(_ROOT, "countries.csv"), index_col=0)
birthwt = pd.read_csv(os.path.join(_ROOT, "birthwt.csv"), index_col=0)
birthwt['smoke1'] = birthwt['smoke'].replace({0: 'No Smoke', 1: 'Smoke'})
countries2009 = countries.query('Year==2009 and healthexp>2000').copy()
PlantGrowth = pd.read_csv(os.path.join(_ROOT, "PlantGrowth.csv"), index_col=0)
mpg = pd.read_csv(os.path.join(_ROOT, "mpg.csv"))
marathon = pd.read_csv(os.path.join(_ROOT, "marathon.csv"), index_col=0)
Animals = pd.read_csv(os.path.join(_ROOT, "Animals.csv"), index_col=0)
wind = pd.read_csv(os.path.join(_ROOT, "wind.csv"), index_col=0)
economics = pd.read_csv(os.path.join(_ROOT, "economics.csv"), index_col=0)
economics['date'] = pd.to_datetime(economics['date'])
mtcars = pd.read_csv(os.path.join(_ROOT, "mtcars.csv"), index_col=0)
