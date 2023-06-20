import matplotlib.pyplot as plt

# setting variables and lists for student names, scores and student percentages
student_names = ['John', 'Megan', 'Cherry', 'Alisha', 'Tim', 'Brandon', 'Kavya', 'Yasir']
student_scores = [59, 65, 75, 80, 90, 69, 95, 100]
score_percentage = [59 * 100/100, 65 * 100/100, 75 * 100/100, 80 * 100/100, 90 * 100/100, 69 * 100/100, 95 * 100/100, 100 * 100/100]

def line_graph():
    # setting window name
    fig = plt.figure(num= 'Score Graph')
    # plotting the points on graph
    plt.plot(student_names, student_scores)
    # giving title to the graph
    plt.title('Students Score')
    
    # labelling x and y axis
    plt.xlabel('Student Names')
    plt.ylabel('Scores')
    plt.xlim(xmin= 0, xmax = 8)
    plt.ylim(ymin = 1, ymax = 100)
    plt.grid(True)
    
    # displaying plot
    plt.show()

def bar_graph():
    # setting window name for bar graph
    fig = plt.figure(num= 'Percentage Graph')
    
    # height variables for x and y axis
    left_edges = student_names
    height = score_percentage
    plt.bar(left_edges, height)
    
    # setting window title
    plt.title('Students Percentage')
    
    # labelling x and y axis
    plt.xlabel('Student Names')
    plt.ylabel('Students Percentage')
    
    # Displaying the plot
    plt.show()

line_graph()
bar_graph()