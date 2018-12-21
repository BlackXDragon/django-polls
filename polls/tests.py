from django.test import TestCase

import datetime
from django.utils import timezone
from .models import Question

class QuestionMethodTests(TestCase):
	
	def test_was_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		futQ = Question(pub_date=time)
		self.assertIs(futQ.recent(), False)
	
	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days=30)
		oldQ = Question(pub_date=time)
		self.assertIs(oldQ.recent(), False)
	
	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours=1)
		recQ = Question(pub_date=time)
		self.assertIs(recQ.recent(), True)
	
	def create_question(qText,days):
		time = timezone.now() + datetime.timedelta(days=days)
		return Question.objects.create(qText,time)

class QuestionViewTests(TestCase):
	def test_index_view_with_question(self):
		response = self.client.get(reverse('polls:index'))
		
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available")
		self.assertQuertsetEqual(response.context['qList'],[])
	
	def test_index_view_with_a_past_question(self):
		create_question(qText="Past Q", days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuertsetEqual(response.context['qList'],['<Question: Past question>'])
