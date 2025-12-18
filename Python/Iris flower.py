import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in Iris dataset
iris = sns.load_dataset('iris')

# Create a pair plot to visualize patterns
sns.pairplot(iris, hue='species', palette='Set1')
plt.suptitle("Patterns in Iris Flower Dataset", y=1.02)
plt.show()
