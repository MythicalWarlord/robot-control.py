#!/usr/bin/env python

import asyncio
import websockets
import RPi.GPIO as GPIO

LEDPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDPin, GPIO.OUT)

async def control(command):
    async for message in command:
        if message == "on":
            GPIO.output(LEDPin, GPIO.HIGH)
            await command.send(message)
        elif message == "off":
            GPIO.output(LEDPin, GPIO.LOW)
            await command.send(message)


async def main():
    async with websockets.serve(control, "", 8080):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
