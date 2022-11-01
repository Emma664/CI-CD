def get_result_by_percentage(corrupted_records_amount: int, overall_records_amount: int, description: str) -> bool:
    """Performs count of percentage of valid records to all records.

    Arguments:
        corrupted_records_amount -- number of corrupted records
        overall_records_amount -- number of all records
        description -- description of the check
    """
    percentage = 100 - corrupted_records_amount / overall_records_amount * 100
    print(f'{description} is {percentage} %.')
    return percentage == 100


def verify_completeness(records: list) -> bool:
    records_amount_with_empty_values = 0
    """Gets the number of fields that are null or empty.

       Arguments:
           records -- list of all values present in a column

       Returns the percentage of complete values to all values in the column.
       """
    for item in records:
        if item == "Null" or item == '' or item is None:
            records_amount_with_empty_values += 1

    return get_result_by_percentage(records_amount_with_empty_values, len(records), "Percentage of completed records")


def verify_max_length(records: list, max_length: int):
    records_amount_with_values_more_than_max_length = 0
    """Gets the number of values with length more than the allowed value.

    Arguments:
        records -- list of all values present in a column
        max_length -- allowed maximal length

    Returns the percentage of valid values to all values in the column.
    """
    for i in records:
        if len(str(i)) > max_length:
            records_amount_with_values_more_than_max_length += 1
    return get_result_by_percentage(records_amount_with_values_more_than_max_length, len(records),
                                    f"Percentage of records with length less than {max_length}")


def verify_allowed_values(records: list, allowed_values: list):
    """Gets the number of values that are not in the list of the allowed values.

    Arguments:
        records -- list of all values present in a column
        allowed_values -- list of allowed values

    Returns the percentage of valid values to all values in the column.
    """
    records_set = set(records)
    allowed_values_set = set(allowed_values)
    difference_set = records_set.difference(allowed_values_set)
    records_amount_with_not_allowed_values = len(difference_set)

    return get_result_by_percentage(records_amount_with_not_allowed_values, len(records),
                                    f"Percentage of records with allowed values ({allowed_values})")


def verify_min_length(records: list, min_length: int):
    records_amount_with_values_less_than_min_length = 0
    """Gets the number of values with length less than the allowed value.

    Arguments:
        records -- list of all values present in a column
        min_length -- allowed minimal length

    Returns the percentage of corrupted values to all values in the column.
    """
    for i in records:
        if len(str(i)) < min_length:
            records_amount_with_values_less_than_min_length += 1
    return get_result_by_percentage(records_amount_with_values_less_than_min_length, len(records),
                                    f"Percentage of records with length more than {min_length}")


def verify_counts(records: list, expected_count: int) -> bool:
    """Gets the number of records and compares to the expected count.

       Arguments:
           records -- list of all values present in a column
           expected_count -- expected number of records

       Returns true it the counts match.
       """

    return len(records) == expected_count


def verify_uniqueness(records: list) -> bool:
    """Gets the number of duplicated values in a record and compares it to the overall count

       Arguments:
           records -- list of all values present in a column

       Returns the percentage of deduplicated count to the overall count in the column.
       """

    return len(set(records)) == len(records)


def collect_result(table_name: str, column_name: str, connection_name: str):
    """Collects values of the specified column to the list.

    Arguments:
        table_name -- name of the table
        column_name -- name of the column
        connection_name -- name of the connection

    Returns the percentage of valid values to all values in the column.
    """
    c1 = connection_name.cursor()
    c1.execute(f"select {column_name} from {table_name}")
    c1_list_of_tuples = c1.fetchall()
    list_of_values = []
    for item in c1_list_of_tuples:
        list_of_values.append(item[0])
    return list_of_values
