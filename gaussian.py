import math
import matplotlib.pyplot as plt


class Gaussian():
    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.            
    """
    def __init__(self, mu = 0, sigma = 1):
        
        self.mean = mu
        self.stdev = sigma
        self.data = []


    def __repr__(self):
    
        """Update repr to print mean and standard deviation 
               <Gaussian | mean: {}, standard deviation: {}>
        """

        return "<Gaussian | mean: {}, standard deviation: {}>".format(self.mean, self.stdev)

    
    def calculate_mean(self):
    
        """Method to calculate the mean of the data set.  
        """
        
        if self.data == []:
            self.mean = 0
        else: 
            sum = 0.0
            for value in self.data:
                sum += value
            self.mean = 1.0 * sum /len(self.data)
        
        return self.mean
                

    def calculate_stdev(self, sample=True):

        """Method to calculate the standard deviation of the data set.
        """
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.calculate_mean()

        sigma = 0

        for value in self.data:
            sigma += (value - mean) ** 2

        standard_deviation = math.sqrt(sigma / n)
        
        self.stdev = standard_deviation

        return standard_deviation


    def read_data_file(self, file_name, sample=True):
    
        """Method to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute. 
        After reading in the file, the mean and standard deviation are calculated
        """

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
        self.calculate_mean()
        self.calculate_stdev(sample)
    
        
    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        """
        
        data = self.data

        plt.hist(data)
        plt.title("Histogram of the Data")
        plt.xlabel("data")
        plt.ylabel("count")
                
        
    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        """
        
        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)        

    def plot_histogram_pdf(self, n_spaces = 50):

        """Method to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        """
        
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y
    
    def __add__(self, other):
        
        """Creates a new Gaussian object with the data of the two Gaussian distributions           
        """

        result = Gaussian()

        new_mean = self.mean + other.mean

        new_stdev = math.sqrt(((self.stdev ** 2) + (other.stdev ** 2)))

        
        result.mean = new_mean 
        result.stdev = new_stdev 
        
        return result

