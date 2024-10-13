from django.test import TestCase
from blog.models import Post, Profile
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):

    def setUp(self):
        User.objects.create(username="testUser",
                            password='C0mpl1cat3dPa$$w0rd')
        Profile.objects.create(user=User.objects.get(username="testUser"),
                              website="testWebsite", 
                              bio="testBio")

    def test_auth_username(self):
        testUser = User.objects.get(username="testUser")
        self.assertEqual(testUser.get_username(), "testUser")

    def test_auth_username_notEqual(self):
        testUser = User.objects.get(username="testUser")
        self.assertNotEqual(testUser.get_username(), "notTestUser")
    
    def test_profile_user(self):
        testUser = Profile.objects.get(id="1")
        self.assertEqual(testUser.__str__(), "testUser")

    def test_profile_user_notEqual(self):
        testUser = Profile.objects.get(id="1")
        self.assertNotEqual(testUser.__str__(), "notTestUser")

    def test_profile_bio(self):
        testUser = Profile.objects.get(id="1")
        bio = str(testUser.bio)
        self.assertEqual(bio, "testBio")

    def test_profile_bio_notEqual(self):
        testUser = Profile.objects.get(id="1")
        bio = str(testUser.bio)
        self.assertNotEqual(bio, "notTestBio")

    def test_profile_website(self):
        testUser = Profile.objects.get(id="1")
        website = str(testUser.website)
        self.assertEqual(website, "testWebsite")

    def test_profile_website_notEqual(self):
        testUser = Profile.objects.get(id="1")
        website = str(testUser.website)
        self.assertNotEqual(website, "notTestWebsite")


        