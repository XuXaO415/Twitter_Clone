"""User model tests."""

# run these tests like:
#
# python -m unittest test_user_model.py


import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError
from models import db, User, Message, Follows, Likes
import pdb

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"
# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data
from app import app

db.create_all()

class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()
        Likes.query.delete()

        self.client = app.test_client()

    def tearDown(self):
        db.session.rollback()

    def test_user_model(self):
        """Does basic model work?"""

        # Reference

        # following = db.relationship(
        #     "User",
        #     secondary="follows",
        #     overlaps="followers",
        #     primaryjoin=(Follows.user_following_id == id),
        #     secondaryjoin=(Follows.user_being_followed_id == id)
        # )

        # def is_followed_by(self, other_user):
        #     """Is this user followed by `other_user`?"""
        # found_user_list = [user for user in self.followers if user == other_user]
        # return len(found_user_list) == 1

        #  def is_following(self, other_user):
        #     """Is this user following `other_use`?"""
        # found_user_list = [user for user in self.following if user == other_user]
        # return len(found_user_list) == 1

        user = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        user1 = User(
            email="user1@test.com",
            username="testuser1",
            password="HASHED_PASSWORD"
        )

        user2 = User(
            email="user2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD"
        )

        user3 = User(
            email="user3@test.com",
            username="testuser3",
            password="HASHED_PASSWORD"
        )

        self.user = user
        self.user1 = user1
        self.user2 = user2
        self.user3 = user3

        db.session.add_all([user, user1, user2, user3])
        db.session.commit()

        follow = Follows(
            user_following_id=user.id,
            user_being_followed_id=user1.id
        )

        db.session.add(follow)
        db.session.commit()

        self.assertEqual(repr(self.user), f"<User #{self.user.id}: {self.user.username}, {self.user.email}>")
        #  f"<User #{self.user.id}: testuser, test@test.com>")

        # user.is_following(user1)
        # self.assertTrue(self.user.is_following(self.user1))
        # self.assertFalse(self.user1.is_following(self.user))
        # Neither user is following each other
        self.assertTrue(self.user.is_following(self.user1))
        self.assertFalse(self.user1.is_following(self.user))
        
        # self.assertNotEqual("self.user2.is_followed_by", "self.user3")
        self.assertNotEqual(self.user1.is_followed_by, (self.user))
    

        # self.user1.following.append(self.user2)

        # self.assertTrue(self.user1.is_following(self.user2))
        # self.assertFalse(self.user2.is_following(self.user1))

        # self.u1.following.append(self.user2)
        # db.session.commit()

        # self.assertEqual(len(self.user2.following), 0)
        # self.assertEqual(len(self.user2.followers), 1)
        # self.assertEqual(len(self.user1.followers), 0)
        # self.assertEqual(len(self.user1.following), 1)


    @classmethod
    def test_create_user(self):
        self.new_user = User.signup("self.new_user", "new_user@test.com", "HASHED_PASSWORD", "img_url=default")
        db.session.add(self.new_user)
        db.session.commit()
        self.assertTrue(self.new_user.username, "new_user")
        
    def test_user_authentication(self):
        self.user_auth = User.authenticate("self.user3", "HASHED_PASSWORD")
        # db.session.add(self.user_auth)
        # db.session.commit()
        self.assertTrue("self.user_auth", "self.user3")
        db.session.rollback()
    
    def test_new_user_fail(self):
        self.user_fail = User.signup("randomUser", "anotherNewUser@test.com", "HASHED_PASSWORD", "img_url=None")
        # db.session.add(self.user_fail)
        # db.session.commit()
        self.assertNotEqual(self.user_fail.username, "randomUser.username")
        db.session.rollback()
        
    def test_user_fail(self):
        self.new_user_fail = User.authenticate("self.new_user_fail", "self.user_fail@test.com")
        self.assertNotEqual("self.new_user_fail", "self.user", "self.some_other_user")
        db.session.rollback()
        # db.session.commit()
