"""Offline regression tests; never call GitHub or change repository state."""
import unittest
from import_board import merge_execution_plan, desired_labels


class PlanPreservationTests(unittest.TestCase):
    def test_changed_evidence_keeps_plan_and_member_notes(self):
        suffix = ('<!-- execution-plan:start -->\n成员审阅的方案\n'
                  '<!-- execution-plan:end -->\n成员追加说明')
        old = '旧判定\n\n' + suffix
        self.assertEqual(merge_execution_plan('新判定', old), '新判定\n\n' + suffix)
        self.assertEqual(merge_execution_plan('新判定', merge_execution_plan('新判定', old)),
                         '新判定\n\n' + suffix)

    def test_malformed_markers_stop_instead_of_losing_content(self):
        for body in ('<!-- execution-plan:start -->没有结束',
                     '<!-- execution-plan:end --><!-- execution-plan:start -->',
                     '<!-- execution-plan:start --><!-- execution-plan:start --><!-- execution-plan:end -->'):
            with self.subTest(body=body), self.assertRaises(ValueError):
                merge_execution_plan('新判定', body)

    def test_enrichment_labels_survive_source_status_update(self):
        old = {'labels': ['source:群聊', 'status:未完成', 'module:资料与需求核对', '建议执行人:王思琦']}
        row = {'labels': 'source:群聊,status:已完成'}
        self.assertEqual(desired_labels(old, row),
                         {'source:群聊', 'status:已完成', 'module:资料与需求核对', '建议执行人:王思琦'})


if __name__ == '__main__':
    unittest.main()
