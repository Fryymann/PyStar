import socket
import threading

host = '72.110.98.3'
port = 8765

nickname = input("Choose your nickname: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            elif message == 'DISCONNECT':
                client.close()
                break
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        inp = input('')
        if inp == 'quit':
            client.close()
            break
        message = '{}: {}'.format(nickname, inp)
        client.send(message.encode('ascii'))


if __name__ == '__main__':
    # receiving multiple messages
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    write_thread = threading.Thread(target=write)
    write_thread.start()

