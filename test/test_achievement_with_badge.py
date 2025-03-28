# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from weglide_client.models.achievement_with_badge import AchievementWithBadge

class TestAchievementWithBadge(unittest.TestCase):
    """AchievementWithBadge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AchievementWithBadge:
        """Test AchievementWithBadge
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AchievementWithBadge`
        """
        model = AchievementWithBadge()
        if include_optional:
            return AchievementWithBadge(
                id = 56,
                badge_id = '',
                points = 56,
                flight_id = 56,
                value = 1.337,
                user = weglide_client.models.user_with_image_and_copilot.UserWithImageAndCopilot(
                    id = 56, 
                    name = '', 
                    image = '', 
                    badge = True, 
                    copilot_uid = 56, ),
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                badge = weglide_client.models.badge.Badge(
                    id = '', 
                    name = '', 
                    logo = '', 
                    description = weglide_client.models.description.Description(), 
                    points = [
                        56
                        ], 
                    values = [
                        1.337
                        ], )
            )
        else:
            return AchievementWithBadge(
                id = 56,
                badge_id = '',
                points = 56,
                user = weglide_client.models.user_with_image_and_copilot.UserWithImageAndCopilot(
                    id = 56, 
                    name = '', 
                    image = '', 
                    badge = True, 
                    copilot_uid = 56, ),
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                badge = weglide_client.models.badge.Badge(
                    id = '', 
                    name = '', 
                    logo = '', 
                    description = weglide_client.models.description.Description(), 
                    points = [
                        56
                        ], 
                    values = [
                        1.337
                        ], ),
        )
        """

    def testAchievementWithBadge(self):
        """Test AchievementWithBadge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
