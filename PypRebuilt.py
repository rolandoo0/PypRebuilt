import os

try:
    import pyppeteer
except:
    os.system("pip3 install pyppeteer")
try:
    import pyppeteer_stealth
except:
    os.system("pip3 install pyppeteer_stealth")

from pyppeteer import launch
from pyppeteer_stealth import stealth


class PyppeteerRebuilt:
    def __init__(self, args: dict = {"headless": True}):
        """
        Initialize the class by passing in a dictionary containing the headless key and
        a bool as the value as you would in the usual pyppeteer.launch() function
        i.e. main = PypRebuilt({'headless': True})
        """
        self.args = args
        self.browser = None

    async def loadPage(self, url: str, **kwargs):
        """
        This function will a page defined by the url passed in as an argument
        ALL ASYNC functions MUST be awaited.
        Timeout is in milliseconds
        i.e. await main.loadPage("https://www.google.com", 1000)
        """
        self.browser = await launch(self.args)
        self.page = await self.browser.newPage()
        await self.page.goto(url, **kwargs)

    async def loadPageStealth(self, url: str, **kwargs):
        """
        This function will load the page using the stealth pyppeteer plugin
        i.e. await main.loadPageStealth("https://www.google.com")
        """
        self.browser = await launch(self.args)
        self.page = await self.browser.newPage()
        await stealth(self.page)
        await self.page.goto(url, **kwargs)

    async def getPageContent(self):
        """
        This function will return the html of the page
        i.e. await main.getPageContent('https://www.google.com')
        """
        return await self.page.content()

    async def click(self, selector: str, options={}, **kwargs):
        """
        This function will click a certain element on the page
        determined by a specific selector passed in as an argument
        i.e. await main.click('#search')
        """
        await self.page.click(selector, options, **kwargs)

    async def executeScript(self, script: str, *args):
        """
        This function will execute a certain scrpit on the page
        i.e. await main.executeScript('document.querySelector("#search").value = "Hello World!"')
        """
        await self.page.evaluate(script, *args)

    async def getInnerText(self, selector: str, *args):
        """
        This function will return the value of a certain element on the page
        i.e. await main.getInnerText('#search')
        """
        return await self.page.querySelectorEval(
            selector, "node => node.textContent", *args
        )

    async def screenShot(self, options={}, **kwargs):
        """
        This function screenshots the current page
        i.e. await main.screenshot('screenshot.png')
        """
        await self.page.screenshot(options, **kwargs)
