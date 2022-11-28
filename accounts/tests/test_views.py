from django.test import TestCase
import accounts.views

class SendLoginEmailViewTest(TestCase):
    '''тест представления, которое отправляет сообщение в систему'''

    def test_redirects_to_home_page(self):
        '''тест: переадресуется на домашнюю страницу'''
        response = self.client.post('/accounts/send_login_email', data={
            'email': 'user@example.com'
        })
        self.assertRedirects(response, '/')

    def test_sends_mail_to_address_from_post(self):
        '''тест: отправляется сообщение на адрес из метода post'''
        self.send_mail_called = False

        def fake_send_mail(subject, body, from_email, to_list):
            '''поддельная функция send_mail'''
            self.send_mail_called = True
            self.subject = subject
            self.body = body
            self.from_email = from_email
            self.to_list = to_list

        accounts.views.send_mail = fake_send_mail

        self.client.post('/accounts/send_login_email', data={
            'email': 'user@example.com'
        })

        self.assertTrue(self.send_mail_called)
        self.assertEqual(self.subject, 'Your login link for Superlists')
        self.assertEqual(self.from_email, 'noreply@superlists')
        self.assertEqual(self.to_list, ['user@example.com'])