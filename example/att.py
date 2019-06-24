"""
Copyright (c) 2019 Giovanni (iGio90) Rocca

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import frida
import os
import sys


def on_message(message, payload):
    if 'payload' in message:
        message = message['payload']
        print(message)
    else:
        print(message)


if not os.path.exists('_agent.js'):
    print('use `npm install` to build the agent')
    exit(0)

d = frida.get_usb_device()
pid = d.spawn('com.my.target')
session = d.attach(pid)
script = session.create_script(open('_agent.js', 'r').read())
script.on('message', on_message)
script.load()
d.resume(pid)
sys.stdin.read()
