# importing matplotlib for displaying signals
import matplotlib.pyplot as plt



class Plotter:
    def draw(x, y, title, pos, yplus, ynegv):
        plt.subplot(3, 1, pos)

        plt.title(title)
        plt.plot(x, y)
        
        plt.ylim(ynegv, yplus)