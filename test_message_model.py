"""Message model test"""

# run these tests like:
#
# python -m unittest test_message_model.py

import os
from unittest import TestCase
from models import db, User, Message, Follows, Likes
import datetime

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

# Now we can import app

from app import app


# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()

class UserModelTestCase(TestCase):
    """Test views for messages"""


    def setUp(self):
        User.query.delete()
        Message.query.delete()
        Follows.query.delete()
        Likes.query.delete()

        self.client = app.test_client()


        user1 = User(
            email="user1@test.com",
            username="testuser1",
            password="hashed_pwd",
            id=1,
        )
        
        message = Message(
            text = "lorum ipsum",
            id = 1,
            user_id = 1,
            # user_id = self.user.id
        )
        
        db.session.add_all([user1, message])
        db.session.commit()
        
        self.user1 = user1
        self.message = message

    def tearDown(self):
        db.session.rollback()


    def test_message_model(self):
        """Test basic message model workings"""
        # User should have at least one message
        self.assertTrue((self.message), 1)
        self.assertEqual(Message.query.count(), 1)

        self.assertEqual(self.message.text, "lorum ipsum")
        self.assertEqual(self.message.id, 1)
        self.assertEqual(self.message.user.id, 1)
        self.assertEqual(self.user1.email, "user1@test.com")
        self.assertEqual(self.user1.username, "testuser1")
        
