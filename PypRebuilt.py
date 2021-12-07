import os

try:
    import pyppeteer
except:
    os.system("pip3 install pyppeteer")
try:
    import pyppeteer_stealth
except:
    os.system("pip3 install pyppeteer_stealth")
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth


class PyppeteerRebuilt:
    # Initialize the class by passing in a dictionary containing the headless key and
    # a bool as the value as you would in the usual pyppeteer.launch() function
    # i.e. main = PypRebuilt({'headless': True})
    def __init__(self, args: dict):
        self.args = args

    # This function will a page defined by the url passed in as an argument
    # ALL ASYNC functions MUST be awaited.
    # Timeout is in milliseconds
    # i.e. await main.loadPage("https://www.google.com", 1000)
    async def loadPage(self, url: str):
        self.browser = await launch(self.args)
        self.page = await self.browser.newPage()
        await self.page.goto(url)

    # This function will load the page using the stealth pyppeteer plugin
    # i.e. await main.loadPageStealth("https://www.google.com")
    async def loadPageStealth(self, url: str):
        self.browser = await launch(self.args)
        self.page = await self.browser.newPage()
        await stealth(self.page)
        await self.page.goto(url)

    # This function will return the html of the page
    # i.e. await main.getPageContent('https://www.google.com')
    async def getPageContent(self):
        return await self.page.content()

    # This function will click a certain element on the page
    # determined by a specific selector passed in as an argument
    # i.e. await main.click('#search')
    async def click(self, selector: str):
        await self.page.click(selector)

    # This function will execute a certain scrpit on the page
    # i.e. await main.executeScript('document.querySelector("#search").value = "Hello World!"')
    async def executeScript(self, script: str):
        await self.page.evaluate(script)

    # This function will return the value of a certain element on the page
    # i.e. await main.getInnerText('#search')
    async def getInnerText(self, selector: str):
        return await self.page.querySelectorEval(selector, "node => node.textContent")
