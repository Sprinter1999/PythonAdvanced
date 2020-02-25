## Fenkit-learn

An implementation of some traditional ML algorithms in Scikit-learn style.
During this winter, I've learned some traditional ML algorithms and use them to cope with some problems.Here's a brief summary of this period.
- **Data and Dataset**: Data scale and Data features, sometimes Data far outweighs the algorithm. Some measures should be taken, like Normalization and Standardization.
- Numpy , visualization and some tricks of juPyter.
- **kNN**: Non-parameter algorithm, driven by Data. There're some hyper parameters in it, like num of neighbors, by num or by distance, and the p of minkowski distance. To figure out the best model for a situation, a grid-search process is needed. Sometimes, hyper parameters are not independent.
- **Linear Regression**: For starters, the *least square method* is what we have learned in middle school. Then we reach theta(vector) weight to cope with multi-feature problem, and we have the solution of normal equation.In this process, a vectorilzed calculating saves the solving time for a computer.Meanwhile, a criteria is needed to evaluate, like rmse, mse, mae, r2square.
- **Gradient Descent**:In fact, it's an optimization problem.Enlighted by simulated annealing algorithm, we have Bacth gradient descent,to stochastic gradient descent ,and to mini-batch and other tricks. Learning rate and iteration times are important hyper parameters.
- **PCA**: Demean, gradient ascent, feature faces, etc
- **Polynomial Regression**: A special linear regression, cross-validation,over-fitted situation,normalization terms(l1,l2)--LASSO and Ridge regression, pipeline of SKlearn style solution process.
- **Logistics Regression**: A special linear regression based on Probabalities, the gradient calculation process,polynomial feature, OVO&OVR(multi-classifier), decision border
- **Evaluation**: Only thinking about accuracy is not enough,especially when the data is sknewed, Recall rate and precesion rate should be considered.
- **SVM**: A more mathematical solution for both classifying and regression. A task of optimization under some limitations. Kernel functions like polynomial ones and gaussion RBF.
- **Decision Tree**: Entropy,Gini-Index,CART implemantation,classifier and regressor,and the limitations of Decision tree model.
- **Ensemble learning and random forest**:Hard&Soft voting classifier, Bagging or Pasting, OOB truth, Random Forest and Extra trees, Ada boost and gradient boost.
- "Bayes"
- "NN"