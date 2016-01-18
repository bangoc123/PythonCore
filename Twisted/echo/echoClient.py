from twisted.internet import reactor,protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        message = input("Type an message: ")
        self.transport.write(str.encode(message))
        if message == "quit":
            self.transport.loseConnection()

    def dataReceived(self, data):
        print("Server reply:", str(data, 'utf-8'))
        return self.connectionMade()

class EchoClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Failed to connect")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Lost connection")
        reactor.stop()


reactor.connectTCP("localhost", 8000, EchoClientFactory())

reactor.run()