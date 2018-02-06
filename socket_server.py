import socket
from static_functions import make_header, add_content_type_to_header

STATIC_FOLDER = 'static'
REQUESTS_METHODS = {'GET': 'GET', 'POST': 'POST'}


class SocketServer:
    listen_to_connection = True

    def __init__(self, host, port):
        self.static_files = STATIC_FOLDER
        self.socket = ''
        self.host = host
        self.port = port

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print('Start Server On', self.host, ':', self.port)
            self.socket.bind((self.host, self.port))

        except self.socket.error:
            print('Port ', self.port, ' is Busy\n')
            self.listen_to_connection = False
            self.socket.close()

        self.connect()

    def connect(self):

        while self.listen_to_connection:
            self.socket.listen(10)
            connection, address = self.socket.accept()
            data = connection.recv(1024)
            decoded_data = bytes.decode(data)

            request_method = decoded_data.split(' ')[0]

            if request_method == REQUESTS_METHODS['GET']:

                print('get method')

                requested_file = decoded_data.split(' ')
                requested_file = requested_file[1]

                if requested_file == '/':
                    requested_file = '/index.html'

                requested_file = self.static_files + requested_file

                try:
                    print('file name : ', requested_file)
                    file_handler = open(requested_file, 'rb')
                    res_content = file_handler.read()
                    file_handler.close()

                    res_headers = make_header('OK')
                    content_type = add_content_type_to_header(requested_file.split('.')[1])
                    res_headers += content_type
                except Exception:
                    res_headers = make_header('Not Found')
                    res_headers += add_content_type_to_header('html')
                    file_handler = open(self.static_files + '/404.html', 'rb')
                    res_content = file_handler.read()
                    file_handler.close()

                server_response = res_headers.encode()
                server_response += res_content
                connection.send(server_response)
                connection.close()

            elif request_method == REQUESTS_METHODS['POST']:

                requested_file = decoded_data.split(' ')
                requested_file = requested_file[1]

                if requested_file == '/':
                    requested_file = '/index.html'

                requested_file = self.static_files + requested_file

                try:
                    print('file name : ', requested_file)
                    file_handler = open(requested_file, 'rb')
                    res_content = file_handler.read()
                    file_handler.close()

                    res_headers = make_header('OK')
                    content_type = add_content_type_to_header(requested_file.split('.')[1])
                    res_headers += content_type

                except Exception:
                    res_headers = make_header('Not Found')
                    res_headers += add_content_type_to_header('html')
                    file_handler = open(self.static_files + '/404.html', 'rb')
                    res_content = file_handler.read()
                    file_handler.close()

                server_response = res_headers.encode()
                server_response += res_content
                connection.send(server_response)
                connection.close()

            else:
                print(request_method)
