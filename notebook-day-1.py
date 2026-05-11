import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, sci


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():
    g = 1.0
    M = 1.0
    l = 2.0
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    **Hypothèses :**
    - Le booster fait un angle \( \theta \) avec la verticale
    - La force du réacteur a une norme \( f \geq 0 \)
    - L’angle entre l’axe du booster et la force est \( \phi \) (sens trigonométrique)
    - L’angle absolu de la force du réacteur dans le repère est :
      \[
      \alpha = \theta + \phi
      \]
    - La gravité agit selon :
      \[
      \mathbf{F}_g =
      \begin{pmatrix}
      0 \\
      -Mg
      \end{pmatrix}
      \]

    **Expression vectorielle des forces :**
    - Force du réacteur :
    \[
    \mathbf{f}_{\text{réacteur}} =
    \begin{pmatrix}
    -f \sin(\alpha) \\
    f \cos(\alpha)
    \end{pmatrix}
    \]

    - Force totale :
    \[
    \mathbf{F} =
    \mathbf{f}_{\text{réacteur}} + \mathbf{F}_g
    =
    \begin{pmatrix}
    -f \sin(\theta + \phi) \\
    f \cos(\theta + \phi) - Mg
    \end{pmatrix}
    \]

    **Composantes cartésiennes :**
    \[
    F_x = - f \sin(\theta + \phi)
    \]
    \[
    F_y = f \cos(\theta + \phi) - Mg
    \]

    **Conclusion :**
    Les composantes de la force totale appliquée au booster sont :
    \[
    (F_x, F_y) = \big(- f \sin(\theta + \phi),\; f \cos(\theta + \phi) - Mg\big)
    \]
    """)
    return


@app.cell
def _(M, g, np):
    def force_components(f, theta, phi):
        fx = -f * np.sin(theta + phi)
        fy = f * np.cos(theta + phi) - M*g
        return fx, fy

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse


    **Hypothèses :**
    - Position du centre de masse : \( (x(t), y(t)) \)
    - Masse du booster : \( M \)
    - Angle du booster avec la verticale : \( \theta(t) \)
    - Force du réacteur :
      \[
      \mathbf{F}_{r} =
      \begin{pmatrix}
      -f \sin(\theta + \phi) \\
      f \cos(\theta + \phi)
      \end{pmatrix}
      \]
    - Gravité :
      \[
      \mathbf{F}_g =
      \begin{pmatrix}
      0 \\
      -Mg
      \end{pmatrix}
      \]
    - Principe fondamental de la dynamique :
      \[
      M \ddot{\mathbf{r}} = \mathbf{F}_r + \mathbf{F}_g
      \]

    ---

    **Équation vectorielle du mouvement :**
    \[
    M
    \begin{pmatrix}
    \ddot{x} \\
    \ddot{y}
    \end{pmatrix}
    =
    \begin{pmatrix}
    -f \sin(\theta + \phi) \\
    f \cos(\theta + \phi) - Mg
    \end{pmatrix}
    \]

    ---

    **Système d’équations différentielles :**

    \[
    \ddot{x}(t) = -\frac{f}{M} \sin(\theta(t) + \phi)
    \]

    \[
    \ddot{y}(t) = \frac{f}{M} \cos(\theta(t) + \phi) - g
    \]

    ---

    **Conclusion :**
    Le mouvement du centre de masse du booster est gouverné par :
    \[
    \begin{cases}
    \ddot{x} = - \dfrac{f}{M} \sin(\theta + \phi) \\
    \ddot{y} = \dfrac{f}{M} \cos(\theta + \phi) - g
    \end{cases}
    \]
    """)
    return


