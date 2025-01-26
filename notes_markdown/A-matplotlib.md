# Plan for Session
- What is Matplotlib?
- Where does it fit in?
- `pyplot` Scripting API
- Simple Line Plot
- Configuring a Plot
- Multiple Line Plot
- Bar Charts
- Pie Charts
- Scatter Graph
- Saving Plot to a File

---

## What is Matplotlib?
- A Python plotting library supporting:
  - Plots, histograms, bar charts
  - Scatter graphs, heat maps, 3D plots
  - Animation, image display, etc.
  - Can have interactive plots
- Very widely used
- For more details, see [Matplotlib Home Page](http://matplotlib.org/)
- Also see [W3 Schools Matplotlib Overview](https://www.w3schools.com/python/matplotlib_intro.asp)

---

## Where Does Matplotlib Fit In?
- Can be used in any Python program.
- Part of a suite of tools commonly used in data analytics:
  - Pandas
  - Matplotlib
  - Python
  - NumPy
  - SciPy

---

## `pyplot` Scripting API
- Several ways to work with Matplotlib:
  - Most common (and easiest) is via `pyplot` API, a module of Matplotlib.
  - Usually imported as `pyplot` or `plt`.
- `pyplot` API is used to:
  - Construct the plot.
  - Configure labels and axes.
  - Manage color and line styles.
  - Handle events / allow plots to be interactive.
  - Display (show) the plot.

### Example:
```python
import matplotlib.pyplot as pyplot
```

---

## Simple Plot
- Using `matplotlib.pyplot` to generate a basic graph.

### Example:
```python
# Import the pyplot API
import matplotlib.pyplot as pyplot

# Plot a sequence of values
pyplot.plot([3, 4, 6, 9, 11, 12, 10, 11, 14, 16])

# Display the chart in a window
pyplot.show()
```

---

## Configuring a Plot
- You can set x and y labels, graph title, line styles, etc.

### Example:
```python
import matplotlib
import matplotlib.pyplot as pyplot

x = range(1, 11)
y = [3, 4, 6, 9, 11, 12, 10, 11, 14, 16]

# Set the axes headings
pyplot.ylabel('y values', fontsize=12)
pyplot.xlabel('x values', fontsize=12)

# Set the title
pyplot.title("Sample Graph using Matplotlib " + str(matplotlib.__version__))

# Configure line on plot
pyplot.plot(x, y, linewidth=2.0, label="samples", marker='o', color='blue', linestyle='--')

# Include a grid
pyplot.grid()

# Display the graph
pyplot.show()
```

---

## Multi-Line Plot
- Can have more than one graph on a plot.

### Example:
```python
# …
x = range(1, 11)
y1 = [3, 4, 6, 9, 11, 12, 10, 11, 14, 16]
y2 = [4, 5, 6, 7, 8, 7, 6, 3, 2, 1]
y3 = [10, 11.5, 12, 10.5, 9, 7.5, 7, 4, 2.3, 1]

# Draw each line graph
pyplot.plot(x, y1, label="dataset1", color='blue', linestyle='--')
pyplot.plot(x, y2, label="dataset2", color='red', linestyle=':')
pyplot.plot(x, y3, label="dataset3", color='green')

# Generate the legend
pyplot.legend()

pyplot.show()
```

---

## Bar Charts
- Can also create bar charts.

### Example:
```python
import matplotlib.pyplot as pyplot

# Set up the data
labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5)
sizes = [45, 10, 15, 30, 22]

# Set up the bar chart
pyplot.bar(index, sizes, tick_label=labels)

# Set up the horizontal bar chart
# pyplot.barh(index, sizes, tick_label=labels)

# Configure the layout
pyplot.ylabel('Usage')
pyplot.xlabel('Programming Languages')

# Display the chart
pyplot.show()
```

### Example: Configuring Colors
```python
import matplotlib.pyplot as pyplot

# Set up the data
labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5)
sizes = [45, 10, 15, 30, 22]

# Set up the multi-colored bar chart
pyplot.bar(index, sizes, tick_label=labels, color=('red', 'green', 'blue', 'yellow', 'orange'))

# Configure the layout
pyplot.ylabel('Usage')
pyplot.xlabel('Programming Languages')

# Display the chart
pyplot.show()
```

---

## Pie Charts
- Can create pie charts.

### Example:
```python
import matplotlib.pyplot as pyplot

labels = ('Python', 'Java', 'Scala', 'C#')
sizes = [45, 30, 15, 10]

pyplot.pie(sizes, labels=labels, autopct='%.1f%%', counterclock=False, startangle=90)
pyplot.show()
```

### Example: Configuring Pie Charts
```python
import matplotlib.pyplot as pyplot

labels = ('Python', 'Java', 'Scala', 'C#')
sizes = [45, 30, 15, 10]

# Only "explode" the 1st slice (i.e., 'Python')
explode = (0.1, 0, 0, 0)

pyplot.pie(sizes, explode=explode, labels=labels, autopct='%.0f%%', shadow=True, counterclock=False, startangle=90)
pyplot.show()
```
- `explode` value also indicates by how much.

---

## Scatter Plots
- Can also generate scatter graphs.

### Example:
```python
# Create data
riding = ((17, 18, 21, 22, 19, 21, 25, 22, 25, 24), (3, 6, 3.5, 4, 5, 6.3, 4.5, 5, 4.5, 4))
swimming = ((17, 18, 20, 19, 22, 21, 23, 19, 21, 24), (8, 9, 7, 10, 7.5, 9, 8, 7, 8.5, 9))
sailing = ((31, 28, 29, 36, 27, 32, 34, 35, 33, 39), (4, 6.3, 6, 3, 5, 7.5, 2, 5, 7, 4))

# Plot the data
pyplot.scatter(x=riding[0], y=riding[1], c='red', marker='o', label='riding')
pyplot.scatter(x=swimming[0], y=swimming[1], c='green', marker='^', label='swimming')
pyplot.scatter(x=sailing[0], y=sailing[1], c='blue', marker='*', label='sailing')

pyplot.show()
```

---

## Saving Plot to a File
- Can do this interactively or programmatically.

### Example:
```python
import matplotlib.pyplot as pyplot

# Plot a sequence of values
pyplot.plot([3, 4, 6, 9, 11, 12, 10, 11, 14, 16])

print('Saving plot as png file')

# Save the plot to a file
pyplot.savefig('plot.png')
```

---

## Additional Useful Resources
- [Matplotlib Home](http://matplotlib.org)
- [Python Matplotlib Crash Course](https://pythonprogramming.net/matplotlib-python-3-basics-tutorial)
- Books:
  - *Mastering Matplotlib* by Duncan M. McGreggor
  - *Matplotlib Plotting Cookbook* by A. Devert
  - *Matplotlib for Python Developers* by S. Tosi

---

## Questions?

?
