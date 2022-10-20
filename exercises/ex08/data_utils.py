"""Dictionary related utility functions."""

__author__ = "730556651"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # open a handle to the data file
    file_handle = open(filename, 'r', encoding='utf8')
    # read that file
    csv_reader = DictReader(file_handle)
    # read each row of the csv line-by-line
    for row in csv_reader:
        result.append(row)
    # close that file when done to free its resources
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: 'str') -> list[str]:
    """Produce a list of values in a particular column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only N number of rows."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        rows_in_column: list[str] = []
        if rows > len(column_table[column]):
            rows = len(column_table[column])
        for i in range(0, rows):
            rows_in_column.append(column_table[column][i])
        result[column] = rows_in_column
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only specificly selected columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = column_table[column]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Takes two column-based tables and combines them into one."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            for i in range(0, len(table_2[column])):
                result[column].append(table_2[column][i])
        else:
            result[column] = table_2[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Given a list of strings, returns a dict with the frequency of each string value."""
    val_frequency: dict[str, int] = {}
    for value in values:
        if value in val_frequency:
            val_frequency[value] += 1
        else:
            val_frequency[value] = 1
    return val_frequency