def make_header(status_code):
    
    header = ''
    if status_code == 'OK':
        header = 'HTTP/1.1 200 OK\n'
    elif status_code == 'Not Found':
        header = 'HTTP/1.1 404 Not Found\n'
    header += 'Server: INTERNET-ENGINEERING\n'
    header += 'Connection: close\n\n'

    return header


def add_content_type_to_header(file_type):
    if file_type == 'txt':
        return 'Content-Type: text/plain\n\n'
    elif file_type == 'pdf':
        return 'Content-Type: application/pdf\nContent-Disposition: inline; filename="filename.pdf"\n\n'
    elif file_type == 'jpg':
        return 'Content-Type: image/jpeg\n\n'

    return ''
