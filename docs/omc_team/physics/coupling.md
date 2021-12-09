

!!! Note
    This section makes heavy use of normal forms and resonance driving terms (RDTs).
    An introductin to those topics is beyond the scope of this website.
    The reader is referred to the great, illustrative introductions at the
    [CAS in Trondheim][herr_cas],
    [W. Herr's and E. Forest's chapter about non-linear dynamics][herr_forest_nf] and
    [R. Tomas' paper about RDTs][tomas_rdt]
    and - for the full mathematical details - to the papers of [Bazzani][bazzani_normal_form]
    and [Bartolini][bartolini_normal_form].


## The 2-BPM-Method
One possible method to calculate coupling used for LHC - which is independent of BPM calibration errors -
makes use of two nearby BPMs in order to cancel out calibration factors. It is therefore called
the _two BPM method_. This method is described in this section.

Under the assumption that no other perturbations than linear transverse coupling are present in the
lattice, the Courant-Snyder coordinates $h_{x/y}^\pm$ read

$$
\newcommand{\conj}[1]{#1^*}
\begin{align}
 h_x^+ &= \zeta_x^+ + 2i\conj{f_{1010}} \zeta_y^- + 2i\conj{f_{1001}}\zeta_y^+  \\
    h_y^+ &= \zeta_y^+ + 2i\conj{f_{1010}} \zeta_x^- + 2i{f_{1001}}\zeta_x^+  \\
    h_x^- &= \zeta_x^- - 2i{f_{1010}} \zeta_y^+ - 2i{f_{1001}}\zeta_y^-   \\
    h_y^- &= \zeta_y^- - 2i{f_{1010}} \zeta_x^+ - 2i\conj{f_{1001}}\zeta_x^-
\end{align}
$$

where $\zeta_{x/y}^\pm$ denotes normal form coordinates and $f_{1001}$ and $f_{1010}$ are the
coupling RDTs. A calculation of the relations above can be found in Franchi's paper about emittance sharing: [10.1103/PhysRevSTAB.10.064003][franchi_emittance_sharing].

By the term _spectral lines_, we usually denote the Fourier transforms of the turn-by-turn spectrum.

$$
\begin{align}
    H^\pm(n_x,n_y) &= \mathcal{F}\{h_x^\pm\}(n_xQ_x+n_yQ_y) \\
    V^\pm(n_x,n_y) &= \mathcal{F}\{h_y^\pm\}(n_xQ_x+n_yQ_y) 
\end{align}
$$

If the BPM calibration is not perfect, the measured $H$ and $V$ lines are not proportional w.r.t. each other:

$$
\newcommand{\meas}{^\text{meas}}
\begin{align}
   x\meas &= C_x x \\
   y\meas &= C_y y
\end{align}
$$

The calibration factors $C_{x/y}$ cancel out if one divides the spectral line by the amplitude of
the main line:

$$
\begin{align}
    A_{0,n_y} &= \frac{H^+(0,n_y)}{\left|H^+(1,0)\right|} \\
    B_{n_x,0} &= \frac{V^+(n_x,0)}{\left|V^+(0,1)\right|} 
\end{align}
$$

Important for the coupling calculation are the following normalised spectral lines:

$$
\begin{align}
    A_{0,1}&=\frac{H^+(0,1)}{\left|H^+(1,0)\right|}
      &= 2i\sqrt{\frac{J_y}{J_x}}f_{1001}^* e^{-i\varphi_{y}}
      \\
    B_{1,0}&=\frac{V^+(1,0)}{\left|V^+(0,1)\right|}
      &= 2i\sqrt{\frac{J_x}{J_y}}{f_{1001}} e^{-i\varphi_{x}}
\end{align}
$$

which contain $f_{1001}$ and

$$
\begin{align}
    A_{0,-1}&=\frac{H^+(0,-1)}{\left|H^+(1,0)\right|}
      &= 2i\sqrt{\frac{J_y}{J_x}}f_{1010}^* e^{i\varphi_{y}}
    \\
    B_{-1,0}&=\frac{V^+(-1,0)}{\left|V^+(0,1)\right|}
      &= 2i\sqrt{\frac{J_x}{J_y}}f_{1010}^* e^{i\varphi_{x}}
\end{align}
$$

which contain $f_{1010}$.

The coupling RDTs $f_{1010}$ and $f_{1001}$ can then be calculated by combining
the equations for $A_{0,1}$, $B_{1,0}$, $A_{0,-1}$ and $B_{-1,0}$
, respectively:

$$
\begin{align}
    \left|f_{1001}\right| &= \frac{1}{2}\sqrt{\left| A_{0,1}B_{1,0} \right|}
\label{eq:normalised_spectral_line_to_rdt_diff} \\
    \left|f_{1010}\right| &= \frac{1}{2}\sqrt{\left| A_{0,-1}B_{-1,0} \right|}
\label{eq:normalised_spectral_line_to_rdt_sum}
\end{align}
$$

The normalised spectral lines $A_{0,n_y}$ and $B_{n_x,0}$ are the Fourier components of the complex
coordinates. But only the projections onto the real axis can be measured. The next step is to calculate
the complex coordinates from the measured ones.

Since $h_z^\pm = z \pm ip_z$, the complex coordinate can be obtained from position and momentum.
BPMs can only measure position but using the position data from a second BPM one can reconstruct the momentum.
The propagation of complex C-S coordinates through a region that is empty of non-linearities reads

$$
\begin{equation}
    \begin{pmatrix}
        z\\p_z
    \end{pmatrix}_b = \mathbf{R}_{ab}
    \begin{pmatrix}
        z\\p_z
    \end{pmatrix}_a
\end{equation}
$$

where the transfer matrix $\mathbf{R}_{ab}$ is a simple rotation matrix.
From this one can reconstruct the momentum:

$$
\begin{equation}
    p_a = \frac{x_b}{\cos\Delta} + x_a \tan\Delta
\end{equation}
$$

where $\Delta$ is the deviation from $\pi/2$ of the phase advance between the two positions $s_a$ and $s_b$.
Therefore:

$$
\begin{equation}
    h_z^\pm(s_a) = z_a - i \left(\frac{z_b}{\cos\Delta} + z_a\tan\Delta \right) = z_a(1-i\tan\Delta) - i \frac{z_b}{\cos\Delta}
\end{equation}
$$

Since the Fourier transform is linear, this identity can be propagated to the spectral lines:

$$
\begin{equation}
\label{eq:reconstr_cplx}
    H^+(n_x,n_y)_a = (1-i\tan\Delta)H(n_x,n_y)_a - \frac{i}{\cos\Delta}H(n_x,n_y)_b
\end{equation}
$$

where $H(n_x,n_y)$ is the measured spectral line which is just the real projection of the complex line.

Under the assumption that the region between $s_a$ and $s_b$ is free from non-linearities and coupling
the action $J_z$ does not change between the two positions and

$$
\begin{align}
    |H(1,0)_a| &= |H(1,0)_b| = \sqrt{2J_x} \\
    |V(0,1)_a| &= |V(0,1)_b| = \sqrt{2J_y}
\end{align}
$$

This allows to express the real normalised spectral lines as

$$
\begin{align}
    A(0,n_y)_a &= \frac{H(0,n_y)_a}{\left| H(1,0)_a \right|} = \frac{H(0,n_y)_a}{\left| H(1,0)_b \right|} \\
    B(n_x,0)_a &= \frac{V(n_x,0)_a}{\left| V(0,1)_a \right|} = \frac{V(n_x,0)_a}{\left| V(0,1)_b \right|} 
\end{align}
$$

This can be plugged into the reconstruction formula $\eqref{eq:reconstr_cplx}$

$$
\begin{equation}
    \frac{H^+(n_x,n_y)_a}{H(1,0)_i} = (1-i\tan\Delta)A(n_x,n_y)_a - \frac{i}{\cos\Delta}A(n_x,n_y)_b
\end{equation}
$$

Together with the identity

$$
\begin{equation}
    H(1,0) = \frac{1}{2} \left( H^+(1,0) + {H^-(1,0)}\right) = \frac{1}{2}H^+(1,0)
\end{equation}
$$

because $H^-(1,0) = 0$, one can express $A^+(0,n_y)$ and $B(n_x, 0)$ in terms of normalised real spectral lines

$$
\begin{align}
    2A^+(n_x,n_y)_a = (1-i\tan\Delta)A(n_x,n_y)_a - \frac{i}{\cos\Delta}A(n_x,n_y)_b \\
    2B^+(n_x,n_y)_a = (1-i\tan\Delta)B(n_x,n_y)_a - \frac{i}{\cos\Delta}B(n_x,n_y)_b
\end{align}
$$

Which can now be plugged into $\eqref{eq:normalised_spectral_line_to_rdt_diff}$ and $\eqref{eq:normalised_spectral_line_to_rdt_sum}$
 in order to calculate the amplitude of the coupling RDTs $f_{1001}$ and $f_{1010}$.
The phases of $A_{0.1},\,B_{1,0},\,A_{0,-1},\,B_{-1,0}$ contain the phases of the RDTs:

$$
\begin{align}
  \text{arg}(A_{0,1}) &= -q_{1001} -\varphi_y +\tfrac{\pi}{2} \\
  \text{arg}(B_{1,0}) &= q_{1001} -\varphi_x +\tfrac{\pi}{2} \\
  \text{arg}(A_{0,-1}) &= -q_{1010} +\varphi_y +\tfrac{\pi}{2} \\
  \text{arg}(B_{-1,0}) &= -q_{1010} +\varphi_x +\tfrac{\pi}{2}
\end{align}
$$

where the phase $\frac{\pi}{2}$ comes from the factor $i$ and the phases of the RDTs are defined as

$$
\begin{align}
  q_{1001} &\equiv \text{arg}(f_{1001})\\
  q_{1010} &\equiv \text{arg}(f_{1010})
\end{align}
$$

From the equations for the phases above, one gets two expressions for each RDT phase:

$$
\begin{align}
  q_{1001} &= -\arg{A_{0,1}}-\varphi_y + \tfrac{\pi}{2} & &= \arg{B_{1,0}}+\varphi_x -\tfrac{\pi}{2}\\
  q_{1010} &= -\arg{A_{0,-1}} +\varphi_y + \tfrac{\pi}{2} & &= -\arg{B_{-1,0}}+\varphi_x +\tfrac{\pi}{2}
\end{align}
$$

which can finally be used to calculate the coupling RDTs $f_{1001}$ and $f_{1010}$.


[franchi_emittance_sharing]: https://inspirehep.net/files/14639a62394d4ce17ea972088f685d91
[bazzani_normal_form]: https://inspirehep.net/literature/373560
[bartolini_normal_form]: https://cds.cern.ch/record/333077
[herr_cas]: https://cds.cern.ch/record/1507631
[herr_forest_nf]: https://cds.cern.ch/record/2743949/files/Herr-Forest2020_Chapter_Non-linearDynamicsInAccelerato%20(1).pdf
[tomas_rdt]: https://inspirehep.net/literature/680877