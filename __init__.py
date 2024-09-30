from nonebot.adapters.onebot.v11 import Message
from nonebot import on_command
from nonebot.adapters import Message
from .rule import *
from nonebot.adapters.onebot.v11 import Message
from nonebot.params import CommandArg
from nonebot import require
import asyncio

rgl = require("nonebot_plugin_apscheduler").scheduler

import mcrcon

async def RunMcCmd(args):

    host = ''
    # port = 25575 #有默认端口25575
    password = ''

    rcon = mcrcon.MCRcon(host, password)
    rcon.connect() #连接
    response = rcon.command(args) #执行命令
    # 输出命令响应
    data = (response)
    rcon.disconnect()
    return data
    # pass

# async def RunMcCmd(args):

#     pass

mccmd = on_command('#mc')
@mccmd.handle()
async def _( args: Message = CommandArg()):

    args = args.extract_plain_text().strip()
    
    response = await RunMcCmd(args)

    if args:
        await mccmd.send(response)
    else:
        await mccmd.send('这个命令没有返回内容')

 
@rgl.scheduled_job("interval", seconds=290)
async def _():
    
    args1 = 'say [自动清理] 10秒后清理掉落物品'
    args2 = 'kill @e[type=item]'
    await RunMcCmd(args1)
    await asyncio.sleep(10)
    await RunMcCmd(args2) 

 
@rgl.scheduled_job("interval", seconds=12*60*60) # 12小时
async def _():
    
    args1 = 'say [自动重启] 30秒后自动重启服务器'
    args2 = 'stop'
    await RunMcCmd(args1)
    await asyncio.sleep(30)
    await RunMcCmd(args2)