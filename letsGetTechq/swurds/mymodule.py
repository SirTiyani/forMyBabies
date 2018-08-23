#import matplotlib.pyplot as plt
# Graphing helper function
def plot_graph(x, y, color='blue', graph_type='line', 
               title=None, x_label='', y_label='', 
               fig_size=None, grid=True, save = False, 
               **kwargs):
    """plot graph by providing xy relation and graph type
    graph types are: 
        line
        bar
        scatter
        histogram"""
    import numpy as np
    import matplotlib.pyplot as plt
    
    # figure setup
    fig = plt.figure()
    if fig_size != None:
        fig.set_size_inches(fig_size[0], fig_size[1])
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if grid: ax.grid()
    
    # line plot
    if graph_type == 'line':
        ax.plot(x, y, color=color)
        ax.set_xlim(x[0], x[-1])
    # scatter plot
    if graph_type == 'scatter':
        ax.scatter(x, y, color=color)
        ax.set_xlim(x[0], x[-1])
    # bar graph
    if graph_type == 'bar':
        ax.bar(x, y, edgecolor = 'white', facecolor=color, 
               width = 0.8, alpha = 0.7, align= 'center',
               )
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        for x,y in zip(x, y):
            if y >= 0:
                ax.text(x,y, '%.0f' % y, ha='center', va='bottom')
            else:
                ax.text(x,y, '%.0f' % y, ha='center', va='bottom')
    # histogram
    if graph_type == 'histogram' or graph_type == 'hist':
        if len(kwargs) > 1:
            if 'bins' in kwargs: num_bins = kwargs['bins']
            if 'bin' in kwargs: num_bins = kwargs['bin']
            if 'density' in kwargs: density = kwargs['density']
        else:
            num_bins = 50
            density = 1
        n = y
        ax.hist(y, bins=num_bins, color=color, density=density)
        # add a 'best fit' line
    # save figure
    if save is True:
        ax.savefig(title + ".png", dpi = 670)
    
    
    

def doubleFactorial(n):
    return n * doubleFactorial(n-1) if n>1 else 1

def tree(n=12):
    r = int(0.2 * n)
    s = (' ' * (n-1)) + '*'
    L = [(('* ' * i)).center(n * 2) for i in range(1, n+1)]
    for i in range(r):
        L.append(s)
    return L

def funcVars(a=2, b=2, *args, **kwargs):
    "args is stored in a variable length list"
    return a**b, args, kwargs


class Person(object):
    def __init__(self, name = None, age = 0):
        self.name = name
        self.age = age
    
    def talk(self):
        return "my name is {}".format(self.name) if self.name != None else "there's food in my mouth"
    
    def walk(self):
        return "i can run dummy" if self.age > 1.2 else "need to nap"
    
    def setName(self, owner_name):
        self.name = owner_name
        return self.name
    
    def growthHomones(self):
        self.age += 0.9
        return "growing real fast. I'm now {:.2f} years old".format(self.age)


class Employer(Person):
    def job(self, job = None):
        self.job = job
    
    def work(self):
        if self.job != None:
            return "I am a {}".format(self.job) 
        else:
            return "still hustling"
    
    
class noInputError(Exception):
    "raise noInputError('Please supply at least one argument')"
    

class UserDB(object):
    def __init__(self, constring='test.db'):
        self.on = db.connect(constring)
        self.cur = self.con.cursor()
        
    def createTable(self):
        sql = '''CREATE TABLE users(
                            id INT PRIMARY KEY,
                            username VARCHR(64),
                            password VARCHAR(64))
              '''
        self.cur.execute(sql)
    
    def addUser(self, *args):
        sql = '''INSERT INTO users
              VALUES(?, ?, ?)'''
        if type(args[0]) in (tuple, list):
            cur.executemany(sql, args)
        else:
            self.cur.execute(sql, args)
        self.con.commit()
        return self
    
    def showTable(self):
        sql = 'SELECT * FROM users'
        print(self.cur.ececure(sql).fetchall())


if __name__ == '__main__()':
    print(' ')