from requests_html import AsyncHTMLSession
import asyncio
class Getter:
    def __init__(self,session,script):
        self.session = session
        self.responses = []
        self.errors = []
        self.loop = asyncio.get_event_loop()
        self.script = script
    async def renderQuestion(self, response):
        return await response.html.arender(script=self.script, reload=True)
    
    async def getQuestion(self,urlAt):
        repeat = True
        while repeat:
            try:
                print("connecting: " + urlAt[0])
                response = await self.session.get(urlAt[0])
            except:
                pass
            else:
                repeat = False
        print("rendering: " + urlAt[0])
        try:
            rendered = await self.renderQuestion(response)
        except:
            print("error was on " + urlAt[0])
            self.errors.append(urlAt)
            response.close()
        else:
            response.close()
            print("correct rendered on:" + urlAt[0])
            self.responses.append([rendered, urlAt[1]])
        
    async def getErrorQuestion(self,urlAt):
        print("start error session " +urlAt[0] + " " + urlAt[1])
        errorSession = AsyncHTMLSession()
        repeat = True
        while repeat:
            try:
                print("connecting: " + urlAt[0])
                response = await errorSession.get(urlAt[0])
            except:
                pass
            else:
                repeat = False
        print("rendering: " + urlAt[0])
        try:
            rendered = await self.renderQuestion(response)
        except:
            print("error was on " + urlAt[0])
            self.errors.append(url)
            response.close()
        else:
            del self.errors[self.errors.index(urlAt)]
            response.close()
            print("correct rendered on:" +  urlAt[0])
            self.responses.append([rendered, urlAt[1]])
        await errorSession.close()