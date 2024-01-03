# CoKriging

We use the Co-Kriging method to predict our regression coefficients using our feature vectors.

X and Y are the features vectors, and Z is the probabilies of the three stages.
X(t) = [X_1(t), X_2(t), ... , X_n(t)] where n is the number of features
Z_i = P_h, P_p, P_i
T_i = time at each photo

$Z*i = \mu_Z(T_i) + \Beta*{ZX} \dot (X*I - \mu_X) + \Beta*{ZY} \dot (Y_i - \mu_Y)$
