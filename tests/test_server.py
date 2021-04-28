import unittest


class TestServerInterface(unittest.IsolatedAsyncioTestCase):
    '''
    Dummy test for CircleCI
    (agreed with the team that the testing for gRPC will be done later)
    '''
    def test_probando(self):
        self.assertEqual(1, 1)
