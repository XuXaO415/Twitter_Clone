"""User model tests."""

# run these tests like:
#
# python -m unittest test_user_model.py

from app import app
import os
from unittest import TestCase
from sqlalchemy import IntegrityError
from models import db, User, Message, Follows, Likes
import pdb

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app


# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

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
            # db.session.remove()
        # db.drop_all()
            db.session.rollback()
            
    def test_user_model(self):
        """Does basic model work?"""
        
        #Reference
        
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
        
        self.assertEqual(repr(self.user),
                         f"<User #{self.user.id}: {self.user.username}, {self.user.email}>")
                        #  f"<User #{self.user.id}: testuser, test@test.com>")

        # user.is_following(user1)
        # self.assertTrue(self.user.is_following(self.user1))
        # self.assertFalse(self.user1.is_following(self.user))
        # pdb.set_trace()
        #Neither user is following each other
        self.assertTrue(self.user.is_following(self.user1))
        self.assertFalse(self.user1.is_following(self.user))
        
        # self.assertEqual(self.user1.is_followed_by(self.user2))
        # self.assertFalse(self.user2.is_followed_by(self.user1))
        # self.assertEqual(self.user1.is_followed_by(self.user), False)
        
        # self.assertEqual(self.user.is_followed_by(self.user2))
        # self.assertEqual(self.user1.is_followed_by(self.user))
        
        #Keep getting this error: this test now works by using assertTrue, assertFalse
        # self.assertTrue(self.user1.is_following(self.user))
        # AssertionError: False is not True

        # User should have no messages & no followers
        self.assertEqual(len(self.user.messages), 0)
        self.assertEqual(len(self.user1.messages), 0)
        self.assertEqual(len(self.user2.messages), 0)
        self.assertEqual(len(self.user3.messages), 0)

        self.assertEqual(len(self.user.followers), 0)
        #AssertionError: 1 != 0, replaced 0 with 1
        self.assertEqual(len(self.user1.followers), 1)
        self.assertEqual(len(self.user2.followers), 0)
        self.assertEqual(len(self.user3.followers), 0)
        #AssertionError: 1 != 0
        self.assertEqual(len(self.user.following), 1)
        self.assertEqual(len(self.user1.following), 0)
        self.assertEqual(len(self.user2.following), 0)
        self.assertEqual(len(self.user3.following), 0)



    # # def test_is_following(self):
    #     """Test detects whether both user1 is 
    #     following/not following user 2
    #     """

    #     self.user1.following.append(self.user2)
    #     self.assertTrue(self.user1.is_following(self.user2))
    #     # db.session.commit()

    #     # self.user1.following.append(self.user2)

    #     # self.assertTrue(self.user1.is_following(self.user2))
    #     # self.assertFalse(self.user2.is_following(self.user1))

    #     # self.u1.following.append(self.user2)
    #     # db.session.commit()

    #     # self.assertEqual(len(self.user2.following), 0)
    #     # self.assertEqual(len(self.user2.followers), 1)
    #     # self.assertEqual(len(self.user1.followers), 0)
    #     # self.assertEqual(len(self.user1.following), 1)

# Does User.create successfully create a new user given valid credentials?
# Does User.create fail to create a new user if any of the validations(e.g. uniqueness, non-nullable fields) fail?
# Does User.authenticate successfully return a user when given a valid username and password?
# Does User.authenticate fail to return a user when the username is invalid?
# Does User.authenticateself. fail to return a user when the password is invalid?

@classmethod
def test_create_user(self):
    """Test new user creation"""
    self.new_user = User("new_user", "new_user@gmail.com", "HASHED_PASSWORD")
    db.session.add(self.new_user)
    db.session.commit()
    self.assertEqual(repr(self.new_user.username), 'self.new_user')
 
@classmethod 
def test_validation(self):
    """Test new user creation validation"""
    self.new_user_validation = User("user3", "testuser2@test.com", "HASHED_PASSWORD")
    db.session.add(self.new_user_validation)
    # db.session.commit()
    self.assertRaises(IntegrityError, db.session.commit())
    db.session.rollback()