@app.cell
def _(M, g, np):
    def center_of_mass_acceleration(f, theta, phi):

        ax = -(f / M) * np.sin(theta + phi)
        ay = (f / M) * np.cos(theta + phi) - g

        return ax, ay

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    **Hypothèses :**
    - Le booster est un tube rigide de longueur \( \ell \)
    - Sa masse \( M \) est uniformément répartie
    - On modélise le booster comme une tige mince
    - Le moment d’inertie est calculé autour de son centre de masse

    ---

    ### Formule physique

    Pour une tige uniforme de longueur \( \ell \) et de masse \( M \), le moment d’inertie autour du centre est :

    \[
    J = \frac{1}{12} M \ell^2
    \]

    ---

    ### 📌 Résultat

    \[
    J = \frac{1}{12} M \ell^2
    \]
    """)
    return


@app.cell
def _(M, l):
    J = M * l**2 / 3
    return (J,)


@app.cell(hide_code=True)
def _(J, mo):
    mo.md(rf"""
    For a uniform rod of total length $2\ell$ rotating around its center of mass,

    $$
    J = \frac{{1}}{{12}} M (2\ell)^2 = \frac{{1}}{{3}} M \ell^2.
    $$

    With the chosen constants, this gives $J = {J}$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    **Hypothèses :**
    - Le booster est une tige rigide de longueur \( \ell \)
    - Son centre de masse est au milieu
    - Moment d’inertie :
    \[
    J = \frac{1}{12} M \ell^2
    \]
    - Le booster est soumis à :
      - la gravité
      - la force du réacteur appliquée à la base
    - Angle du booster : \( \theta \) (par rapport à la verticale)
    - Angle de la force du réacteur dans le repère :
      \[
      \alpha = \theta + \phi
      \]

    ---

    ## Principe dynamique

    On utilise la dynamique de rotation  :

    \[
    J \ddot{\theta} = \sum \mathcal{M}_O
    \]

    où les moments sont pris autour du centre de masse.

    ---

    ## Moments des forces

    ### 1. Moment de la gravité

    La gravité agit au centre de masse → elle ne crée **aucun moment autour du centre de masse** :

    \[
    \mathcal{M}_g = 0
    \]

    ---

    ### 2. Moment du réacteur

    La force est appliquée à la base, située à distance \( \ell/2 \) du centre de masse.

    Vecteur position :
    \[
    \mathbf{r} = -\frac{\ell}{2} \mathbf{e}_\theta
    \]

    $\mathbf{e}_\theta = (\sin\theta)\,\mathbf{e}_x + (\cos\theta)\,\mathbf{e}_y$

    Force du réacteur :
    \[
    \mathbf{F}_r =
    \begin{pmatrix}
    -f \sin(\theta + \phi) \\
    f \cos(\theta + \phi)
    \end{pmatrix}
    \]

    Moment scalaire (2D) :
    \[
    \mathcal{M}_r = \mathbf{r} \times \mathbf{F}_r
    \]

    \[
    \mathbf{r} =
    -\frac{\ell}{2}
    \begin{pmatrix}
    \sin\theta \\
    \cos\theta
    \end{pmatrix}
    \]

    \[
    \mathbf{F}_r =
    f
    \begin{pmatrix}
    -\sin(\theta+\phi) \\
    \cos(\theta+\phi)
    \end{pmatrix}
    \]

    \[
    \mathcal{M}_r = r_x F_y - r_y F_x
    \]

    \[
    \mathcal{M}_r =
    \left(-\frac{\ell}{2}\sin\theta\right)\left(f\cos(\theta+\phi)\right)
    -
    \left(-\frac{\ell}{2}\cos\theta\right)\left(f\sin(\theta+\phi)\right)
    \]

    \[
    \mathcal{M}_r = - \frac{\ell}{2} f \sin(\phi)
    \]

    ---

    ## Équation finale

    \[
    J \ddot{\theta} = - \frac{\ell}{2} f \sin(\phi)
    \]

    ---

    ## Forme simplifiée

    \[
    \ddot{\theta} = -\frac{\ell}{2J} f \sin(\phi)
    \]

    En remplaçant \( J \) :

    \[
    \ddot{\theta} = - \frac{6 f}{M \ell} \sin(\phi)
    \]

    ---
    """)
    return


@app.cell
def _(J, l, np):
    def theta_acceleration(f, phi):
        return -(l* f * np.sin(phi))/(2*J)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse
    ### Dimension de l’espace d’état

    On définit les variables d’état :

    \[
    v_x = \dot{x}, \quad v_y = \dot{y}, \quad \omega = \dot{\theta}
    \]

    et les positions :

    \[
    x, \; y, \; \theta
    \]

    ---

    ### Dimension du système

    Le vecteur d’état contient :

    - \( x \)
    - \( y \)
    - \( \theta \)
    - \( v_x \)
    - \( v_y \)
    - \( \omega \)

    Donc :

    \[
    n = 6
    \]

    ---

    ### État du système

    \[
    s =
    \begin{pmatrix}
    x \\
    y \\
    \theta \\
    v_x \\
    v_y \\
    \omega
    \end{pmatrix}
    \in \mathbb{R}^6
    \]

    ---

    ### Dynamique du système

    On utilise la mécanique newtonienne et la dynamique de rotation :

    - \( \dot{x} = v_x \)
    - \( \dot{y} = v_y \)
    - \( \dot{\theta} = \omega \)

    Accélérations :

    \[
    \dot{v}_x = \frac{f}{M}\sin(\theta+\phi)
    \]

    \[
    \dot{v}_y = \frac{f}{M}\cos(\theta+\phi) - g
    \]

    Moment d’inertie :

    \[
    J = \frac{1}{12}M\ell^2
    \]

    Équation de rotation :

    \[
    \dot{\omega} = \frac{\ell}{2J} f \sin(\phi)
    \]

    ---

    ### Fonction dynamique

    \[
    F : \mathbb{R}^6 \times \mathbb{R}^+ \times \mathbb{R} \rightarrow \mathbb{R}^6
    \]

    \[
    F(s,f,\phi) =
    \begin{pmatrix}
    v_x \\
    v_y \\
    \omega \\
    -\frac{f}{M}\sin(\theta+\phi) \\
    \frac{f}{M}\cos(\theta+\phi) - g \\
    -\frac{\ell}{2J} f \sin(\phi)
    \end{pmatrix}
    \]

    ---

    ### Équation d’évolution

    \[
    \dot{s} = F(s,f,\phi)
    \]
    """)
    return


