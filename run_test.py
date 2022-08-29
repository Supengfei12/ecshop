import unittestreport
import unittest
suite = unittest.defaultTestLoader.discover('./scripts', pattern='test*.py')

unittestreport.TestRunner(
    suite=suite,
    filename='report5.html',
    report_dir='reports',
    title='测试报告',
    tester='苏鹏飞',
    desc='ecshop商城项目',
    templates=2
).run()