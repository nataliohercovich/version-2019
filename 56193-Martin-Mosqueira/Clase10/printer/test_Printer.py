import unittest
from printer  import Printer

class Test_Printer(unittest.TestCase):
    def test_printer_available(self):
        result=Printer().printer_available()
        self.assertTrue(result)

    def test_print_job(self):
        result=Printer()
        result.add_print_job('hoja')
        result.print_job()
        self.assertFalse(result.error_flag)

    def test_print_job_error(self):
        result=Printer()
        result.print_job()
        self.assertTrue(result.error_flag)
        self.assertEqual(result.error_description, "nothing to print")

    def test_reset_printer(self):
        result=Printer()
        result.reset_printer()
        self.assertFalse(result.printing)
        self.assertFalse(result.error_flag)
        self.assertEqual(result.error_description, "")


if __name__ == '__main__':
   unittest.main()