import unittest
import password_worker
from hashlib import md5
from password_worker.password_hasher import passwordEqualsHasher, passwordHasher
from setting import SALT

class TestGeneratorPassword(unittest.TestCase):
    """Набор тестов для генератора пароля"""
    def test_len_password(self):
         self.assertEqual(len(password_worker.generatorPassword(len_password=10)), 10) 

    def test_valid_password(self):
        self.assertTrue(password_worker.passwordValidator(password_worker.generatorPassword()))

    
class TestPasswordValidationChecks(unittest.TestCase):
    """Проверка вспомогательных функций при генерации пароля"""

    def test_line_intersections_false(self):
        self.assertFalse(password_worker.checkingMatchingCharInStrings("123ggfte", "00_dsads"))

    def test_line_intersections_true(self):
        self.assertTrue(password_worker.checkingMatchingCharInStrings("123ggfte", "00_dsad12s"))

    def test_validator_password_true(self):
        self.assertTrue(password_worker.passwordValidator("_d)Fa4'#O5"))

    def test_validator_password_too_shot(self):
        self.assertFalse(password_worker.passwordValidator("_d)Fa4'#O5", minimal_len_password=100))

    def test_validator_password_dont_element(self):
        self.assertFalse(password_worker.passwordValidator("aa_oooooooooo"))
        self.assertFalse(password_worker.passwordValidator("1a_oooooooooo"))
        self.assertFalse(password_worker.passwordValidator("1A_OOOOOOOOOO"))
        self.assertFalse(password_worker.passwordValidator("1aAoooooooooo"))


class TestHesherPassword(unittest.TestCase):
    "Проверка функций кеширования и сравнения паролей"

    def test_password_hashr_with_salt(self):
        password_test = '6376hjdfs6@bnvasdnf'
        etalon = md5(password_test.encode() + SALT).hexdigest()  
        self.assertEqual(etalon, passwordHasher(password_test, using_salt=True))

    def test_password_hashr(self):
        password_test = '6376hjdfs6@bnvasdnf'
        etalon = md5(password_test.encode()).hexdigest()  
        self.assertEqual(etalon, passwordHasher(password_test, using_salt=False))
    
    def test_password_equals_hasher_good(self):
        password_test = '6376hjdfs6@bnvasdnf'
        self.assertTrue(passwordEqualsHasher(password=password_test, password_from_db=int(passwordHasher(password_test),16)))

    def test_password_equals_hasher_bed(self):
        password_test = '6376hjdfs6@bnvasdnf'
        self.assertFalse(passwordEqualsHasher(password="password_test", password_from_db=int(passwordHasher(password_test),16)))


