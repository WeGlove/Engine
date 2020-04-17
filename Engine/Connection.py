import _thread

class Connection:
    """
    The connection handling ocmmunication between a Server and client thread
    """

    def __init__(self):
        self.server_lock = _thread.allocate_lock()
        self.client_lock = _thread.allocate_lock()

        self.to_server = []
        self.to_clients = []

    def push_to_server(self, events):
        with self.server_lock:
            self.to_server.extend(events)

    def push_to_clients(self, events):
        with self.client_lock:
            self.to_clients.extend(events)

    def pop_server(self):
        with self.server_lock:
            temp = self.to_server
            self.to_server = []
        return temp

    def pop_clients(self):
        with self.client_lock:
            temp = self.to_clients
            self.to_clients = []
        return temp

    def clients_have_events(self):
        with self.client_lock:
            return len(self.to_clients) > 0

    def server_has_events(self):
        with self.server_lock:
            return len(self.to_server) > 0

    def server_wait_for_msg(self):
        while not self.server_has_events():
            pass

    def client_wait_for_msg(self):
        while not self.clients_have_events():
            pass
