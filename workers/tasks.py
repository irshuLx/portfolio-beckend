# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from workers.scrapperservice.main import _scrapSymbols, _scrap, _scrapAll, _scrapWatchListTickers, _scrapWatchOptions, _scrapOption


@shared_task
def add(a, b):
    return a + b

##########################################################################################################
# Stock ticker quote tasks
##########################################################################################################


@shared_task
def scrapTicker(ticker):
    return _scrap(ticker)


@shared_task
def scrapTickers():
    return _scrapAll()


@shared_task
def scrapWatchListTickers():
    return _scrapWatchListTickers()


##########################################################################################################
# Options tasks
##########################################################################################################


@shared_task
def scrapWatchOptions():
    return _scrapWatchOptions()


@shared_task
def scrapOption(ticker):
    return _scrapOption(ticker)


@shared_task
def scrapSymbolsNasdaq():
    return _scrapSymbols(True)


@shared_task
def scrapSymbolsNYSE():
    return _scrapSymbols(False)
