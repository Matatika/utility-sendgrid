"""Unittest module for sendgrid utility"""

import unittest
from pathlib import Path
from click.testing import CliRunner
from sendgrid_cli.cli.commands.root import sendgrid_cli
from sendgrid_cli.utils import split_into_list


class TestSendgrid(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.single_attachment = "path/to/file"
        self.multiple_attachment = "path/to/file,path/to/file2"
        self.single_to_address = "test@test.com"
        self.multiple_to_addresses = "test@test.com,example@example.com"

    def tearDown(self):
        pass

    def test_email_no_args(self):
        result = self.runner.invoke(sendgrid_cli, catch_exceptions=False)
        self.assertIn("Error", result.output)
        self.assertIs(result.exit_code, 2)

    def test_split_single_attachment(self):
        result = split_into_list(self.single_attachment)
        self.assertTrue(isinstance(result, list))
        self.assertTrue(len(result), 1)
        self.assertEqual(result[0], self.single_attachment)

    def test_split_multiple_attachments(self):
        result = split_into_list(self.multiple_attachment)
        self.assertTrue(isinstance(result, list))
        self.assertTrue(len(result), 2)
        self.assertEqual(result[0], "path/to/file")
        self.assertEqual(result[1], "path/to/file2")

    def test_split_single_to_email_addresses(self):
        result = split_into_list(self.single_to_address)
        self.assertTrue(isinstance(result, list))
        self.assertTrue(len(result), 1)
        self.assertEqual(result[0], self.single_to_address)

    def test_split_multiple_to_email_addresses(self):
        result = split_into_list(self.multiple_to_addresses)
        self.assertTrue(isinstance(result, list))
        self.assertTrue(len(result), 2)
        self.assertEqual(result[0], "test@test.com")
        self.assertEqual(result[1], "example@example.com")
