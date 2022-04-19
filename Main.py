from bluez_peripheral.util import *
from bluez_peripheral.advert import Advertisement
from bluez_peripheral.agent import NoIoAgent
from Service import WifiService

import asyncio

async def main():
    bus = await get_message_bus()

    #create the service and register it to the bus
    service = WifiService()
    await service.register(bus)

    # An agent is required to handle pairing 
    agent = NoIoAgent()
    # This script needs superuser for this to work.
    await agent.register(bus)

    adapter = await Adapter.get_first(bus)
    
    #advert with infinite timeout
    advert = Advertisement("Blackmirror", ["844F"], 0x0A02, 0)
    await advert.register(bus, adapter)

    while True:
        # Handle dbus requests.
        await asyncio.sleep(5)

    await bus.wait_for_disconnect()

if __name__ == "__main__":
    asyncio.run(main())