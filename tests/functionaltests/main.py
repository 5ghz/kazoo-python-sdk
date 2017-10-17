#!/usr/bin/env python
import kazoo
import unittest
import pprint
import random


class FunctionalTest(unittest.TestCase):
    def auth(self, username=None, password=None, account_name=None, base_url=None):
        if username is not None:
            self.username = username
        else:
            self.username = 'superadmin'

        if password is not None:
            self.password = password
        else:
            self.password = 'a1s2d3QWE123'

        if account_name is not None:
            self.account_name = account_name
        else:
            self.account_name = 'superadmin'

        if base_url is not None:
            self.base_url = base_url
        else:
            self.base_url = 'http://tvnow.io:8000/v2'

        client = kazoo.Client(username=self.username, password=self.password, account_name=self.account_name,
                              base_url=self.base_url)
        client.authenticate()
        return client

    def testAuth(self):
        self.client = self.auth()
        self.assertGreater(len(self.client.account_id),0)

class DeviceTest(FunctionalTest):
    def testCreateDevice(self):
        self.client = FunctionalTest.auth(self)
        data={}
        data['name']='SDKTest'+str(random.randint(100,1000))
        self.a_device = self.client.create_device(self.client.account_id,data)
        self.assertGreater(len(self.a_device['data']['id']),0)

if __name__ == '__main__':
    unittest.main()
