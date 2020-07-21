import numpy as np 

X = np.random.normal(size=(20,20))

y = np.random.normal(size=(20,1))
y = y.astype(np.int32)

X_dash = np.transpose(X)

product = X_dash @ X

inverse_of_product = np.linalg.inv(product)

pre_theta = inverse_of_product @ X_dash

theta = pre_theta @ y

print(theta)

