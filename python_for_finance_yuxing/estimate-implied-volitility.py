from scipy import log,exp,sqrt,stats
def bs_call(S,X,T,r,sigm):
    """Objective: estimate call for stock with one known dividend
    S: current stock price
    T: maturity date in years
    r: risk-free rate
    sigma: volatility
    """
    d1 = (log(S/X)+(r+sigma*sigm/2.)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    return S*stats.norm.cdf(d1(d1)-X*exp(-r*T)*stats.norm.cdf(d2)
S=40
K=40
t=0.5
R=0.05
C=3.30
for i in range(200):
    sigma=0.005*(i+1)
                            
                        