@app.cell
def _(J, M, g, l, np):
    def F(s, f, phi):
        x, vx, y, vy, theta, omega = s

        dx = vx
        dvx = -(f / M) * np.sin(theta + phi)

        dy = vy
        dvy = (f / M) * np.cos(theta + phi) - g

        dtheta = omega
        domega = -(l * f * np.sin(phi)) /(2*J)

        return np.array([dx, dvx, dy, dvy, dtheta, domega])

    return (F,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell
def _(F, sci):
    def redstart_solve(t_span, y0, f_phi):

        def dynamics(t, y):
            f, phi = f_phi(t, y)
            return F(y, f, phi)

        result = sci.solve_ivp(
            dynamics,
            t_span,
            y0,
            dense_output=True,
            rtol=1e-9,
            atol=1e-9
        )

        return result.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    ### 1. Cas étudié

    Dans le cas de la chute libre :
    - \( f = 0 \)
    - \( \phi = 0 \)
    - donc seule la gravité agit

    On a alors :
    \[
    \ddot{y} = -g
    \]

    Conditions initiales :
    \[
    y(0) = 10, \quad \dot{y}(0) = 0
    \]

    On cherche le moment où :
    \[
    y(t) = \ell \quad \text{avec } \ell = 2
    \]

    ---

    ### 2. Solution théorique

    \[
    y(t) = y_0 - \frac{1}{2} g t^2
    \]

    On résout :
    \[
    2 = 10 - \frac{1}{2} t^2
    \]

    \[
    t^2 = 16
    \]

    \[
    t = 4
    \]

    ---
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([0.0, 0.0])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]

        # niveau cible
        y_target = l


        idx = np.argmin(np.abs(y_t - y_target))
        t_cross = t[idx]
        y_cross = y_t[idx]

        plt.figure()
        plt.plot(t, y_t, label=r"$y(t)$")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=l$")

        # ligne verticale détectée
        plt.axvline(t_cross, color="red", ls="--", label=fr"$t \approx {t_cross:.3f}$")

        # point d’intersection
        plt.scatter([t_cross], [y_cross], color="red")

        plt.title("Free Fall (graphical detection)")
        plt.xlabel("time t")
        plt.ylabel("height y")
        plt.grid(True)
        plt.legend()

        return plt.gcf()

    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    ---

    ## 1. Modèle dynamique

    On suppose :
    - \( \theta = 0 \Rightarrow \) poussée verticale
    - \( M = 1 \), \( g = 1 \)

    Équation du mouvement vertical :

    \[
    \ddot{y} = f(t) - g = f(t) - 1
    \]

    ---

    ## 2. Conditions initiales et finales

    ### État initial :
    \[
    y(0) = 10, \quad \dot{y}(0) = -2
    \]

    ### État final :
    \[
    y(5) = 1, \quad \dot{y}(5) = 0
    \]

    La forme de l'accélération $\ddot{y}$ est directement déterminée par la loi de commande $f(t)$ selon la relation

    $$\ddot{y} = f(t) - g$$

    Ainsi, imposer une structure particulière à $f(t)$ revient à imposer la même structure à $\ddot{y}(t)$, à une translation verticale près (due à la gravité).

    Le choix de la commande $f(t)$ détermine entièrement l’évolution temporelle de l’accélération du système. Par intégrations successives, cette commande permet ensuite d’obtenir la vitesse $\dot{y}(t)$ ainsi que la position $y(t)$. Ainsi, pour des conditions initiales données, la loi de commande $f(t)$ fixe de manière univoque la dynamique et la trajectoire du système.

    De manière équivalente, il est possible de supposer directement une forme analytique de la trajectoire $y(t)$ afin d’en déduire la commande $f(t)$. Étant donné que le système est soumis à quatre conditions initiales ou aux limites, on peut modéliser $y(t)$ par un polynôme de degré trois :

    \[
    y(t)=a_0+a_1 t+a_2 t^2+a_3 t^3
    \]

    Les coefficients du polynôme sont alors déterminés à partir des conditions imposées sur la position et la vitesse aux instants initial et final.

    ---


    ## 3. Choix de la trajectoire

    On impose une trajectoire polynomiale cubique :

    \[
    y(t) = a t^3 + b t^2 + c t + d
    \]

    ---

    ## 4. Détermination des coefficients

    À partir des conditions :

    - \( y(0)=10 \Rightarrow d=10 \)
    - \( \dot{y}(0)=-2 \Rightarrow c=-2 \)
    - \( y(5)=1 \)
    - \( \dot{y}(5)=0 \)

    On obtient :

    \[
    a = \frac{8}{125}, \quad b = -\frac{7}{25}, \quad c = -2, \quad d = 10
    \]

    ---

    ## 5. Trajectoire obtenue

    \[
    y(t)=\frac{8}{125}t^3 - \frac{7}{25}t^2 - 2t + 10
    \]

    ---

    ## 6. Accélération

    \[
    \ddot{y}(t) = \frac{48}{125}t - \frac{14}{25}
    \]

    ---

    ## 7. Loi de commande

    Comme :
    \[
    \ddot{y} = f(t) - 1
    \]

    on obtient :

    \[
    f(t) = \frac{48}{125}t + \frac{11}{25}
    \]

    ---
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    def controlled_landing():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        def f_phi(t, y):
            f = 0.44 + 0.384 * t
            phi = 0.0
            return np.array([f, phi])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)
        s = sol(t)

        x_t = s[0]
        vx_t = s[1]
        y_t = s[2]
        vy_t = s[3]
        theta_t = s[4]
        omega_t = s[5]

        f_t = 0.44 + 0.384 * t

        plt.figure()
        plt.plot(t, y_t, label=r"$y(t)$")
        plt.plot(t, l/2 * np.ones_like(t), color="grey", ls="--", label=r"$y=1$")
        plt.title("Controlled Landing: height")
        plt.xlabel("time t")
        plt.ylabel("height y")
        plt.grid(True)
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(t, vy_t, label=r"$\dot{y}(t)$")
        plt.axhline(0, color="grey", ls="--")
        plt.title("Controlled Landing: vertical velocity")
        plt.xlabel("time t")
        plt.ylabel("vertical velocity")
        plt.grid(True)
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(t, f_t, label=r"$f(t)$")
        plt.title("Controlled Landing: thrust")
        plt.xlabel("time t")
        plt.ylabel("force f")
        plt.grid(True)
        plt.legend()
        plt.show()

        print("Final state at t=5:")
        print("x(5)      =", sol(5.0)[0])
        print("vx(5)     =", sol(5.0)[1])
        print("y(5)      =", sol(5.0)[2])
        print("vy(5)     =", sol(5.0)[3])
        print("theta(5)  =", sol(5.0)[4])
        print("omega(5)  =", sol(5.0)[5])

        return sol

    sol_controlled = controlled_landing()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.function
