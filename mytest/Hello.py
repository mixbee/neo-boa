from boa.interop.Neo.Runtime import Log, Notify

def Main(operation, args):
    if operation == 'Hello':
        msg = args[0]
        return Hello(msg)

    return False


def Hello(msg):
    Log(msg)
    Notify(msg)
    return True