import pytest
import os
#from base.logger import Logger

#logger = Logger('root').getlog()
if __name__ == '__main__':
    pytest.main(['-s','--alluredir','./report/xml'])
    #logger.info('test end! Generate test report')
    html_report_generate ='allure generate report/xml/ -o report/html --clean'
    os.system(html_report_generate)

