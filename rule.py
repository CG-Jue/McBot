from nonebot.adapters.onebot.v11 import Event


async def checkIfListenpro(event: Event):

     
    templist = [] # 群号列表
    
    for id in templist:
        if id == event.group_id:
            return True
    return False


