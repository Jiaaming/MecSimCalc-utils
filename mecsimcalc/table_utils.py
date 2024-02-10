import pandas as pd
from typing import List


def table_to_dataframe(
    column_headers: List[str], rows: List[List[str]]
) -> pd.DataFrame:
    """
    >>> table_to_dataframe(column_headers: List[str], rows: List[List[str]]) -> pd.DataFrame

    Creates a DataFrame from given rows and column headers.

    Parameters
    ----------
    column_headers : List[str]
        A list of column headers.
    rows : List[List[str]]
        A list of rows where each row is a list of strings. Each row is converted into a DataFrame row.

    Returns
    -------
    pd.DataFrame
        A DataFrame constructed from the given rows and column headers.

    Raises
    ------
    ValueError
        If the length of any row is not equal to the length of column headers.

    Examples
    --------
    >>> column_headers = ["A", "B", "C"]
    >>> rows = [["1", "2", "3"], ["4", "5", "6"]]
    >>> df = table_to_dataframe(column_headers, rows)
    >>> print(df)
       A  B  C
    0  1  2  3
    1  4  5  6
    """
    for row in rows:
        if len(row) != len(column_headers):
            raise ValueError("Each row must have the same length as the column headers")

    return pd.DataFrame(rows, columns=column_headers)


def print_table(
    column_headers: List[str], rows: List[List[str]], index: bool = True
) -> str:
    """
    >>> print_table(column_headers: List[str], rows: List[List[str]]) -> str

    Creates an HTML table from given rows and column headers.

    Parameters
    ----------
    column_headers : List[str]
        A list containing the headers for each column in the table.
    rows : List[List[str]]
        A list of rows, where each row is a list of strings corresponding to the values for each column.
    index : bool, optional
        Whether to use the first column as the table's index. Defaults to True.

    Returns
    -------
    str
        A string representing the HTML table created from the provided rows and column headers.

    Examples
    --------
    >>> column_headers = ["A", "B", "C"]
    >>> rows = [["1", "2", "3"], ["4", "5", "6"]]
    >>> df = msc.table_to_dataframe(column_headers, rows)
    >>> print(df)
       A  B  C
    0  1  2  3
    1  4  5  6
    """

    df = table_to_dataframe(column_headers, rows)
    return df.to_html(index=index, border=1, escape=True)
