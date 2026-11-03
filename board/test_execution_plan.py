"""Offline regression tests; never call GitHub or change repository state."""
import unittest
from import_board import merge_execution_plan, desired_labels


class PlanPreservationTests(unittest.TestCase):
    def test_changed_evidence_keeps_plan_and_member_notes(self):
        suffix = ('<!-- execution-plan:start -->\nMember-reviewed plan\n'
                  '<!-- execution-plan:end -->\nAdditional member note')
        old = 'Old evidence\n\n' + suffix
        self.assertEqual(merge_execution_plan('New evidence', old), 'New evidence\n\n' + suffix)
        self.assertEqual(merge_execution_plan('New evidence', merge_execution_plan('New evidence', old)),
                         'New evidence\n\n' + suffix)

    def test_malformed_markers_stop_instead_of_losing_content(self):
        for body in ('<!-- execution-plan:start -->No end marker',
                     '<!-- execution-plan:end --><!-- execution-plan:start -->',
                     '<!-- execution-plan:start --><!-- execution-plan:start --><!-- execution-plan:end -->'):
            with self.subTest(body=body), self.assertRaises(ValueError):
                merge_execution_plan('New evidence', body)

    def test_enrichment_labels_survive_source_status_update(self):
        old = {'labels': ['source:wechat', 'status:unfinished', 'module:requirements', 'suggested-lead:wang-siqi']}
        row = {'labels': 'source:wechat,status:completed'}
        self.assertEqual(desired_labels(old, row),
                         {'source:wechat', 'status:completed', 'module:requirements', 'suggested-lead:wang-siqi'})


if __name__ == '__main__':
    unittest.main()
