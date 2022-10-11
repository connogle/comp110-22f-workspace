"""Some helpful utility functions for helping with csv files."""


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """read the rows of a csv into a 'table'."""
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



def coulumn_values(table: list[dict[str, str]], column: 'str') -> list[str]:
    """Produce a list[str] of hte values in a particular column."""
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
        result[column] = coulumn_values(row_table, column)
    return result
