"""User test model"""

# run these tests like:
#
#  python -m unittest test_message_model.py

from app import app
import os
from unittest import TestCase
from models import db, User, Message, Follows, Likes

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

# Now we can import app

from app import app


# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()

class UserModelTestCase(TestCase):
    def setUp(self):
        User.query.delete()
        Message.query.delete()
        Follows.query.delete()
    # Test User 0 
        test_user0 = User(email='test_email@test.com', 
                            username='webbmark', 
                            password='HASHED_PASSWORD')
        db.session.add(test_user0)
        db.session.commit()

        self.test_user0 = test_user0

        test_message0 = Message(text='test message',
                                user_id=test_user0.id
                                )
        
        db.session.add(test_message0)
        db.session.commit()

        self.test_message0 = test_message0

        self.client = app.test_client()
