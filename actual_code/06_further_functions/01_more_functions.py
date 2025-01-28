"""
Scope - Local and Global Variables
Anonymous/Lambda functions
filter & map
"""

count = 10

def new_func():
    local_count = 100
    global count  # use carefully!
    count += 1
    print(f"Local count: {local_count}")
    print(f"Global count: {count}")

new_func()
print(count)

# - Local variables aren't available outside of their function
# - Global variables are readable inside of a function
# - Local variables can "shadow" global variables
# - Global variables are not write-able (by default) inside a function
# - But we can write to them if we declare `global variable_name` first
