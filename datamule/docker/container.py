import random
import string

import docker


class DataMuleDocker:
    def __init__(self, db='postgres', username=None, password=None):
        try:
            # todo replace text file with YAML
            secret = open('secret.txt', 'r')
            userpw = secret.readline().rstrip().split()
            secret.close()

            config = {
                'username': userpw[0],
                'password': userpw[1]
            }

        except FileNotFoundError:
            config = None

        self.client = docker.from_env()
        self.db = db

        if config:
            self.username = config['username']
            self.password = config['password']

        else:
            # todo make dynamic user names
            self.username = 'postgres' if not username else username
            self.password = DataMuleDocker.random_string() if not password else password
            secret = open('secret.txt', 'w')
            secret.writelines(self.username + ' ' + self.password + '\n')
            secret.close()

    def run(self):
        try:
            container = self.client.containers.get('data-mule-' + self.db)
            container.start()

        except docker.errors.NotFound:
            try:
                self.client.images.get(self.db + ':latest')

            except docker.errors.NotFound:
                self.client.images.pull(self.db + ':latest')

            self.client.containers.run(
                image=self.db + ':latest',
                name='data-mule-' + self.db,
                detach=True,

                environment={
                    self.db.upper() + '_PASSWORD': self.password
                },

                ports={
                    '5432/tcp': 5432
                }
            )

        return {
            'username': self.username,
            'password': self.password
        }

    @staticmethod
    def random_string(n=15):
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(n))
