import os
import subprocess
import signal
import asyncio

from evdev import InputDevice, list_devices

devices = map(InputDevice, tuple(list_devices()))

async def get_event_id(device):
    async for event in device.async_read_loop():
        return device_id


async def print_events(device):
    global device_id
    async for event in device.async_read_loop():
        device_id = device.path
        print(device_id)

for device in devices:
    if "mouse" not in device.name.lower():
        asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()
