"""

Dataframe Creation and Loading:

pandas.DataFrame(): Creating a DataFrame.
read_csv(): Reading data from a CSV file into a DataFrame.
read_excel(): Reading data from an Excel file into a DataFrame.
from_dict(): Creating a DataFrame from a dictionary.
from_records(): Creating a DataFrame from a list of records.
pd.concat(): Combining multiple DataFrames.
Data Exploration:

head(): Viewing the first few rows of a DataFrame.
tail(): Viewing the last few rows of a DataFrame.
info(): Displaying information about the DataFrame.
describe(): Generating summary statistics of numeric columns.
shape: Getting the dimensions (rows and columns) of a DataFrame.
columns: Accessing the column names of a DataFrame.
dtypes: Getting data types of columns.
Data Selection and Filtering:

loc[]: Accessing rows and columns by label.
iloc[]: Accessing rows and columns by integer index.
at[]: Accessing a single element by label.
iat[]: Accessing a single element by integer index.
isin(): Filtering rows based on a condition.
query(): Filtering rows using a query expression.
Data Manipulation:

drop(): Removing rows or columns from a DataFrame.
rename(): Renaming columns or indices.
sort_values(): Sorting a DataFrame by one or more columns.
fillna(): Filling missing values in a DataFrame.
drop_duplicates(): Removing duplicate rows.
apply(): Applying a function to each element or row of a DataFrame.
replace(): Replacing values in a DataFrame.
pivot_table(): Creating a pivot table for data aggregation.
Grouping and Aggregation:

groupby(): Grouping data by one or more columns for aggregation.
agg(): Applying aggregation functions (e.g., sum, mean) to grouped data.
count(): Counting non-null values in each group.
sum(): Calculating the sum of values in each group.
mean(): Calculating the mean of values in each group.
max() and min(): Finding maximum and minimum values in each group.
Data Cleaning:

dropna(): Removing rows or columns with missing values.
fillna(): Filling missing values with specified values or methods.
interpolate(): Interpolating missing values.
replace(): Replacing values with other values.
Merging and Joining:

merge(): Merging two DataFrames based on common columns.
concat(): Concatenating DataFrames vertically or horizontally.
String Operations:

str.contains(): Checking for substring existence in string columns.
str.split(): Splitting string columns into multiple columns.
str.strip(): Removing leading and trailing whitespaces.
Datetime Handling:

to_datetime(): Converting a column to datetime format.
dt.year, dt.month, etc.: Extracting date components.
Reshaping Data:

melt(): Unpivoting a DataFrame.
stack() and unstack(): Pivoting and unstacking data.
pivot(): Creating a pivot table from long data.
Statistical Analysis:

corr(): Calculating the correlation between columns.
cov(): Calculating the covariance between columns.
value_counts(): Counting unique values in a column."""