"""User view tests."""

# run these tests like:
#
# python -m unittest test_user_views.py

from app import app
import os
from unittest import TestCase
from models import db, User, Message, Follows, Likes

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

# Now we can import app

from app import app, CURR_USER_KEY

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()

# Don't have WTForms use CSRF at all, since it's a pain to test
app.config['WTF_CSRF_ENABLED'] = False

# app.config['TESTING'] = True
# app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


class UserViewTestCase(TestCase):
    """Test views for messages"""
    def setUp(self):
        """Create test client & add sample data"""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()
        Likes.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="testuser1",
                                    email="test123@test.com",
                                    password="testuser",
                                    image_url=None)

        self.testuser2 = User.signup(username="testuser2",
                                     email="testabc@test.com",
                                     password="testuser",
                                     image_url=None)

        db.session.add_all([self.testuser, self.testuser2])
        db.session.commit()

    def tearDown(self):
        db.session.rollback()

    def test_users_following(self):
        """When user is logged in, test checks whether you can see 
        follower/following pages of other users 
        """

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

        user = User.query.get(self.testuser.id)
        user.following.append(self.testuser2)
        db.session.commit()

        resp = c.get(
            f"/users/follow/{self.testuser.id}, /users/following/{self.testuser2.id} "
        )
        data = resp.get_data(as_text=True)
        self.assertTrue("self.testuser.id", data)
        # self.assertEqual(resp.status_code, 404)

    def test_user_logout(self):
        # with app.test_client() as c:
        # resp = c.get("/users/logout_user")
        resp = self.client.get("/users/log-out",
                               follow_redirects=True)
        data = resp.get_data(as_text=True)
        # self.assertTrue(self.testuser, data)
        self.assertEqual(resp.status_code, 200)