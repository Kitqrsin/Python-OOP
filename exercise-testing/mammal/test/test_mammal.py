from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("test_subject", "test_subject_type", "test_subject_sound")

    def test_correct_init(self):
        self.assertEqual("test_subject", self.mammal.name)
        self.assertEqual("test_subject_type", self.mammal.type)
        self.assertEqual("test_subject_sound", self.mammal.sound)

    def test_if_make_sound_gives_the_correct_sound_for_the_current_mammal(self):
        expected_result = "test_subject makes test_subject_sound"
        self.assertEqual(expected_result, self.mammal.make_sound())

    def test_if_get_kingdom_returns_the_correct_kingdom_of_the_mammal(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_returns_the_correct_string_message(self):
        expected_result = "test_subject is of type test_subject_type"
        self.assertEqual(expected_result, self.mammal.info())


if __name__ == '__main__':
    main()