# coding:utf-8
import xlrd


class HandleExcel:
    """封装操作excel的方法"""

    def __init__(self, file='G:/rayfire/excel/TestAccountSet.xlsx', sheet_id=1):
        self.file = file
        self.sheet_id = sheet_id
        self.data = self.get_data()

    def get_data(self):
        data = xlrd.open_workbook(self.file)
        sheet = data.sheet_by_index(self.sheet_id)
        return sheet

    # 获取excel的行数
    def get_rows(self):
        rows = self.data.nrows
        return rows

    # 获取excel的列数
    def get_cols(self):
        cols = self.data.ncols
        return cols

    # 获取某个单元格的数据
    def get_cell_value(self, row, col):
        cell_value = self.data.cell_value(row, col)
        return cell_value

    # 向某个单元格写入数据
    def write_cell_value(self, row, col):
        pass

    # 获取excel的列名常量
    def get_caseSeq():
        """获取caseSeq"""
        caseSeq = 0
        return caseSeq

    def get_apitype():
        """获取apiType"""
        apiType = 1
        return apiType

    def get_apiseq():
        """获取apiSeq"""
        apiSeq = 2
        return apiSeq

    def get_apiName():
        """获取apiName"""
        apiName = 3
        return apiName

    def get_priority():
        """获取priority"""
        priority = 4
        return priority

    def get_url():
        """获取url"""
        url = 5
        return url

    def get_method():
        """获取method"""
        method = 6
        return method

    def get_header():
        """获取header"""
        header = 7
        return header

    def get_purpose():
        purpose = 8
        return purpose

    def get_params():
        """获取params"""
        params = 9
        return params

    def get_expectvalue():
        """获取expectValue"""
        expect = 10
        return expect

if __name__ == '__main__':
        test = HandleExcel()
        print(test.get_data())
        print(test.get_rows())
        print(test.get_cell_value(1, 1))
