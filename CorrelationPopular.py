from scipy.stats import linregress


__author__ = 'Abdul Rubaye'

issue_pop = []

def coeff(a,b):
    r = linregress(a,b)
    print str(r[2])
    print str(float(r[3]))
    print ('-'*100)

if __name__ == "__main__":

    coeff(issue_pop, issue_blw)
