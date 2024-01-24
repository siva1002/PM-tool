from .test_setup import TestSetup
import pdb


class Testview(TestSetup):
    def test_user_registration1(self):
        res = self.client.post(self.registerurl, data={
                               "username": "siva", "age": 25, "email": "siva@gmail.com", "password": "12345678", "phone": "7423234325", "address": "madurai"})
        self.assertEqual(res.status_code, 201)

    def test_user_registration2(self):
        res = self.client.post(self.registerurl, data={
                               "age": 25, "email": "siva@gmail.com", "password": "12345678", "phone": "7423234325", "address": "madurai"})

        self.assertEqual(res.status_code, 201)
