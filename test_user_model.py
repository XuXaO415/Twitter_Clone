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
        # db.session.commit()
        

        self.client = app.test_client()
        
        self.user = user
        self.user1 = user1
        self.user2 = user2
        self.user3 = user3
        
        db.session.add_all([user, user1, user2, user3])
        # db.session.add(user)
        # db.session.add(user1)
        # db.session.add(user2)
        # db.session(user3)
        db.session.commit()
        
        
    def tearDown(self):
        # db.session.remove()
        # db.drop_all()
        db.session.rollback()
        
        
    def test_user_model(self):
        """Does basic model work?"""

        # User should have no messages & no followers
        self.assertEqual(len(self.user.messages), 0)
        self.assertEqual(len(self.user1.messages), 0)
        self.assertEqual(len(self.user2.messages), 0)
        self.assertEqual(len(self.user3.messages), 0)
        
        self.assertEqual(len(self.user.followers), 0)
        self.assertEqual(len(self.user1.followers), 0)
        self.assertEqual(len(self.user2.followers), 0)
        self.assertEqual(len(self.user3.followers), 0)
        
        # self.assertEqual(len(self.user.following), 0)
        # self.assertEqual(len(self.user1.following), 0)
        # self.assertEqual(len(self.user2.following), 0)
        # self.assertEqual(len(self.user3.following), 0)
        
        # self.assertEqual(len(self.user.is_following), 0)
        # self.assertEqual(len(self.user1.is_following), 0)
        # self.assertEqual(len(self.user2.is_following), 0)
        # self.assertEqual(len(self.user3.is_following), 0)
    
    def test_repr(self):
        self.assertEqual(repr(self.user),
        # f"<User #{self.user.id}: {self.user.username}, {self.user.email}>")
        f"<User #{self.user.id}: testuser, test@test.com>")
        
    # def test_is_following(self):
    #     """Test detects whether both user1 is 
    #     following/not following user 2
    #     """
        
        # self.user1.following.append(self.user2)
        # db.session.commit()
        
        # self.user1.following.append(self.user2)
        
        # self.assertTrue(self.user1.is_following(self.user2))
        # self.assertFalse(self.user2.is_following(self.user1))

   
