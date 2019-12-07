

class Logger:
    def __init__(self, socketio_):
        #self.log_socket = socket_send_log
        self.socketio_ = socketio_
        self.outputs = [self.log_print]#, socketio_)#self.log_print, self.log_socket)


    def write(self, msg):
        msg = f'\r\nINFO: {msg}\r\n'
        [write_(msg) for write_ in self.outputs]

    def error(self, msg):
        msg = f'\r\nERROR: {msg}\r\n'
        [write(msg) for write in self.outputs]

    def log_socket(self, msg):
        self.socketio_.emit('log', msg)

    def log_print(self, msg):
        print(f'{msg}')