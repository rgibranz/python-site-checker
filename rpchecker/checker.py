# checker.py

from http.client import HTTPConnection
from urllib.parse import urlparse


def site_is_online(url, timeout=2):

    # return true if the target url is online
    # raise an exception otherwise

    error = Exception("Error HEHE")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request('HEAD', '/')
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error
