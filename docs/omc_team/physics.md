# The Physics of OMC

!!! note
    Long and detailed note of the kind of accelerator physics that OMC takes care of.
    Includes the prerequisites of accelerator physics necessary to do OMC work / understand OMC methods.
    See example headers below.
    
## Basic Error Propagation
Let's have a function $f$ of variables $x_i$, which can be well linearised around some point:

$$
f\approx f_0 + \sum_i \frac{\partial f}{\partial x_i} \notag
$$

then we can write $\sigma_f$ the error of $f$ as follows ($\sigma_f^2$ actually):

$$
\sigma_f^2=
\left(\begin{matrix} \frac{\partial f}{\partial x_1}&\frac{\partial f}{\partial x_2}&\cdots\end{matrix}\right)\cdot
\left(\begin{matrix} \sigma_1^2&\sigma_{12}&\cdots\\ \sigma_{21}&\sigma_2^2&\cdots\\ \vdots& \vdots& \ddots \end{matrix}\right)
\left(\begin{matrix} \frac{\partial f}{\partial x_1}\\\frac{\partial f}{\partial x_2}\\\vdots \end{matrix}\right), \notag
$$

where $\sigma_i$ are uncertainties of variables $x_i$. 
The matrix in the middle (covariance matrix) you may get, for instance, from a fit. 
We often assume that the variables are not correlated, i.e. covariance matrix has non-zero values only on the diagonal. 
In such a case, we get the famous formula:

$$
\sigma_f^2=\sum_i \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_i^2  \notag
$$

However, sometimes we should not neglect the covariances. 
For more details, look on the Wikipedia: https://en.wikipedia.org/wiki/Propagation_of_uncertainty or in your favourite statistics textbook.

## Basics of Accelerator Physics

## LHC IR Linear Optics

## LHC IR NonLinear Optics
