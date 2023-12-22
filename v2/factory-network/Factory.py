from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass
class Network(ABC):

    @abstractmethod
    def my_type(self):
        print("abstract!")

class TCP(Network):

    def my_type(self):
        print("tcp!")

class FTP(Network):

    def my_type(self):
        print("ftp!")

class UDP(Network):

    def my_type(self):
        print("udp!")

class NetworkExists(Exception):

    
    def __init__(self, network_type, message="Cannot create network object"):
        self.network_type = network_type
        self.message = message
        super().__init__(f"{message}: {network_type}")

@dataclass
class NetworkFactory:

    networks: dict = field(default_factory=dict)

    def create_network(self, net: str) -> Network:
        network = self.networks.get(net)
        if network is None:
            raise NetworkExists(net)
        return network()

    def learn_network(self, net: str, network: Network) -> bool:
        holder = self.networks.get(net)
        if holder:
            return False
        self.networks[net] = network
        return True

factory = NetworkFactory()

factory.learn_network("udp", UDP)
factory.learn_network("ftp", FTP)

a = factory.create_network("tcp")
print(a)
a.my_type()
