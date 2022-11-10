import pymssql

from checker import *
conn = pymssql.connect(server='*', user='*', password='*',
                       database='AdventureWorks2014', port='*')


def test_column_completeness_addressline1_address():
    assert verify_completeness(collect_result("Person.address", "addressLine1", conn)), "addressLine1 column is not " \
                                                                                        "complete "


def test_verify_address_FK():
    """
    Test checks whether all foreign keys are valid and exist

    """
    conn_cursor = conn.cursor()
    conn_cursor.execute("""
        SELECT COUNT(*) count_wrong_FK FROM (
        SELECT a.StateProvinceID FROM  person.Address a
        LEFT JOIN Person.StateProvince s 
        ON a.StateProvinceID = s.StateProvinceID WHERE s.StateProvinceID is NULL) AS t
                              """)
    result = conn_cursor.fetchall()
    assert result[0][0] == 0, "Foreign key is corrupted"


def test_min_value_length_postalcode_address():
    assert verify_min_length(collect_result("Person.address", "PostalCode", conn), 2),\
        f'PostalCode value is shorter than 2 '


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

