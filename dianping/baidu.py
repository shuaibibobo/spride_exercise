import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
   Java.perform(function () {
    var cls = Java.use("com.dianping.nvnetwork.tunnel2.a");
    cls.isSocketConnected.overload().implementation = function () {
        return false;
    };
});
"""

process = frida.get_usb_device().attach('美团')
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
sys.stdin.read()