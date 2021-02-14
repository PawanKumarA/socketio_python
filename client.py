from socketIO_client import SocketIO, LoggingNamespace
import logging
logging.getLogger('socketIO-client').setLevel(logging.INFO)
logging.basicConfig()

print("1")
# socketIO = SocketIO('localhost', 8080, LoggingNamespace, params={'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Mzc2NjYzMTMxNTksInVzZXIiOnsiaWQiOjEwLCJlbWFpbCI6ImFkbWluQGFsaW5lLmNvbSIsIm5hbWUiOiJBbGluZWFkbWluIn19.D_bIDl1uJcdTqxwFCGnmf_q1J7zYA-iNKiJ7c5MkMoI'})
socketIO = SocketIO('127.0.0.1', 5000, LoggingNamespace ,resource='socket')
print("connected:",socketIO.connected)

print("2")

socketIO.emit('connect')
socketIO.wait(seconds=1)
print("3")
#logging.getLogger('socketIO-client').info("\n\n\n ************************************************* \n\n\n ")
socketIO.emit('disconnect')
socketIO.wait(seconds=1)
#logging.getLogger('socketIO-client').info("\n\n\n ************************************************* \n\n\n ")
print("4")
