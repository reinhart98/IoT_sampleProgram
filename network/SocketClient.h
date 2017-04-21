class SocketClient{
private:
	int	socketfd;
	struct 	sockaddr_in	serverAddress;
	struct 	hostent 	*server;
	std::string 	serverName;
	int 		portNumber;
	bool 		inConnected;
public:
	SocketClient(std::string serverName,int portNumber);
	virtual int connectedToServer();
	virtual int disconnectedFromServer();
	virtual int send(std::stringmessage);
	virtual std::string receive(int,size);
	bool isClientConnected() {return this->isConnected;}
	virtual ~SocketClient();

};
