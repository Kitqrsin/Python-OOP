from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("some_guy", 1, 100, 1)

    def test_if_init_is_correct(self):
        self.assertEqual("some_guy", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(1, self.hero.damage)

    def test_battle_exception_error_if_you_try_to_fight_yourself(self):
        self.test_enemy = Hero("some_guy", 1, 100, 1)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.test_enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_you_do_not_have_health_to_fight_raise_exception(self):
        self.test_enemy = Hero("some_other_guy", 1, 100, 1)
        self.hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.test_enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_if_enemy_does_not_have_enough_health_raise_exception(self):
        self.test_enemy = Hero("some_other_guy", 1, 0, 1)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.test_enemy)

        self.assertEqual("You cannot fight some_other_guy. He needs to rest", str(ex.exception))

    def test_battle_if_no_exceptions_are_raised_and_hero_wins_battle_decrease_hero_health_and_decrease_enemy_health(self):
        self.test_enemy = Hero("some_other_guy", 2, 100, 2)
        self.hero.level = 2
        self.hero.damage = 50

        expected_hero_health_after_battle = 101
        expected_hero_level_after_battle = 3
        expected_hero_damage_after_battle = 55
        expected_enemy_health_after_battle = 0

        result = self.hero.battle(self.test_enemy)

        self.assertEqual(expected_hero_health_after_battle, self.hero.health)
        self.assertEqual(expected_hero_level_after_battle, self.hero.level)
        self.assertEqual(expected_hero_damage_after_battle, self.hero.damage)
        self.assertEqual(expected_enemy_health_after_battle, self.test_enemy.health)
        self.assertEqual("You win", result)

    def test_battle_if_no_exceptions_are_raised_and_enemy_wins_battle(self):
        self.test_enemy = Hero("some_other_guy", 2, 100, 50)

        expected_hero_health_after_battle = 0
        expected_enemy_level_after_battle = 3
        expected_enemy_health_after_battle = 104
        expected_enemy_damage_after_battle = 55

        result = self.hero.battle(self.test_enemy)
        self.assertEqual(expected_hero_health_after_battle, self.hero.health)
        self.assertEqual(expected_enemy_damage_after_battle, self.test_enemy.damage)
        self.assertEqual(expected_enemy_level_after_battle, self.test_enemy.level)
        self.assertEqual(expected_enemy_health_after_battle, self.test_enemy.health)
        self.assertEqual("You lose", result)

    def test_battle_if_no_exceptions_are_raised_and_battle_ends_in_draw(self):
        self.test_enemy = Hero("some_other_guy", 2, 100, 50)
        self.hero.level = 2
        self.hero.damage = 50

        expected_hero_health_after_battle = 0
        expected_enemy_health_after_battle = 0

        result = self.hero.battle(self.test_enemy)

        self.assertEqual(expected_hero_health_after_battle, self.hero.health)
        self.assertEqual(expected_enemy_health_after_battle, self.test_enemy.health)
        self.assertEqual("Draw", result)

    def test_if__str__method_works_correctly(self):
        expected_result = f"Hero some_guy: 1 lvl\n" \
                          f"Health: 100\n" \
                          f"Damage: 1\n"

        self.assertEqual(expected_result, self.hero.__str__())

if __name__ == '__main__':
    main()
