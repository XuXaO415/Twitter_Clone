"""User model tests."""

# run these tests like:
#
# python -m unittest test_user_model.py


import os
from unittest import TestCase
from models import db, User, Message, Follows, Likes

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()

user = User(
    email="test@test.com",
    username="testuser",
    password="HASHED_PASSWORD"
)

user1 = User(
    email = "user1@test.com",
    username = "testuser1",
    password = "HASHED_PASSWORD"
)

user2 = User(
    email = "user2@test.com",
    username ="testuser2",
    password = "HASHED_PASSWORD"
)

user3 = User(
    email = "user3@test.com",
    username = "testuser3",
    password = "HASHED_PASSWORD"
)



class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()
        Likes.query.delete()

        self.client = app.test_client()
        
        self.user = user
        self.user1 = user1
        self.user2 = user2
        self.user3 = user3
        
        db.session.add_all([user, user1, user2, user3])
        db.session.commit()
        
        
    def tearDown(self):
        db.session.rollback()
        
        
    def test_user_model(self):
        """Does basic model work?"""

        # User should have no messages & no followers
        self.assertEqual(len(self.user.messages), 0)
        self.assertEqual(len(self.user1.messages), 0)
        self.assertEqual(len(self.user2.messages), 0)
        self.assertEqual(len(self.user3.messages), 0)
        self.assertEqual(len(user.followers), 0)
        self.assertEqual(len(user1.followers), 0)
        self.assertEqual(len(user2.followers), 0)
        self.assertEqual(len(user3.followers), 0)
        
        self.assertEqual(str(self.user),
        f"<User #{self.user.id}: {self.user.username}, {self.user.email}>")