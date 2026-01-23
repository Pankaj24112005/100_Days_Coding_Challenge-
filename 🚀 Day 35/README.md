# Pandas Filtering, Sorting & Indexing (Day 35)

This project demonstrates core Pandas operations:
Filtering, Sorting, and Indexing/Selection.
It is useful for Data Science, AI/ML, internships, and interviews.

--------------------------------------------------
PROJECT FILES
--------------------------------------------------
Pandas_Filtering_Sorting_Indexing.ipynb
README.md

--------------------------------------------------
TOPICS COVERED
--------------------------------------------------

1) FILTERING
- Boolean filtering: df[df["Age"] > 23]
- Label-based filtering: df.loc[condition]
- Query-based filtering: df.query()

2) SORTING
- Sort by column values: df.sort_values()
- Ascending & Descending order
- Sort by index: df.sort_index()

3) INDEXING / SELECTION
- Row selection: df.iloc[]
- Column selection: df[["col1","col2"]]
- Set index: df.set_index()
- Reset index: df.reset_index()
- Access using index: df.loc["index_name"]

--------------------------------------------------
SAMPLE DATA USED
--------------------------------------------------
Columns:
- Name
- Age
- Department
- Salary

--------------------------------------------------
TECH STACK
--------------------------------------------------
Python
Pandas
Jupyter Notebook

--------------------------------------------------
HOW TO RUN (TERMINAL)
--------------------------------------------------

# Step 1: Create virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Step 2: Install dependencies
pip install pandas notebook

# Step 3: Launch Jupyter Notebook
jupyter notebook

# Step 4: Open file
Pandas_Filtering_Sorting_Indexing.ipynb

--------------------------------------------------
LEARNING GOAL
--------------------------------------------------
Build strong fundamentals in Pandas data manipulation
for Data Science, AI/ML projects, and placements.

--------------------------------------------------
AUTHOR
--------------------------------------------------
Pankaj J
Day 35 – Data Science / Python Learning Journey
