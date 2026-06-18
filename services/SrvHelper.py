import asyncio
from datetime import datetime
import time

class SrvHelper:   
    
    def getDateNowIso(self):
        return datetime.now().isoformat()



    def getDateString(self):
        now = datetime.now().isoformat()
        arr_date = now.split('T')[0].split('-')
        arr_time = now.split('T')[1].split(':')
        str = f"{arr_date[2]}{arr_date[2]}{arr_date[1]}_{arr_time[0]}{arr_time[1]}{arr_time[2].split('.')[0]}"
        return str
    


    async def delay(self, dur):
        if(dur > 0) : 
            dur = dur 
        else : dur = 2 
        await asyncio.sleep(dur)
        return


SrvHelper = SrvHelper()