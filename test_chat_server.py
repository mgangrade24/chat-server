import unittest
import json
from chat_server import app

class ChatServerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_send_message(self):
        response = self.app.post('/send', json={'from_user': 'user_1', 'to_user': 'user_2', 'message': 'Hello, user_2!'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['status'], 'Message sent')

    def test_get_unread_messages(self):
        self.app.post('/send', json={'from_user': 'user_1', 'to_user': 'user_2', 'message': 'Hello, user_2!'})

        response = self.app.get('/messages?user=user_2')
        self.assertEqual(response.status_code, 200)
        messages = json.loads(response.data)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]['from_user'], 'user_1')
        self.assertEqual(messages[0]['message'], 'Hello, user_2!')
        self.assertTrue(messages[0]['read'])

if __name__ == '__main__':
    unittest.main()