def world(view_box, *objects):
    x_min, x_max, y_min, y_max = view_box

    width = x_max - x_min
    height = y_max - y_min

    # SVG has y going downward by default.
    # We use a transform scale(1,-1) to make y go upward.
    svg_objects = "\n".join(objects)

    return f"""
    <svg viewBox="{x_min} {-y_max} {width} {height}" width="300" height="300"
         xmlns="http://www.w3.org/2000/svg">

        <g transform="scale(1,-1)">
            <rect x="{x_min}" y="{y_min}" width="{width}" height="{height}"
                  fill="skyblue"/>

            <rect x="{x_min}" y="{y_min}" width="{width}" height="{0 - y_min}"
                  fill="sandybrown"/>

            <rect x="-1" y="0" width="2" height="0.1"
                  fill="green"/>

            <line x1="{x_min}" y1="0" x2="{x_max}" y2="0"
                  stroke="black" stroke-width="0.02"/>

            {svg_objects}
        </g>
    </svg>
    """


@app.cell
def _(mo):
    mo.hstack(
        [
            mo.Html(world([-3, 3, -2, 4])),

            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    '<rect x="-1" y="0" width="2" height="2" fill="black"/>'
                )
            ),

            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    '<rect x="-3" y="2" width="2" height="2" fill="red"/>',
                    '<rect x="1" y="2" width="2" height="2" fill="blue"/>'
                )
            )
        ],
        justify="space-around"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.function
