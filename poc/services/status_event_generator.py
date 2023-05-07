
import asyncio
from services import StatusQue
'''
Get status as an event generator
'''
status_stream_delay = 5  # second
status_stream_retry_timeout = 30000  # milisecond
newData = False
queue = StatusQue.Singleton().getInstance()
myQueue = queue._Singleton__queue

def checkKey( key):
    if key in myQueue.keys():
        return True
    else:
        return False

def setStaus(status):
    print("changing  status::",status)
    # print("previos status::",newData)
    newData = status

    # print("Current status::",newData)
async def compute_status(param1):
    
    if not checkKey(param1):
        dummy = {param1: True}
        myQueue.update(dummy)
    print("Sending  status::",newData)
    print("param1::",param1)
    print("Que value",queue._Singleton__queue[param1])

    return queue._Singleton__queue[param1]
    

async def status_event_generator(request, param1):
    previous_status = False
   
    while True:
        if await request.is_disconnected():
            print('Request disconnected')
            break

        # if previous_status and previous_status['some_end_condition']:
        #     print('Request completed. Disconnecting now')
        #     yield {
        #         "event": "end",
        #         "data" : ''
        #     }
        #     break

        current_status = await compute_status(param1)
        # print("current_status::",current_status)
        # 
        if previous_status != current_status:
            yield {
                "event": "update",
                "retry": status_stream_retry_timeout,
                "data": current_status
            }
            previous_status = current_status
            print('Current status :%s', current_status)
        else:
            print('No change in status...')

        await asyncio.sleep(status_stream_delay)