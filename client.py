from twisted.internet import reactor
from twisted.conch.client import options
from twisted.conch.client import default, forward
from twisted.conch.ssh import transport
from twisted.conch.ssh.keys import Key
from twisted.python import log

class SSHDemoClientTransport(transport.SSHClientTransport):
    def verifyHostKey(self, hostKey, fingerprint):
        # Verify the server's host key
        # Return True to accept or False to reject
        return True  # Replace with your host key verification logic

    def connectionSecure(self):
        # Connection is secure, start authentication
        self.requestService(SSHUserAuthClient('username', 'password'))  # Replace with your authentication details

class SSHUserAuthClient(userauth.SSHUserAuthClient):
    def getPassword(self):
        # Return the password for authentication
        return self.password

log.startLogging(open("ssh_client.log", "w"))
options.ConchOptions().parseOptions([])
reactor.connectTCP('server_ip', 2222, SSHDemoClientTransport())
reactor.run()
