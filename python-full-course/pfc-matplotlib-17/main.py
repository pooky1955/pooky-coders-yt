import matplotlib.pyplot as plt
import numpy as np

# adding title
plt.title("An awesome title")

# plotting lines 
X = np.arange(0,10)
Y = X * 2 + 3
Y2 = X + 3
plt.plot(X,Y,label="first line")
plt.plot(X,Y2,label="second line")
plt.legend()
# saving a plot
plt.savefig("image.png")
plt.show()
# adding a legend

# plotting histograms
randn_array = np.random.randn(2000)
plt.hist(randn_array,bins=100)
plt.title("Histogram of standard distribution")
plt.show()


# plotting bar charts
labels = ["apple","orange","banana"]
counts = [10,20,5]
plt.title("Bar chart of fruits")
plt.bar(labels,counts)
plt.show()



# plotting scatter plot
SAMPLE_SIZE = 100000
X_randn = np.random.randn(SAMPLE_SIZE)
Y_randn = np.random.randn(SAMPLE_SIZE)

plt.title("Scatter plot of two random normal variables")
plt.scatter(X_randn,Y_randn)
plt.show()

# plotting images
data = plt.imread("image.png")
plt.title("Image of matplotlib previous plot")
plt.imshow(data)
plt.show()

# plotting in subplots
layout = (2,10)
total_plots = layout[0] * layout[1]
for i in range(total_plots):
    plt.subplot(layout[0],layout[1],i+1)
    plt.axis("off")
    plt.imshow(data)
plt.savefig("plot_of_plots.png")
plt.show()


