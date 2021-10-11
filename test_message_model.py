"""Message model test"""

# run these tests like:
#
# python -m unittest test_message_model.py

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
    """Test views for messages"""
    
    
    def setUp(self):
        User.query.delete()
        Message.query.delete()
        Follows.query.delete()
        Likes.query.delete()
        
        self.client = app.test_client()
        
    def tearDown(self):
        # db.session.remove()
        # db.drop_all()
        db.session.rollback()


    def test_message_model(self):
        """Test basic message model workings"""
        # User should have at least message
        self.assertEqual((self.user.messages), 1)
        self.assertEqual(Message.query.count(), 1)

        self.assertEqual(self.message.text, "lorum ipsum")
        self.assertEqual(self.message.user_id, self.user.id)
        self.assertEqual(self.message.user, self.user)
    #     db.session.commit()
        
