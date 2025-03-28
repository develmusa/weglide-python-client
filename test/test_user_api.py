# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from weglide_client.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_create_xcsoar_token_v1_user_xcsoar_token_post(self) -> None:
        """Test case for create_xcsoar_token_v1_user_xcsoar_token_post

        Create Xcsoar Token
        """
        pass

    def test_delete_me_v1_user_me_delete_post(self) -> None:
        """Test case for delete_me_v1_user_me_delete_post

        Delete Me
        """
        pass

    def test_delete_profile_pic_v1_user_image_delete(self) -> None:
        """Test case for delete_profile_pic_v1_user_image_delete

        Delete Profile Pic
        """
        pass

    def test_get_me_active_subscription_v1_user_me_copilot_subscription_get(self) -> None:
        """Test case for get_me_active_subscription_v1_user_me_copilot_subscription_get

        Get Me Active Subscription
        """
        pass

    def test_get_me_v1_user_me_get(self) -> None:
        """Test case for get_me_v1_user_me_get

        Get Me
        """
        pass

    def test_get_user_v1_user_user_id_get(self) -> None:
        """Test case for get_user_v1_user_user_id_get

        Get User
        """
        pass

    def test_get_users_v1_user_get(self) -> None:
        """Test case for get_users_v1_user_get

        Get Users
        """
        pass

    def test_latest_aircraft_v1_user_aircraft_user_id_get(self) -> None:
        """Test case for latest_aircraft_v1_user_aircraft_user_id_get

        Latest Aircraft
        """
        pass

    def test_latest_copilot_v1_user_copilot_user_id_get(self) -> None:
        """Test case for latest_copilot_v1_user_copilot_user_id_get

        Latest Copilot
        """
        pass

    def test_patch_me_v1_user_me_patch(self) -> None:
        """Test case for patch_me_v1_user_me_patch

        Patch Me
        """
        pass

    def test_post_profile_pic_v1_user_image_post(self) -> None:
        """Test case for post_profile_pic_v1_user_image_post

        Post Profile Pic
        """
        pass

    def test_post_user_v1_user_post(self) -> None:
        """Test case for post_user_v1_user_post

        Post User
        """
        pass


if __name__ == '__main__':
    unittest.main()
