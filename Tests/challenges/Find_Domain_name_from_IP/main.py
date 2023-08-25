import socket

class FindDomain:
    def __init__(self, dns_path: str) -> None:
        self.__dns_path = dns_path
        
    @property
    def dns_path(self) -> str:
        return self.__dns_path
    
    def get_domain(self) -> str:
        domain: str = socket.gethostbyaddr(str(self.dns_path))[0]
        return domain
    