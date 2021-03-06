from unittest import TestCase
import MetricsCalculator

class TestMetrics(TestCase):
    def test_selectStmtCount(self):
        fileName = "./testSubject.sql"
        contents = MetricsCalculator.readFileContents(fileName)
        createStmts, insertStmts, selectStmts, updateStmts = MetricsCalculator.computeMetrics(contents)

        self.assertEquals(selectStmts, 4)

    def test_createTableStmtCount(self):
        fileName = "./testSubject.sql"
        contents = MetricsCalculator.readFileContents(fileName)
        createStmts, insertStmts, selectStmts, updateStmts = MetricsCalculator.computeMetrics(contents)

        self.assertEqual(createStmts, 1)

    def test_insertStmtCount(self):
        fileName = "./testSubject.sql"
        contents = MetricsCalculator.readFileContents(fileName)
        createStmts, insertStmts, selectStmts, updateStmts = MetricsCalculator.computeMetrics(contents)

        self.assertEqual(insertStmts, 2)

    def test_updateStmtCount(self):
        fileName = "./testSubject.sql"
        contents = MetricsCalculator.readFileContents(fileName)
        createStmts, insertStmts, selectStmts, updateStmts = MetricsCalculator.computeMetrics(contents)

        self.assertEqual(updateStmts, 1)