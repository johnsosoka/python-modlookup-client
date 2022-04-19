from base_client import BaseClient


class ModLookupClient(BaseClient):

    def get_user(self, user: str, limit: int = 100, cursor: str = ''):
        path = '/user-v3/{username}'.format(username=user)
        return self.get_request(path)

    def get_user_total(self, user: str):
        path = '/user-totals/{username}'.format(username=user)
        return self.get_request(path)

    def get_top(self):
        path = '/top'
        return self.get_request(path)

    def get_stats(self):
        path = '/stats'
        return self.get_request(path)
