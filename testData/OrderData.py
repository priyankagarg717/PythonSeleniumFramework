from PythonSeleniumFramework.utilities import excelReader


class OrderData:
    order_test_data = [{"items": ["Blackberry", "iphone X"], "search_location": "ind", "country": "India"},
                       {"items": ["Nokia Edge"], "search_location": "chi", "country": "China"}]

    order_excel_data = excelReader.get_excel_data("testData.xlsx", "testSheet2")