def polygon(points, fill, stroke="black", stroke_width=0.02):
    points_str = " ".join([f"{x},{y}" for x, y in points])
    return f"""
    <polygon points="{points_str}"
             fill="{fill}"
             stroke="{stroke}"
             stroke-width="{stroke_width}"/>
    """


@app.cell
def _(M, g, l, np):
    def booster(x, y, theta, f, phi):
        body_width = 0.2
        flame_half_width = 0.09

        def flame_scale(thrust):
            if M * g == 0:
                return 0.0
            return max(thrust / (M * g), 0.0)

        body = f"""
        <rect x="{-body_width / 2}" y="{-l}" width="{body_width}" height="{2 * l}"
              fill="lightgrey" stroke="black" stroke-width="0.02" rx="0.04"/>
        """
        flame = polygon(
            [(-flame_half_width, -l), (flame_half_width, -l), (0.0, -1.5 * l)],
            fill="orange",
            stroke="red",
        )

        return f"""
        <g transform="translate({x},{y})">
            <g transform="rotate({np.degrees(theta)})">
                {body}
                <g transform="rotate({np.degrees(phi)},0,{-l})">
                    <g transform="translate(0,{-l})">
                        <g transform="scale(1,{flame_scale(f)})">
                            <g transform="translate(0,{l})">
                                {flame}
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
        """

    return (booster,)


@app.cell
def _(M, booster, g, l, mo, np):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell
def _(M, g, l, np):
    def booster_anim(x, y, theta, f, phi, T=5.0, fps=30.0):
        body_width = 0.2
        flame_half_width = 0.09
        dt = 1.0 / fps
        t_samples = [t for t in np.arange(0.0, T + dt, dt) if t / T <= 1.0]
        key_times = "; ".join(str(t / T) for t in t_samples)

        def sampled_values(fun):
            return [fun(t) for t in t_samples]

        def flame_scale(thrust):
            if M * g == 0:
                return 0.0
            return max(thrust / (M * g), 0.0)

        x_values = sampled_values(x)
        y_values = sampled_values(y)
        theta_values = sampled_values(theta)
        phi_values = sampled_values(phi)
        force_values = sampled_values(f)

        translate_values = "; ".join(
            f"{x_t},{y_t}" for x_t, y_t in zip(x_values, y_values)
        )
        rotation_values = "; ".join(
            f"{np.degrees(theta_t)},0,0" for theta_t in theta_values
        )
        flame_rotation_values = "; ".join(
            f"{np.degrees(phi_t)},0,{-l}" for phi_t in phi_values
        )
        scale_values = "; ".join(
            f"1,{flame_scale(thrust)}" for thrust in force_values
        )

        body = f"""
        <rect x="{-body_width / 2}" y="{-l}" width="{body_width}" height="{2 * l}"
              fill="lightgrey" stroke="black" stroke-width="0.02" rx="0.04"/>
        """
        flame = polygon(
            [(-flame_half_width, -l), (flame_half_width, -l), (0.0, -1.5 * l)],
            fill="orange",
            stroke="red",
        )

        return f"""
        <g>
            <animateTransform
                attributeName="transform"
                type="translate"
                values="{translate_values}"
                keyTimes="{key_times}"
                dur="{T}s"
                repeatCount="indefinite"/>
            <g>
                <animateTransform
                    attributeName="transform"
                    type="rotate"
                    values="{rotation_values}"
                    keyTimes="{key_times}"
                    dur="{T}s"
                    repeatCount="indefinite"/>
                {body}
                <g>
                    <animateTransform
                        attributeName="transform"
                        type="rotate"
                        values="{flame_rotation_values}"
                        keyTimes="{key_times}"
                        dur="{T}s"
                        repeatCount="indefinite"/>
                    <g transform="translate(0,{-l})">
                        <g>
                            <animateTransform
                                attributeName="transform"
                                type="scale"
                                values="{scale_values}"
                                keyTimes="{key_times}"
                                dur="{T}s"
                                repeatCount="indefinite"/>
                            <g transform="translate(0,{l})">
                                {flame}
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
        """

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, mo, np):
    def booster_anim_0():
        T = 5.0

        def x(t):
            return -l / 2 + l * (t / T)

        def y(t):
            return l / 2 + l / 2 * (t / T)

        def theta(t):
            return (t / T) * 2 * np.pi

        def f(t):
            return M * g * (t / T)

        def phi(t):
            return 2 * np.pi * (t / T)

        return booster_anim(x, y, theta, f, phi, T=T)

    mo.center(
        mo.Html(
            world([-3, 3, -2, 4], booster_anim_0())
        )
    )
    return


