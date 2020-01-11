from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime

# Create your tests here.
class QuestionModelTest(TestCase):
    def test_recent_published_with_future(self):
        future = Question(pub_date = timezone.now() + datetime.timedelta(days=2))
        self.assertIs(future.was_published_recently(), False)