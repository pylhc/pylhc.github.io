
# Basic Error Propagation

Let's have a function $f$ of variables $x_i$, which can be well linearised around some point $f_0$:

$$
\begin{equation}
f\approx f_0 + \sum_i \frac{\partial f}{\partial x_i}
\end{equation}
$$

then we can write the variance $\sigma_f^2$ of $f$ as follows:

$$
\begin{equation}
\sigma_f^2
=
J\Sigma J^T
=
\left(\begin{matrix} \frac{\partial f}{\partial x_1}&\frac{\partial f}{\partial x_2}&\cdots\end{matrix}\right)\cdot
\left(\begin{matrix} \sigma_1^2&\sigma_{12}&\cdots\\ \sigma_{21}&\sigma_2^2&\cdots\\ \vdots& \vdots& \ddots \end{matrix}\right)
\left(\begin{matrix} \frac{\partial f}{\partial x_1}\\\frac{\partial f}{\partial x_2}\\\vdots \end{matrix}\right)
,
\end{equation}
$$

where $J$ is the Jacobian of $f$ and the $\sigma_i$ are the uncertainties of variables $x_i$, while $\sigma_{ij}$ are the covariances between the variables.
The **covariance matrix** $\Sigma$ you can get, for instance, from a fitting function.
We often assume that the variables are not correlated, i.e. covariance matrix has non-zero values only on the diagonal.
In such a case, we get the famous formula:

$$
\begin{equation}
\sigma_f^2=\sum_i \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_i^2  
\end{equation}
$$

However, sometimes we should not neglect the covariances.
For details, see the more extensive [Wikipedia article about propagation of uncertainty][wiki_propagation_uncertainty]{target=_blank} or your favourite statistics textbook.


[wiki_propagation_uncertainty]: https://en.wikipedia.org/wiki/Propagation_of_uncertainty