@app.cell
def _(booster, mo):
    def display_booster_at_time(sol, f_phi, t, view_box=[-3, 3, -6, 12]):
        s = sol(t)
        x, vx, y, vy, theta, omega = s
        f, phi = f_phi(t, s)

        return mo.Html(
            world(
                view_box,
                booster(x, y, theta, f, phi)
            )
        )

    return (display_booster_at_time,)


@app.cell
def _(display_booster_at_time, mo, np, redstart_solve):
    def free_fall_solution():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([0.0, 0.0])

        sol = redstart_solve(t_span, y0, f_phi)

        return sol, f_phi

    sol_free, f_phi_free = free_fall_solution()

    mo.hstack(
        [
            display_booster_at_time(sol_free, f_phi_free, 0.0),
            display_booster_at_time(sol_free, f_phi_free, 2.5),
            display_booster_at_time(sol_free, f_phi_free, 5.0),
        ],
        justify="space-around"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell
def _(M, g, np, redstart_solve):
    def scenario_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([0.0, 0.0])

        sol = redstart_solve(t_span, y0, f_phi)
        return sol, f_phi

    def scenario_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([M * g, 0.0])

        sol = redstart_solve(t_span, y0, f_phi)
        return sol, f_phi

    def scenario_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([M * g, np.pi / 8])

        sol = redstart_solve(t_span, y0, f_phi)
        return sol, f_phi

    def scenario_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([0.44 + 0.384 * t, 0.0])

        sol = redstart_solve(t_span, y0, f_phi)
        return sol, f_phi

    return scenario_1, scenario_2, scenario_3, scenario_4


@app.cell
def _(booster_anim, l, mo, np):
    def scenario_animation(sol, f_phi, title, T=5.0, view_box=[-3, 3, -6, 12]):
        if view_box is None:
            t = np.linspace(0.0, T, 250)
            states = sol(t)
            x_values = states[0]
            y_values = states[2]
            view_box = [
                float(np.min(x_values) - 2.5 * l),
                float(np.max(x_values) + 2.5 * l),
                -1.0,
                float(max(4.0, np.max(y_values) + 2.5 * l)),
            ]

        def x(t):
            return float(sol(t)[0])

        def y(t):
            return float(sol(t)[2])

        def theta(t):
            return float(sol(t)[4])

        def f(t):
            return float(f_phi(t, sol(t))[0])

        def phi(t):
            return float(f_phi(t, sol(t))[1])

        return mo.vstack(
            [
                mo.md(f"### {title}"),
                mo.center(
                    mo.Html(
                        world(
                            view_box,
                            booster_anim(x, y, theta, f, phi, T=T),
                        )
                    )
                ),
            ]
        )

    return (scenario_animation,)


@app.cell
def _(mo, scenario_1, scenario_2, scenario_3, scenario_4, scenario_animation):
    sol1, f_phi1 = scenario_1()
    sol2, f_phi2 = scenario_2()
    sol3, f_phi3 = scenario_3()
    sol4, f_phi4 = scenario_4()

    mo.vstack(
        [
            scenario_animation(sol1, f_phi1, "Scenario 1: Free fall"),
            scenario_animation(sol2, f_phi2, "Scenario 2: f = Mg, phi = 0"),
            scenario_animation(sol3, f_phi3, "Scenario 3: f = Mg, phi = pi/8"),
            scenario_animation(sol4, f_phi4, "Scenario 4: Controlled landing"),
        ]
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
