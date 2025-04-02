# ud120-projects
This repository shows my solutions to the projects proposed in the course of Udacity's [**Intro to Machine Learning**](https://www.udacity.com/enrollment/ud120). The following are the answers for each section:

## Naive Bayes
```PowerShell
> python nb_author_id.py
no. of Chris training emails: 7936
no. of Sara training emails: 7884
Training time: 1.52 s
Predicting time: 0.209 s
The accuracy of Naive Bayes author identifier is 0.9732650739476678
```

## SVM (Support Vector Machine)
- With training and test datasets at 100%, and using a linear kernel:
```PowerShell
> python svm_author_id.py
no. of Chris training emails: 7936
no. of Sara training emails: 7884
Training time: 111.625 s
Predicting time: 10.488 s
The accuracy of SVM author identifier is 0.9840728100113766
```
- With training and test datasets at 1%, and using a linear kernel:
```PowerShell
> python svm_author_id.py
no. of Chris training emails: 7936
no. of Sara training emails: 7884
Training time: 0.05 s
Predicting time: 0.376 s
The accuracy of SVM author identifier is 0.8845278725824801
```
- With training and test datasets at 1%, and using a rbf kernel:
```PowerShell
> python svm_author_id.py
no. of Chris training emails: 7936
no. of Sara training emails: 7884
Training time: 0.049 s
Predicting time: 0.708 s
The accuracy of SVM author identifier is 0.8953356086461889
```
- With training and test datasets at 1%, using a rbf kernel and C = 10000.0:
```PowerShell
>python svm_author_id.py
no. of Chris training emails: 7936
no. of Sara training emails: 7884
Training time: 0.048 s
Predicting time: 0.804 s
The accuracy of SVM author identifier is 0.8998862343572241
```
- With training and test datasets at 100%, using a rbf kernel and C = 10000.0:
```PowerShell
>python svm_author_id.py
no. of Chris training emails: 7936
no. of Sara training emails: 7884
Training time: 122.881 s
Predicting time: 16.143 s
The accuracy of SVM author identifier is 0.9960182025028441
```
- With training and test datasets at 1%, using a rbf kernel and C = 10000.0. What are the predictions for 10th, 26th and 50th element?
```PowerShell
> python svm_author_id.py
no. of Chris training emails: 7936
no. of Sara training emails: 7884
Training time: 0.041 s
Predicting time: 0.833 s
The accuracy of SVM author identifier is 0.8998862343572241
Prediction for element 10: 1 #Chris
Prediction for element 26: 0 #Sara
Prediction for element 50: 1 #Chris
```
