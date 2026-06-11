clients = input("Na ile osób chciałby Pan zarezerwować stolik? ")
clients = int(clients)

if clients > 8:
    print("\nProszę zaczekać na stolik.")
else:
    print("\nStolik jest już gotowy.")