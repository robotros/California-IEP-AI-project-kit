#!/usr/bin/env python3
"""Unit tests use entirely invented identifiers; no actual education records."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from pii_redact import Redactor

SCRIPT=Path(__file__).with_name('pii_redact.py')

class PIIRedactionTests(unittest.TestCase):
    def test_labeled_identifiers_and_ordinary_goal_date(self):
        text='Student Name: Avery Fiction\nParent: Casey Imaginary\nDOB: 01/02/2017\nStudent ID: 9876543210\nIEP goal date: 10/14/2027\n'
        out=Redactor().text(text)
        for original in ('Avery Fiction','Casey Imaginary','01/02/2017','9876543210'):
            self.assertNotIn(original,out)
        for typ in ('STUDENT_NAME','FAMILY_NAME','DATE_OF_BIRTH','STUDENT_ID'):
            self.assertIn('[[REDACTED: '+typ,out)
        self.assertIn('10/14/2027',out)

    def test_unlabeled_student_id_not_confused_with_phone(self):
        r=Redactor()
        out=r.text('Student ID 1234567890; staff phone: 626-555-0123')
        self.assertIn('[[REDACTED: STUDENT_ID #001]]',out)
        self.assertIn('[[REDACTED: PHONE_NUMBER #001]]',out)

    def test_no_detection_does_not_mean_cleared(self):
        r=Redactor()
        self.assertEqual(r.text('Grade 3 goal: 6/10 correct; due 2027-10-14.'),'Grade 3 goal: 6/10 correct; due 2027-10-14.')
        self.assertEqual(len(r.tokens),0)

    def test_unlabeled_names_with_private_dictionary(self):
        r=Redactor(extra_names=['Avery Fiction'])
        result=r.text('Avery Fiction scored 5/10; Avery Fiction improved.')
        self.assertNotIn('Avery Fiction',result)
        self.assertEqual(result.count('[[REDACTED: PERSON_NAME #001]]'),2)

    def test_json_and_csv_field_labels(self):
        j=Redactor().sanitized(json.dumps({'studentName':'Avery Fiction','studentId':'9876543210','grade':3,'goal':'6 of 10'}),'.json')
        obj=json.loads(j)
        self.assertIn('[[REDACTED: STUDENT_NAME',obj['studentName'])
        self.assertIn('[[REDACTED: STUDENT_ID',obj['studentId'])
        self.assertEqual(obj['goal'],'6 of 10')
        csvtext='student_name,dob,baseline\nAvery Fiction,01/02/2017,6/10\n'
        out=Redactor().sanitized(csvtext,'.csv')
        self.assertNotIn('Avery Fiction',out)
        self.assertNotIn('01/02/2017',out)
        self.assertIn('6/10',out)

    def test_email_phone_address_and_ssn(self):
        r=Redactor()
        value='Email: pupil@example.test\nPhone: 626-555-0123\nAddress: 123 Maple Road\nSSN: 111-22-3333\n'
        result=r.text(value)
        for original in ('pupil@example.test','626-555-0123','123 Maple Road','111-22-3333'):
            self.assertNotIn(original,result)
        self.assertIn('EMAIL_ADDRESS',result)
        self.assertIn('SSN',result)

    def test_cli_preserves_only_safe_report(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td)
            (d/'private-input.txt').write_text('Student Name: Avery Fiction\nDOB: 01/02/2017\n',encoding='utf-8')
            res=subprocess.run([sys.executable,str(SCRIPT),str(d/'private-input.txt'),'--out-dir',str(d/'out'),'--strict'],capture_output=True,text=True)
            self.assertEqual(res.returncode,2,res.stderr)
            redacted=(d/'out/redacted_001.txt').read_text()
            report=(d/'out/pii_review_report.json').read_text()
            self.assertIn('[[PII_REVIEW_REQUIRED]]',redacted)
            for secret in ('Avery Fiction','01/02/2017','private-input'):
                self.assertNotIn(secret,report)
            self.assertTrue(json.loads(report)['requires_manual_review'])

    def test_detected_identifiers_do_not_remove_skill_evidence(self):
        result=Redactor().text('Student Name: Avery Fiction\nBaseline: 5/10 correct with picture cues. Goal: 8/10 by 2027-10-14.')
        self.assertIn('5/10 correct',result)
        self.assertIn('8/10 by 2027-10-14',result)

if __name__=='__main__': unittest.main()
