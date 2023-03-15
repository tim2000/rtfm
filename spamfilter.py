import time

DEFAULT_TIMEOUT_SEC = 2

class SpamFilter:
    def __init__(self, filter_time_sec = DEFAULT_TIMEOUT_SEC, excluded_groups = ["Admin"]) -> None:
        self.clients = dict()
        self.filter_time_sec = filter_time_sec
        self.excluded_groups = excluded_groups
    

    def is_authorized(self, client_addr):
        if client_addr not in self.clients:
            self.clients[client_addr] = {'addr': client_addr, 'timer': time.time()}
            return True
        
        last_time = self.clients[client_addr]['timer']
        diff = time.time() - last_time
        self.clients[client_addr]['timer'] = time.time()
        
        if diff < self.filter_time_sec:
            print(str(diff))
            return False

        return True
    

    def should_apply_filter(self, group):
        if group in self.excluded_groups:
            return False
        
        return True
