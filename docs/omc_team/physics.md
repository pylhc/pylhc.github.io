# The Physics of OMC

!!! note
    Long and detailed note of the kind of accelerator physics that OMC takes care of.
    Includes the prerequisites of accelerator physics necessary to do OMC work / understand OMC methods.
    See example headers below.


Until this section is filled, [Ewens presentation at Uni Goettingen][maclean_goettingen_2019]{target=_blank} provides some insights.

## Basic Error Propagation

Let's have a function $f$ of variables $x_i$, which can be well linearised around some point $f_0$:

$$
f\approx f_0 + \sum_i \frac{\partial f}{\partial x_i}
$$

then we can write the variance $\sigma_f^2$ of $f$ as follows:

$$
\sigma_f^2
=
J\Sigma J^T
=
\left(\begin{matrix} \frac{\partial f}{\partial x_1}&\frac{\partial f}{\partial x_2}&\cdots\end{matrix}\right)\cdot
\left(\begin{matrix} \sigma_1^2&\sigma_{12}&\cdots\\ \sigma_{21}&\sigma_2^2&\cdots\\ \vdots& \vdots& \ddots \end{matrix}\right)
\left(\begin{matrix} \frac{\partial f}{\partial x_1}\\\frac{\partial f}{\partial x_2}\\\vdots \end{matrix}\right)
,
$$

where $J$ is the Jacobian of $f$ and the $\sigma_i$ are the uncertainties of variables $x_i$, while $\sigma_{ij}$ are the covariances between the variables.
The **covariance matrix** $\Sigma$ you can get, for instance, from a fitting function.
We often assume that the variables are not correlated, i.e. covariance matrix has non-zero values only on the diagonal.
In such a case, we get the famous formula:

$$
\sigma_f^2=\sum_i \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_i^2  
$$

However, sometimes we should not neglect the covariances.
For details, see the more extensive [Wikipedia article about propagation of uncertainty][wiki_propagation_uncertainty]{target=_blank} or your favourite statistics textbook.

## Basics of Accelerator Physics

Write here Andreas (or make a new section, maybe "Coupling?").

## LHC IR Linear Optics

## LHC IR NonLinear Optics


[wiki_propagation_uncertainty]: https://en.wikipedia.org/wiki/Propagation_of_uncertainty
[maclean_goettingen_2019]: https://indico.cern.ch/event/788195/contributions/3364867/attachments/1886006/3109100/2019_07_25_HASCO_lcomp.pdf