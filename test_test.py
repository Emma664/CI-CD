import pymssql

from checker import *
conn = pymssql.connect(server='127.0.0.1', user='youruser', password='yourpassword',
                       database='AdventureWorks2014', port='yourport')


def test_column_completeness_addressline1_address():
    assert verify_completeness(collect_result("Person.address", "addressLine1", conn)), "addressLine1 column is not " \
                                                                                        "complete "


def test_column_completeness_addressline2_address():
    assert verify_completeness(collect_result("Person.address", "addressLine2", conn)), "addressLine2 column is not " \
                                                                                        "complete "


def test_max_value_length_postalcode_address():
    assert verify_max_length(collect_result("Person.address", "PostalCode", conn), 5),\
        f'PostalCode value is longer than 5 '


def test_allowed_values_status_document():
    assert verify_allowed_values(collect_result("Production.document", "Status", conn), [1, 2, 3]),\
        f'Status contains values that are not expected (1,2,3)'


def test_min_value_length_owner_document():
    assert verify_min_length(collect_result("Production.document", "Owner", conn), 3),\
        f'Owner value is shorter than 3 '


def test_counts_unitmeasure():
    assert verify_counts(collect_result("Production.UnitMeasure", "UnitMeasureCode", conn), 38),\
        f'Count of UnitMeasureCode does not equals to 38'


def test_uniqueness_unitmeasure():
    assert verify_uniqueness(collect_result("Production.UnitMeasure", "UnitMeasureCode", conn)),\
        f'UnitMeasureCode values are not unique'
