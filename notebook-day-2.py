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

    return np, plt, sci, scipy


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
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
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
    return (J,)


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
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
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
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

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
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
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

    return animate_transform, svg, transform


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
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

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center() 
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    On cherche les configurations d’équilibre, c’est-à-dire lorsque :
    \[
    \ddot{x} = 0, \quad \ddot{y} = 0, \quad \ddot{\theta} = 0
    \]

    ---

    ### Équations du système

    \[
    \begin{aligned}
    M \ddot{x} & = -f \sin(\theta + \phi) \\
    M \ddot{y} & = f \cos(\theta + \phi) - Mg \\
    J \ddot{\theta} & = - f \frac{\ell}{2} \sin \phi
    \end{aligned}
    \]

    ---

    ### Conditions d’équilibre

    #### 1. Équation selon \(x\)

    \[
    -f \sin(\theta + \phi) = 0
    \quad \Rightarrow \quad \sin(\theta + \phi) = 0
    \]

    Donc :
    \[
    \theta + \phi = k\pi, \quad k \in \mathbb{Z}
    \]

    ---

    #### 2. Équation selon \(y\)

    \[
    f \cos(\theta + \phi) - Mg = 0
    \quad \Rightarrow \quad f \cos(\theta + \phi) = Mg
    \]

    ---

    #### 3. Équation de rotation

    \[
    - f \frac{\ell}{2} \sin \phi = 0
    \quad \Rightarrow \quad \sin \phi = 0
    \]

    Donc :
    \[
    \phi = m\pi, \quad m \in \mathbb{Z}
    \]

    ---

    ### Combinaison des conditions

    - De \(\phi = m\pi\), on a \(\sin\phi = 0\)
    - Et \(\theta + \phi = k\pi\)

    Donc :
    \[
    \cos(\theta + \phi) = \cos(k\pi) = (-1)^k
    \]

    Substitution dans l’équation verticale :
    \[
    f (-1)^k = Mg
    \]

    ---

    ### Contrainte : \(f > 0\)

    - Si \(k\) est pair : \(f = Mg\)
    - Si \(k\) est impair : \(f = -Mg\) (impossible)

    Donc :
    \[
    k = 2n \quad \Rightarrow \quad f = Mg
    \]

    ---

    ### Solutions admissibles

    \[
    \theta + \phi = 2n\pi, \quad \phi = m\pi, \quad f = Mg
    \]

    Avec les contraintes :
    \[
    |\theta| < \frac{\pi}{2}, \quad |\phi| < \frac{\pi}{2}
    \]

    On obtient :
    \[
    \phi = 0 \quad \Rightarrow \quad \theta = 0
    \]

    ---

    ### Résultat final

    - Configuration d’équilibre :
    \[
    \theta = 0, \quad \phi = 0
    \]

    - Entrée correspondante :
    \[
    f = Mg
    \]

    ---

    ### Interprétation

    À l’équilibre :
    - La force \(f\) compense le poids \(Mg\)
    - Le système est aligné verticalement
    - Aucun couple n’est appliqué (\(\phi = 0\))
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    On introduit les variables d’erreur $\Delta x$, $\Delta y$, $\Delta \theta$, $\Delta f$ et $\Delta \phi$ par rapport à l’équilibre :
    \[
    \theta_e = 0,\quad \phi_e = 0,\quad f_e = Mg
    \]

    On définit :
    \[
    x = x_e + \Delta x,\quad y = y_e + \Delta y,\quad \theta = \Delta \theta,\quad f = Mg + \Delta f,\quad \phi = \Delta \phi
    \]

    ---

    ## 1. Modèle non linéaire

    \[
    \begin{aligned}
    M \ddot{x} &= -f \sin(\theta + \phi) \\
    M \ddot{y} &= f \cos(\theta + \phi) - Mg \\
    J \ddot{\theta} &= - f \frac{\ell}{2} \sin \phi
    \end{aligned}
    \]

    ---

    ## 2. Approximation linéaire

    Au voisinage de l’équilibre :
    \[
    \sin(\theta+\phi) \approx \theta + \phi,\quad
    \cos(\theta+\phi) \approx 1,\quad
    \sin\phi \approx \phi
    \]

    On néglige tous les termes d’ordre supérieur.

    ---

    ## 3. Dynamique linéarisée

    ### Direction $x$

    \[
    M \Delta \ddot{x} = -(Mg + \Delta f)(\Delta \theta + \Delta \phi)
    \]

    En négligeant les termes d’ordre supérieur :
    \[
    M \Delta \ddot{x} = -Mg(\Delta \theta + \Delta \phi)
    \]

    \[
    \boxed{\Delta \ddot{x} = -g(\Delta \theta + \Delta \phi)}
    \]

    ---

    ### Direction $y$

    \[
    M \Delta \ddot{y} = (Mg + \Delta f) - Mg
    \]

    \[
    \boxed{\Delta \ddot{y} = \frac{1}{M}\Delta f}
    \]

    ---

    ### Dynamique de rotation

    \[
    J \Delta \ddot{\theta} = -(Mg + \Delta f)\frac{\ell}{2}\Delta \phi
    \]

    En négligeant les termes d’ordre supérieur :
    \[
    J \Delta \ddot{\theta} = -Mg \frac{\ell}{2}\Delta \phi
    \]

    \[
    \boxed{\Delta \ddot{\theta} = -\frac{Mg\ell}{2J}\Delta \phi}
    \]

    ---

    ## 4. Modèle linéarisé final

    \[
    \boxed{
    \begin{aligned}
    \Delta \ddot{x} &= -g(\Delta \theta + \Delta \phi) \\
    \Delta \ddot{y} &= \frac{1}{M}\Delta f \\
    \Delta \ddot{\theta} &= -\frac{Mg\ell}{2J}\Delta \phi
    \end{aligned}
    }
    \]

    ---

    ## 5. Interprétation

    - Le mouvement horizontal dépend de $\Delta \theta + \Delta \phi$
    - Le mouvement vertical dépend uniquement de $\Delta f$
    - La rotation dépend uniquement de $\Delta \phi$
    - Le système linéarisé est partiellement découplé
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse
    ### 1. Vecteurs d’état et d’entrée

    On choisit le vecteur d’état :
    \[
    X =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta y \\
    \Delta \dot{y} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}
    \]

    et le vecteur d’entrée :
    \[
    U =
    \begin{bmatrix}
    \Delta f \\
    \Delta \phi
    \end{bmatrix}
    \]

    ---

    ### 2. Modèle linéarisé

    \[
    \boxed{
    \begin{aligned}
    \Delta \dot{x} &= \Delta \dot{x}
    &\qquad
    \Delta \ddot{x} &= -g(\Delta \theta + \Delta \phi) \\[6pt]
    \Delta \dot{y} &= \Delta \dot{y}
    &\qquad
    \Delta \ddot{y} &= \frac{1}{M}\Delta f \\[6pt]
    \Delta \dot{\theta} &= \Delta \dot{\theta}
    &\qquad
    \Delta \ddot{\theta} &= -\frac{Mg\ell}{2J}\Delta \phi
    \end{aligned}
    }
    \]


    \[
    \begin{bmatrix}
    \Delta \dot{x} \\
    \Delta \ddot{x} \\
    \Delta \dot{y} \\
    \Delta \ddot{y} \\
    \Delta \dot{\theta} \\
    \Delta \ddot{\theta}
    \end{bmatrix} =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta y \\
    \Delta \dot{y} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}
    +
    \begin{bmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    \frac{1}{M} & 0 \\
    0 & 0 \\
    0 & -\frac{Mg\ell}{2J}
    \end{bmatrix}
    \begin{bmatrix}
    \Delta f \\
    \Delta \phi
    \end{bmatrix}
    \]


    ---

    ### 3. Forme espace d’état

    On écrit :
    \[
    \dot{X} = AX + BU
    \]

    ---

    ## 4. Matrice A

    \[
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}
    \]

    ---

    ### 5. Matrice B

    \[
    B =
    \begin{bmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    \frac{1}{M} & 0 \\
    0 & 0 \\
    0 & -\frac{Mg\ell}{2J}
    \end{bmatrix}
    \]

    ---
    """)
    return


@app.cell
def _(J, M, g, l, np):
    A = np.array([
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, -g, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0]
    ])

    B = np.array([
        [0, 0],
        [0, -g],
        [0, 0],
        [1/M, 0],
        [0, 0],
        [0, -(M*g*l)/(2*J)]
    ])
    return A, B


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    ### 1. Rappel du modèle linéarisé

    On considère le système :

    \[
    \begin{aligned}
    \Delta \ddot{x} &= -g(\Delta \theta + \Delta \phi) \\
    \Delta \ddot{y} &= \frac{1}{M}\Delta f \\
    \Delta \ddot{\theta} &= -\frac{Mg\ell}{2J}\Delta \phi
    \end{aligned}
    \]

    ---

    ### 2. Analyse de stabilité

    On observe que :

    - La dynamique en $\Delta x$ dépend de $\Delta \theta$ et $\Delta \phi$
    - La dynamique en $\Delta \theta$ dépend de $\Delta \phi$
    - La dynamique en $\Delta y$ dépend uniquement de $\Delta f$

    ---

    ### 3. Nature des dynamiques

    #### Direction verticale
    \[
    \Delta \ddot{y} = \frac{1}{M}\Delta f
    \]

    - système de type double intégrateur
    - aucune force de rappel naturelle
    - donc **pas asymptotiquement stable sans contrôle**

    ---

    #### Rotation
    \[
    \Delta \ddot{\theta} = -\frac{Mg\ell}{2J}\Delta \phi
    \]

    - dépend uniquement de l’entrée $\Delta \phi$
    - pas de terme de retour en $\theta$
    - donc **pas de stabilité interne**

    ---

    #### Direction horizontale
    \[
    \Delta \ddot{x} = -g(\Delta \theta + \Delta \phi)
    \]

    - dépend des variables angulaires
    - mais ces variables ne sont pas stabilisées dynamiquement par le système

    ---

    ### 4. Étude de la stabilité (Analyse mathématique)

    En annulant le vecteur d'entrée $U$, le système se ramène à son équation homogène :

    \[
    \dot{X} = AX
    \]

    On cherche les valeurs propres de la matrice \(A\) en calculant :
    \[
    \det(\lambda I - A)
    \]

    ---

    ## 1. Matrice \(A\)

    \[
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}
    \]

    ---

    ## 2. Calcul de \( \lambda I - A \)

    \[
    \lambda I - A =
    \begin{bmatrix}
    \lambda & -1 & 0 & 0 & 0 & 0 \\
    0 & \lambda & 0 & 0 & g & 0 \\
    0 & 0 & \lambda & -1 & 0 & 0 \\
    0 & 0 & 0 & \lambda & 0 & 0 \\
    0 & 0 & 0 & 0 & \lambda & -1 \\
    0 & 0 & 0 & 0 & 0 & \lambda
    \end{bmatrix}
    \]

    On remarque que la matrice \( \lambda I - A \) est triangulaire supérieure.

    Par conséquent, son déterminant est le produit de ses éléments diagonaux :

    \[
    \Delta = \det(\lambda I - A) = \lambda^6
    \]

    Ainsi, les valeurs propres de \(A\) sont données par les racines du polynôme caractéristique :

    \[
    P(\lambda) = \lambda^6
    \]

    ---


    Donc :

    \[
    \lambda(A) = \{0,0,0,0,0,0\}
    \]

    Ainsi :
    - aucune valeur propre à partie réelle strictement négative
    - absence de décroissance exponentielle

    ---

    ### 5. Conclusion

    Le système linéarisé autour de l’équilibre :

    \[
    \boxed{\text{n’est pas asymptotiquement stable en boucle ouverte}}
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    On étudie la contrôlabilité du système linéarisé :

    \[
    \dot{X} = AX + BU
    \]

    avec :
    \[
    X =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta y \\
    \Delta \dot{y} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}
    \quad
    U =
    \begin{bmatrix}
    \Delta f \\
    \Delta \phi
    \end{bmatrix}
    \]



    On considère le système linéarisé :

    \[
    \dot{X} = AX + BU
    \]

    avec \(X \in \mathbb{R}^6\), \(U \in \mathbb{R}^2\).

    ---

    ## 1. Critère de Kalman

    Le système est contrôlable si et seulement si :

    \[
    \mathrm{rank}(\mathcal{C}) = 6
    \quad \text{avec} \quad
    \mathcal{C} = \begin{bmatrix}
    B & AB & A^2B & A^3B & A^4B & A^5B
    \end{bmatrix}
    \]
    On a :
    \[
    A = \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}
    \]
    Donc :
    \[
    A^2 = \begin{bmatrix}
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 0 & 0 & -g \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}
    A^3 = \begin{bmatrix}
    0 & 0 & 0 & 0 & 0 & -g \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}
    A^4 = \begin{bmatrix}
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}
    \]


    D'ou :
    \[
    \mathcal{C} = \begin{bmatrix}
    B & AB & A^2B & A^3B & A^4B & A^5B
    \end{bmatrix}
    \]
    \[
    C = \begin{bmatrix} \begin{bmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    \frac{1}{M} & 0 \\
    0 & 0 \\
    0 & -\frac{Mg\ell}{2J}
    \end{bmatrix}
    \begin{bmatrix}
    0 & -g \\
    0 & 0 \\
    \frac{1}{M} & 0 \\
    0 & 0 \\
    0 & -\frac{Mg\ell}{2J} \\
    0 & 0
    \end{bmatrix}
    \begin{bmatrix}
    0 & 0 \\
    0 & \frac{g^2 M \ell}{2J} \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0
    \end{bmatrix}
    \begin{bmatrix}
    0 & \frac{g^2\ell M}{2J} \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0
    \end{bmatrix}
    \begin{bmatrix}
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0
    \end{bmatrix}
    \begin{bmatrix}
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0
    \end{bmatrix}
    \end{bmatrix}
    \]

    La matrice de contrôlabilité $\mathcal{C}$ possède 6 colonnes linéairement indépendantes, ce qui implique que :
    \[\mathrm{rank}(\mathcal{C}) = 6\]
    Le système linéarisé est donc complètement contrôlable au sens de Kalman
    """)
    return


@app.cell
def _(A, B):
    import sympy as sp

    n = A.shape[0]  
    A_sym = sp.Matrix(A)
    B_sym = sp.Matrix(B)

    C = B_sym

    for i in range(1, 6):
        col_block = (A_sym**i) * B_sym
        C = C.row_join(col_block)

    print("Matrice de contrôlabilité C :")
    sp.pprint(C)

    print("\nRang de la matrice C :")
    print(C.rank())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    On ne garde que les variables latérales :

    \[
    X =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}
    \]

    et on fixe :
    \[
    f = Mg \quad \Rightarrow \quad \Delta f = 0
    \]

    Donc l’unique entrée est :
    \[
    U = \Delta \phi
    \]

    ---

    ## 1. Modèle réduit

    À partir du modèle linéarisé :

    \[
    \begin{aligned}
    \Delta \ddot{x} &= -g(\Delta \theta + \Delta \phi) \\
    \Delta \ddot{\theta} &= -\frac{Mg\ell}{2J}\Delta \phi
    \end{aligned}
    \]

    ---

    ## 2. Forme état-espace

    On pose :

    \[
    X =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}
    \]

    ---

    ## 3. Matrice \(A\)

    \[
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix}
    \]

    ---

    ## 4. Matrice \(B\)

    L’entrée est uniquement \(\Delta \phi\) :

    \[
    B =
    \begin{bmatrix}
    0 \\
    -g \\
    0 \\
    -\frac{Mg\ell}{2J}
    \end{bmatrix}
    \]

    ---

    ## 5. Test de contrôlabilité

    On forme :

    \[
    \mathcal{C} = \begin{bmatrix}
    B & AB & A^2B & A^3B
    \end{bmatrix}
    \]

    ---

    ## 6. Calcul des directions

    ### \(B\)

    \[
    B =
    \begin{bmatrix}
    0 \\
    -g \\
    0 \\
    -\frac{Mg\ell}{2J}
    \end{bmatrix}
    \]

    ---

    ### \(AB\)

    \[
    AB =
    \begin{bmatrix}
    -g \\
    0 \\
    -\frac{Mg\ell}{2J} \\
    0
    \end{bmatrix}
    \]

    ---

    ### \(A^2B\)

    \[
    A^2B =
    \begin{bmatrix}
    0 \\
    g\frac{Mg\ell}{2J} \\
    0 \\
    0
    \end{bmatrix}
    \]

    ---

    ### \(A^3B\)

    \[
    A^3B =
    \begin{bmatrix}
    g\frac{Mg\ell}{2J} \\
    0 \\
    0 \\
    0
    \end{bmatrix}
    \]

    ---

    ## 7. Matrice de contrôlabilité

    Les vecteurs :

    \[
    B,\ AB,\ A^2B,\ A^3B
    \]

    génèrent successivement :

    - vitesse et position en \(x\)
    - angle et vitesse en \(\theta\)

    ---

    ## 8. Rang

    On obtient 4 vecteurs linéairement indépendants :

    \[
    \boxed{\mathrm{rank}(\mathcal{C}) = 4}
    \]

    ---

    ## 9. Conclusion

    \[
    \boxed{\text{Le système latéral réduit est complètement contrôlable}}
    \]

    ---

    ## 10. Interprétation

    - Une seule entrée \(\Delta \phi\) suffit à piloter :
      - position horizontale \(x\)
      - angle \(\theta\)
    - Le système est une **chaîne d’intégrateurs couplés**
    - Toute dynamique est accessible via propagation de \(A\)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse
    Avec $\Delta\phi = 0$ (pas de contrôle), les équations se simplifient :\
    1. $\dot{\Delta\omega} = -3 \times 0 = 0$ → $\Delta\omega(t) = \Delta\omega(0) = 0$ (pas de couple = pas d'accélération angulaire)
    2. $\dot{\Delta\theta} = \Delta\omega = 0$ → $\Delta\theta(t) = \Delta\theta(0) = \pi/4$ (l'angle ne bouge pas)
    3. $\dot{\Delta v_x} = -\Delta\theta = -\pi/4$ → $\Delta v_x(t) = -(\pi/4) \cdot t$ (accélération horizontale constante)
    4. $\dot{\Delta x} = \Delta v_x$ → $\Delta x(t) = -(\pi/4) \cdot t^2/2$ (dérive quadratique)
    """)
    return


@app.cell
def _(J, M, g, l, np, plt, sci):
    A_lat = np.array([
        [0, 1, 0, 0],
        [0, 0, -g, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ])

    B_lat = np.array([
        [0],
        [-g],
        [0],
        [-M*g*l/ (2*J)],
    ])
    def sim_linear_lat(A, B, x0, K_ctrl, t_span, t_eval):
        def rhs(t, x):
            u = -K_ctrl @ x
            return (A @ x + B @ u).flatten()
        r = sci.solve_ivp(rhs, t_span, x0, t_eval=t_eval, rtol=1e-10, atol=1e-10)
        return r.t, r.y

    t_eval = np.linspace(0, 20, 1000)
    x0_ff = [0.0, 0.0, np.pi/4, 0.0]  
    K_zero = np.zeros((1, 4))

    t_ff, y_ff = sim_linear_lat(A_lat, B_lat, x0_ff, K_zero, [0, 20], t_eval)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(t_ff, y_ff[0]); axes[0].set_title(r"$\Delta x(t)$"); axes[0].grid(True)
    axes[0].set_xlabel("t (s)")
    axes[1].plot(t_ff, y_ff[2]); axes[1].set_title(r"$\Delta	\beta(t)$"); axes[1].grid(True)
    axes[1].set_xlabel("t (s)")
    plt.tight_layout()
    plt.show()
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    C'est tout à fait cohérent : avec le booster incliné à 45° sans correction, la composante latérale de la poussée (ou le couplage de la gravité) agit comme une accélération constante. Puisque l'angle reste figé, la vitesse horizontale augmente linéairement et la position dérive de façon parabolique.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    On considère le système réduit (seulement dynamique latérale + rotation) :

    \[
    \ddot{x} = -g(\theta + \phi), \qquad
    \ddot{\theta} = -\alpha \phi
    \quad \text{avec} \quad \alpha = \frac{Mg\ell}{2J}
    \]

    et la loi de commande :

    \[
    \phi(t) = -K
    \begin{bmatrix}
    x \\ \dot{x} \\ \theta \\ \dot{\theta}
    \end{bmatrix}
    =
    -(k_3 \theta + k_4 \dot{\theta})
    \]

    (car \(k_1=k_2=0\)).

    ---

    # 1. Idée de conception

    On veut uniquement contrôler \(\theta\), donc on impose un comportement de type :

    \[
    \ddot{\theta} + 2\zeta\omega_n \dot{\theta} + \omega_n^2 \theta = 0
    \]

    objectif :
    - convergence en ~20 s
    - pas de dépassement excessif
    - rester dans \(|\theta| < \pi/2\)

    ---

    # 2. Choix des dynamiques désirées

    On prend une dynamique lente mais stable :

    \[
    \omega_n = 0.2 \ \text{rad/s}, \quad \zeta = 1
    \]

    Donc :

    \[
    \ddot{\theta} + 0.4 \dot{\theta} + 0.04 \theta = 0
    \]

    ---

    # 3. Lien avec le système physique

    On a :

    \[
    \ddot{\theta} = -\alpha \phi
    \]

    et :

    \[
    \phi = -(k_3 \theta + k_4 \dot{\theta})
    \]

    Donc :

    \[
    \ddot{\theta} = \alpha (k_3 \theta + k_4 \dot{\theta})
    \]

    ---

    # 4. Identification des gains

    On veut :

    \[
    \alpha k_3 = -0.04, \qquad \alpha k_4 = -0.4
    \]

    Donc :

    \[
    k_3 = -\frac{0.04}{\alpha}, \qquad
    k_4 = -\frac{0.4}{\alpha}
    \]

    ---

    # 5. Matrice de gain finale

    \[
    \boxed{
    K =
    \begin{bmatrix}
    0 & 0 & -\frac{0.04}{\alpha} & -\frac{0.4}{\alpha}
    \end{bmatrix}
    }
    \]

    ---

    # 6. Intuition du réglage

    - \(k_3\) règle la raideur (retour vers 0)
    - \(k_4\) règle l’amortissement (évite oscillations)
    - plus \(|k_3|\) est grand → convergence plus rapide
    - plus \(|k_4|\) est grand → système plus stable mais lent

    ---

    # 7. Vérification comportementale

    ### Angle :
    - décroissance exponentielle
    - retour vers zéro en ~20 s

    ### Entrée \(\phi\) :
    - reste bornée si gains raisonnables
    - respecte \(|\phi| < \pi/2\)

    ---

    # 8. Attention importante (point critique)

    La dynamique en \(x\) devient :

    \[
    \ddot{x} = -g(\theta + \phi)
    \]

    Donc :
    - \(x\) peut dériver
    - mais ce n’est pas pénalisé ici

    ---

    # 9. Stabilité du système fermé

    Sous ce contrôle :

    - le sous-système \((\theta, \dot{\theta})\) devient **linéaire stable (Hurwitz)**
    - donc il est **asymptotiquement stable en rotation**

    Mais :

    \[
    \boxed{\text{le système complet n’est pas globalement stable à cause de } x}
    \]

    ---

    # 10. Conclusion finale

    - ✔ Sous-système angulaire : asymptotiquement stable
    - ❌ Système complet : pas globalement stable (drift en \(x\))
    - ✔ Objectif principal atteint : stabilisation de \(\theta\)

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    On considère le système réduit :

    \[
    X =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix},
    \qquad
    \Delta \phi = -K_{pp} X
    \]

    ---

    ## 1. Modèle sous forme état

    À partir de la dynamique linéarisée :

    \[
    \begin{aligned}
    \Delta \ddot{x} &= -g(\Delta \theta + \Delta \phi) \\
    \Delta \ddot{\theta} &= -\alpha \Delta \phi
    \end{aligned}
    \quad
    \alpha = \frac{Mg\ell}{2J}
    \]

    On obtient :

    \[
    \dot{X} = AX + B\Delta\phi
    \]

    avec :

    \[
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix},
    \quad
    B =
    \begin{bmatrix}
    0 \\
    -g \\
    0 \\
    -\alpha
    \end{bmatrix}
    \]

    ---

    ## 2. Boucle fermée

    Avec :

    \[
    \Delta \phi = -K_{pp} X
    \]

    on obtient :

    \[
    \dot{X} = (A - BK_{pp})X
    \]

    ---

    ## 3. Choix des pôles désirés

    Objectifs :
    - stabilité asymptotique
    - convergence ~20 s
    - dynamique non oscillatoire

    On choisit des pôles réels dominants :

    \[
    \lambda_1 = -0.2,\quad \lambda_2 = -0.25,\quad \lambda_3 = -0.3,\quad \lambda_4 = -0.35
    \]

    ---

    ## 4. Méthode de conception

    Le système est :
    - complètement contrôlable (résultat précédent)
    - donc on peut imposer les 4 pôles

    On résout :

    \[
    \det(\lambda I - (A - BK)) = \prod (\lambda - \lambda_i)
    \]

    ---

    ## 5. Structure du gain

    On impose une loi de type retour d’état :

    \[
    K_{pp} =
    \begin{bmatrix}
    k_1 & k_2 & k_3 & k_4
    \end{bmatrix}
    \]

    ---

    ## 6. Interprétation des gains

    - \(k_3\) : stabilise l’angle \(\theta\)
    - \(k_4\) : amortit la dynamique angulaire
    - \(k_1\) : corrige la position \(x\)
    - \(k_2\) : stabilise la vitesse horizontale

    ---

    ## 7. Choix qualitatif des gains

    On choisit :

    - forte correction sur \(\theta\)
    - amortissement élevé sur vitesses
    - correction plus faible sur position

    Donc structure typique :

    \[
    k_3 \gg k_1, \quad k_4 \gg k_2
    \]

    ---

    ## 8. Résultat (forme explicite)

    Après placement de pôles (résolution algébrique ou commande numérique type Ackermann) :

    \[
    \boxed{
    K_{pp} =
    \begin{bmatrix}
    k_1 & k_2 & k_3 & k_4
    \end{bmatrix}
    }
    \]

    avec valeurs telles que :

    \[
    A - BK_{pp} \;\text{a pour spectre}\;
    \{-0.2,\,-0.25,\,-0.3,\,-0.35\}
    \]

    ---

    ## 9. Propriétés du système fermé

    ### ✔ Stabilité
    \[
    \Re(\lambda_i) < 0 \Rightarrow \text{asymptotiquement stable}
    \]

    ---

    ### ✔ Convergence de \(x(t)\)
    Grâce au couplage :
    \[
    \Delta x \leftrightarrow \Delta \theta
    \]

    la position converge aussi vers zéro.

    ---

    ### ✔ Temps de convergence
    Le pôle dominant \(-0.2\) donne :

    \[
    T_s \approx \frac{4}{0.2} \approx 20\,s
    \]

    ---

    ## 10. Conclusion

    \[
    \boxed{
    \text{Le système fermé est asymptotiquement stable et entièrement contrôlé par placement de pôles}
    }
    \]

    ---

    ## 11. Interprétation physique

    - \(\theta\) est stabilisé rapidement
    - cette stabilisation entraîne celle de \(x\)
    - le système devient un pendule inversé stabilisé par retour d’état
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse

    On considère le système linéarisé :

    \[
    \dot{X} = AX + B\Delta\phi,
    \qquad
    X =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}
    \]

    et la loi de commande :

    \[
    \Delta \phi = -K_{oc} X
    \]

    ---

    ## 1. Principe de la commande optimale

    On cherche à minimiser un coût quadratique :

    \[
    J = \int_0^{\infty}
    \left( X^T Q X + R \Delta\phi^2 \right)\,dt
    \]

    où :
    - \(Q \succeq 0\) pénalise les états
    - \(R > 0\) pénalise l’effort de commande

    ---

    ## 2. Choix des matrices de pondération

    On choisit une structure cohérente avec les objectifs :

    - forte priorité sur la stabilité de l’angle
    - contrôle de la position \(x\)
    - limitation de l’effort \(\phi\)

    \[
    Q =
    \begin{bmatrix}
    q_x & 0 & 0 & 0 \\
    0 & q_{\dot{x}} & 0 & 0 \\
    0 & 0 & q_\theta & 0 \\
    0 & 0 & 0 & q_{\dot{\theta}}
    \end{bmatrix}
    \]

    avec typiquement :
    - \(q_\theta \gg q_x\) (priorité à la stabilité angulaire)
    - \(q_{\dot{\theta}}, q_{\dot{x}}\) modérés
    - \(R\) choisi pour éviter des commandes trop agressives

    ---

    ## 3. Équation de Riccati

    On résout l’équation algébrique de Riccati :

    \[
    A^T P + P A - P B R^{-1} B^T P + Q = 0
    \]

    ---

    ## 4. Gain optimal

    Le gain est donné par :

    \[
    \boxed{
    K_{oc} = R^{-1} B^T P
    }
    \]

    ---

    ## 5. Interprétation du réglage

    Le choix de \(Q\) et \(R\) agit comme suit :

    ### ✔ Si \(q_\theta\) augmente
    - \(\theta\) converge plus vite
    - système plus rigide

    ### ✔ Si \(R\) augmente
    - effort \(\phi\) plus faible
    - dynamique plus lente mais plus robuste

    ### ✔ Si \(q_x\) augmente
    - amélioration du retour en position \(x\)

    ---

    ## 6. Comparaison avec placement de pôles

    | Méthode | Contrôle | Robustesse | Réglage |
    |--------|----------|------------|---------|
    | Pole placement | direct | faible | manuel |
    | LQR | optimal | élevé | via \(Q,R\) |

    ---

    ## 7. Propriétés du système fermé

    Avec :

    \[
    \dot{X} = (A - B K_{oc})X
    \]

    on obtient :

    - ✔ stabilité asymptotique garantie
    - ✔ compromis optimal entre performance et effort
    - ✔ convergence de \(x(t)\) et \(\theta(t)\)

    ---

    ## 8. Condition sur les performances

    En ajustant \(Q\) :

    - temps de convergence ~20 s obtenu en augmentant \(q_\theta\)
    - limitation de \(\phi\) via \(R\)
    - stabilité globale assurée automatiquement

    ---

    ## 9. Conclusion

    \[
    \boxed{
    K_{oc} = R^{-1} B^T P
    }
    \]

    est un gain optimal garantissant :

    - stabilité asymptotique
    - contrôle simultané de \(x\) et \(\theta\)
    - compromis optimal performance / énergie

    ---

    ## 10. Interprétation physique

    - le système “corrige automatiquement” ses gains
    - la dynamique est stabilisée sans réglage manuel de pôles
    - les états couplés sont régulés de manière optimale
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Réponse
    ### Étude de la Dynamique et de la Contrôlabilité du Système

    ## 1. Recherche du point d'équilibre
    À l'équilibre, toutes les vitesses et accélérations s'annulent ($\dot{X} = 0, \ddot{X} = 0$).

    À partir des équations de la dynamique :
    - **Rotation :** $J \ddot{\theta} = -f(\ell/2)\sin\phi = 0 \implies \phi_\star = 0$
    - **Translation Horizontale :** $M \ddot{x} = -f \sin(\theta + \phi) = 0 \implies \theta_\star = 0$
    - **Translation Verticale :** $M \ddot{y} = f \cos(\theta + \phi) - Mg = 0 \implies f_\star = Mg$

    **État et Commande d'équilibre :**
    $$s_\star = [x_\star, 0, y_\star, 0, 0, 0]^T, \quad u_\star = [Mg, 0]^T$$

    ---

    ## 2. Modèle Linéarisé
    Le système linéarisé autour de l'équilibre est défini par $\dot{X} = AX + BU$ avec :

    ### Matrice d'état $A$
    $$A = \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}$$

    ### Matrice de commande $B$
    $$B = \begin{bmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    \frac{1}{M} & 0 \\
    0 & 0 \\
    0 & -\frac{Mg\ell}{2J}
    \end{bmatrix}$$

    ---

    ## 3. Analyse de la Contrôlabilité
    Pour vérifier si le système est contrôlable, on calcule la matrice de Kalman :
    $$\mathcal{C} = \begin{bmatrix} B & AB & A^2B & A^3B & A^4B & A^5B \end{bmatrix}$$

    **Résultat :**
    La matrice $\mathcal{C}$ est de **rang 6** (pleine dimension de l'espace d'état).
    > **Conclusion :** Le système est complètement contrôlable. On peut stabiliser la position et l'angle à l'aide des entrées $\Delta f$ et $\Delta \phi$.

    ---

    ## 4. Simulation en boucle ouverte
    En l'absence de contrôle ($K=0$), une perturbation sur l'angle initial ($\Delta \theta_0 = 45^\circ$) provoque :
    1. Une **inclinaison constante** (l'angle ne revient pas à zéro).
    2. Une **accélération latérale** constante due à la gravité.
    3. Une **dérive parabolique** de la position $x(t)$.
    """)
    return


@app.cell
def _(M, g, np):
    def equilibrium_state(x_eq=0.0, y_eq=0.0):
        return np.array([x_eq, 0.0, y_eq, 0.0, 0.0, 0.0], dtype=float)

    equilibrium_input = np.array([M * g, 0.0], dtype=float)
    equilibrium_state(), equilibrium_input
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Linéarisation du système

    Nous linéarisons le système autour d'un point d'équilibre générique en introduisant les petites variations suivantes :

    $$
    x = x_\star + \Delta x, \quad y = y_\star + \Delta y, \quad \theta = \Delta \theta, \quad f = Mg + \Delta f, \quad \phi = \Delta \phi
    $$

    Nous définissons également les variables d'état pour les vitesses :

    $$
    \Delta v_x = \Delta \dot{x}, \qquad \Delta v_y = \Delta \dot{y}, \qquad \Delta \omega = \Delta \dot{\theta}
    $$

    #### 1. Approximations
    En utilisant les développements limités pour les petits angles ($\sin z \approx z$ et $\cos z \approx 1$) et en négligeant les produits d'ordre supérieur (comme $\Delta f \cdot \Delta \theta$), nous obtenons :

    * **Accélération horizontale :**
        $$M \Delta \ddot{x} = -(Mg + \Delta f)\sin(\Delta\theta + \Delta\phi) \approx -Mg(\Delta\theta + \Delta\phi)$$
    * **Accélération verticale :**
        $$M \Delta \ddot{y} = (Mg + \Delta f)\cos(\Delta\theta + \Delta\phi) - Mg \approx \Delta f$$
    * **Accélération angulaire :**
        $$J \Delta \ddot{\theta} = -(Mg + \Delta f)(\ell/2)\sin(\Delta \phi) \approx -Mg(\ell/2)\Delta \phi$$

    ---

    #### 2. Dynamique linéarisée
    Les équations simplifiées du mouvement sont donc :

    \begin{align*}
    \Delta \ddot{x} & = -g \Delta \theta - g \Delta \phi \\
    \Delta \ddot{y} & = \frac{1}{M}\Delta f \\
    \Delta \ddot{\theta} & = - \frac{Mg\ell}{2J}\Delta \phi
    \end{align*}

    ---

    #### 3. Application au cas de la tige
    En considérant le moment d'inertie d'une tige fine $J = \frac{M\ell^2}{12}$, le coefficient de la dynamique angulaire se simplifie :

    $$
    \frac{Mg\ell}{2J} = \frac{Mg\ell}{2(M\ell^2/12)} = \frac{6g}{\ell}
    $$

    Avec les paramètres numériques $g=1$ et $\ell=2$, l'équation de rotation devient simplement :

    $$\Delta \ddot{\theta} = -3 \Delta \phi$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Représentation par variables d'état

    Pour décrire la dynamique du système, nous utilisons le vecteur d'état linéarisé $z$ et le vecteur de commande linéarisé $\Delta u$.

    #### 1. Vecteur d'état
    Le vecteur $z \in \mathbb{R}^6$ regroupe les positions et les vitesses du système :

    $$
    z =
    \begin{bmatrix}
    \Delta x \\
    \Delta v_x \\
    \Delta y \\
    \Delta v_y \\
    \Delta \theta \\
    \Delta \omega
    \end{bmatrix}
    $$

    #### 2. Vecteur de commande
    Le vecteur $\Delta u$ représente les variations des entrées autour du point d'équilibre :

    $$
    \Delta u =
    \begin{bmatrix}
    \Delta f \\
    \Delta \phi
    \end{bmatrix}
    $$

    #### 3. Équations d'état
    La dynamique est régie par l'équation $\dot{z} = A z + B \Delta u$, où les matrices $A$ et $B$ sont définies par :

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix},
    \qquad
    B =
    \begin{bmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    1/M & 0 \\
    0 & 0 \\
    0 & -Mg\ell/(2J)
    \end{bmatrix}
    $$
    """)
    return


@app.cell
def _(J, M, g, l, np):
    alpha = M * g * l / (2 * J)

    A_lin = np.array(
        [
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, -g, 0.0],
            [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        ],
        dtype=float,
    )

    B_lin = np.array(
        [
            [0.0, 0.0],
            [0.0, -g],
            [0.0, 0.0],
            [1.0 / M, 0.0],
            [0.0, 0.0],
            [0.0, -alpha],
        ],
        dtype=float,
    )

    A_lin, B_lin
    return A_lin, B_lin


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Analyse de la stabilité

    **Le vol stationnaire à l'équilibre est-il stable ?**

    **Non.** L'équilibre en vol stationnaire (hovering) n'est pas asymptotiquement stable en boucle ouverte.

    #### Justification mathématique
    L'analyse de la matrice d'état $A$ montre que :
    * Toutes les valeurs propres de $A$ sont nulles ($\lambda_i = 0$).
    * En automatique, cela signifie que le système se comporte comme un **intégrateur pur**.

    #### Justification physique
    Il n'existe aucun **mécanisme de rappel naturel** (comme un ressort ou un amortissement) qui ramènerait le système vers son équilibre après une perturbation.

    Si le drone est légèrement incliné ou poussé :
    1. Il ne redressera pas son angle tout seul.
    2. Sa vitesse continuera de croître ou sa position de dériver indéfiniment.

    > **Conclusion :** Une intervention active via une loi de commande (boucle fermée) est indispensable pour stabiliser le système.
    """)
    return


@app.cell
def _(A_lin, np):
    eig_A_lin = np.linalg.eigvals(A_lin)
    eig_A_lin
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###  Analyse de la contrôlabilité

    **Le système est-il contrôlable ?**

    **Oui.** Le système linéarisé complet est entièrement contrôlable.

    #### Justification intuitive
    Le système peut être décomposé en deux sous-systèmes découplés au premier ordre :

    1.  **Sous-système vertical $(\Delta y, \Delta v_y)$ :** L'entrée $\Delta f$ (variation de la poussée) contrôle directement ce double intégrateur.
    2.  **Sous-système latéral-attitude $(\Delta x, \Delta v_x, \Delta \theta, \Delta \omega)$ :** L'entrée $\Delta \phi$ (inclinaison du booster) permet de contrôler l'angle $\theta$, qui lui-même induit un mouvement latéral $x$ grâce au couplage de la gravité.

    Puisque ces deux sous-systèmes sont contrôlables indépendamment, l'ensemble du système est **contrôlable**.

    > **Note technique :** Ce résultat a été confirmé mathématiquement par le calcul du rang de la matrice de Kalman, qui est égal à 6 (dimension totale de l'espace d'état).
    """)
    return


@app.cell
def _(A_lin, B_lin, np):
    def controllability_matrix(A, B):
        n = A.shape[0]
        blocks = [B]
        current = B
        for _ in range(1, n):
            current = A @ current
            blocks.append(current)
        return np.hstack(blocks)

    ctrb_full = controllability_matrix(A_lin, B_lin)
    ctrb_full_rank = np.linalg.matrix_rank(ctrb_full)
    ctrb_full_rank
    return (controllability_matrix,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Système latéral réduit

    Si l'on ne conserve que les variables latérales et angulaires en fixant la poussée $f = Mg$, le vecteur d'état réduit $z_{\mathrm{lat}}$ et l'entrée $u_{\mathrm{lat}}$ sont :

    $$
    z_{\mathrm{lat}} =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix},
    \qquad
    u_{\mathrm{lat}} = \Delta \phi
    $$

    #### 1. Équations du système réduit
    La dynamique simplifiée s'écrit :

    \begin{align*}
    \Delta \dot{x} &= \Delta v_x \\
    \Delta \ddot{x} &= -g \Delta \theta - g \Delta \phi \\
    \Delta \dot{\theta} &= \Delta \omega \\
    \Delta \ddot{\theta} &= -\frac{Mg\ell}{2J}\Delta \phi
    \end{align*}

    #### 2. Représentation d'état $\dot{z}_{\mathrm{lat}} = A_{\mathrm{lat}} z_{\mathrm{lat}} + B_{\mathrm{lat}} \Delta \phi$
    Les matrices correspondantes sont :

    $$
    A_{\mathrm{lat}} =
    \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix},
    \qquad
    B_{\mathrm{lat}} =
    \begin{bmatrix}
    0 \\
    -g \\
    0 \\
    -\frac{Mg\ell}{2J}
    \end{bmatrix}
    $$

    #### 3. Application numérique
    Avec les paramètres $g=1$ et $\ell=2$ (où $\frac{6g}{\ell} = 3$), nous obtenons :

    $$
    B_{\mathrm{lat}} = \begin{bmatrix} 0 \\ -1 \\ 0 \\ -3 \end{bmatrix}
    $$

    **Analyse de la contrôlabilité :**
    La matrice de Kalman pour ce système réduit est de **rang 4**. Par conséquent, le système latéral est entièrement contrôlable : il est possible de stabiliser à la fois la position horizontale et l'angle d'inclinaison en utilisant uniquement l'orientation du booster ($\Delta \phi$).
    """)
    return


@app.cell
def _(A_lat, B_lat, controllability_matrix, np):
    ctrb_lat = controllability_matrix(A_lat, B_lat)
    ctrb_lat_rank = np.linalg.matrix_rank(ctrb_lat)
    A_lat, B_lat, ctrb_lat_rank
    return


@app.cell
def _(A_lat, B_lat, np, scipy):
    def solve_linear_lateral(t_span, z0, phi_fun):
        def fun(t, z):
            phi = float(np.atleast_1d(phi_fun(t, z))[0])
            return A_lat @ z + B_lat[:, 0] * phi

        r = scipy.integrate.solve_ivp(fun, t_span, z0, dense_output=True, max_step=0.05)
        return r.sol

    return (solve_linear_lateral,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Analyse du comportement sans contrôle

    Si l'on n'applique aucune correction ($\Delta \phi(t)=0$ pour tout $t$), les équations de la dynamique latérale se simplifient ainsi :

    \begin{align*}
    \Delta \ddot{x} &= -g \Delta \theta \\
    \Delta \ddot{\theta} &= 0
    \end{align*}

    #### Évolution temporelle
    En partant d'une perturbation initiale de l'angle $\Delta \theta(0)=\pi/4$ avec une vitesse angulaire nulle $\Delta \dot{\theta}(0)=0$, nous obtenons :

    1.  **L'angle reste constant :**
        $$\Delta \theta(t) = \frac{\pi}{4}$$
        Pour tout $t$, l'inclinaison ne change pas car aucune force ne vient s'opposer au déséquilibre.

    2.  **La position dérive :**
        L'accélération horizontale est donc constante :
        $$\Delta \ddot{x}(t) = -g \frac{\pi}{4}$$
        Par intégration, cela signifie que la vitesse croît linéairement et que le déplacement latéral $\Delta x(t)$ dérive de manière **quadratique** (parabolique) au cours du temps.

    > **Conclusion :** Le système ne possède aucun mécanisme d'auto-correction. Sans un asservissement actif pour ramener l'angle à zéro, une simple erreur d'inclinaison initiale entraîne une divergence totale de la position du booster.
    """)
    return


@app.cell
def _(np, plt, solve_linear_lateral):
    def linear_free_fall_example():
        t_span = [0.0, 8.0]
        z0 = np.array([0.0, 0.0, np.pi / 4, 0.0], dtype=float)
        sol = solve_linear_lateral(t_span, z0, lambda t, z: np.array([0.0]))
        t = np.linspace(t_span[0], t_span[1], 600)
        z_t = sol(t)

        fig, axes = plt.subplots(2, 1, figsize=(7, 6), sharex=True)
        axes[0].plot(t, z_t[0], label=r"$\Delta x(t)$")
        axes[0].axhline(0.0, color="black", lw=0.8, ls="--")
        axes[0].set_ylabel(r"$\Delta x$")
        axes[0].grid(True)
        axes[0].legend()

        axes[1].plot(t, z_t[2], color="darkorange", label=r"$\Delta \theta(t)$")
        axes[1].axhline(0.0, color="black", lw=0.8, ls="--")
        axes[1].set_xlabel("time $t$")
        axes[1].set_ylabel(r"$\Delta \theta$")
        axes[1].grid(True)
        axes[1].legend()

        fig.suptitle("Reduced Linear Model with $\\Delta \\phi(t)=0$")
        fig.tight_layout()
        return fig

    linear_free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Conception d'une commande manuelle (PD)

    Pour simplifier la conception, nous choisissons de ne réinjecter que les variables angulaires (commande proportionnelle-dérivée sur l'angle) :

    $$
    K =
    \begin{bmatrix}
    0 & 0 & k_\theta & k_\omega
    \end{bmatrix}
    $$

    #### 1. Loi de commande
    L'orientation du booster est alors pilotée par :
    $$
    \Delta \phi = -k_\theta \Delta \theta - k_\omega \Delta \dot{\theta}
    $$

    #### 2. Dynamique en boucle fermée
    En sachant que $\Delta \ddot{\theta} = -3 \Delta \phi$, l'évolution de l'angle en boucle fermée devient :
    $$
    \Delta \ddot{\theta} - 3 k_\omega \Delta \dot{\theta} - 3 k_\theta \Delta \theta = 0
    $$

    Pour obtenir un modèle de second ordre stable de la forme $\Delta \ddot{\theta} + b \Delta \dot{\theta} + a \Delta \theta = 0$, nous devons identifier les gains :
    $$
    k_\theta = -\frac{a}{3}, \qquad k_\omega = -\frac{b}{3}
    $$

    #### 3. Application numérique
    Un bon compromis (stabilité et douceur) est obtenu avec $a \approx 0.12$ et $b \approx 0.5$, ce qui donne :
    $$
    K_{\mathrm{manuelle}} = \begin{bmatrix} 0 & 0 & -0.04 & -1/6 \end{bmatrix}
    $$



    ---

    ### ⚠️ Limite de cette commande
    Avec ces réglages, l'angle $\theta(t)$ converge vers zéro en moins de 20 secondes tout en maintenant l'inclinaison $\phi(t)$ très faible.

    Cependant, le système à 4 états n'est **pas** encore asymptotiquement stable. Pourquoi ? Parce que $\Delta x$ et $\Delta \dot{x}$ ne sont pas pris en compte dans le calcul. Mathématiquement, deux valeurs propres restent à **0**. Le booster sera "droit" (vertical), mais il pourrait continuer à dériver à une vitesse constante s'il avait une impulsion initiale.
    """)
    return


@app.cell
def _(np, plt, solve_linear_lateral):
    def simulate_linear_state_feedback(K, t_span=(0.0, 30.0), z0=None):
            if z0 is None:
                z0 = np.array([0.0, 0.0, np.pi / 4, 0.0], dtype=float)

            def phi_fun(t, z):
                # Assure-toi que solve_linear_lateral est défini ailleurs
                return np.array([float(-(K @ z.reshape(-1, 1))[0, 0])])

            sol = solve_linear_lateral(t_span, z0, phi_fun)
            return sol, phi_fun
    def plot_manual_tuning():
        manual_gain_guesses = [
            ("guess 1", np.array([[0.0, 0.0, -0.03, -0.14]], dtype=float)),
            ("guess 2", np.array([[0.0, 0.0, -0.04, -1.0 / 6.0]], dtype=float)),
            ("guess 3", np.array([[0.0, 0.0, -1.0 / 15.0, -7.0 / 30.0]], dtype=float)),
        ]


        t_eval = np.linspace(0.0, 30.0, 1200)
        # On utilise des noms locaux pour éviter les conflits Marimo
        fig_tuning, ax_tuning = plt.subplots(3, 1, figsize=(8, 9), sharex=True)

        for label, K_mat in manual_gain_guesses:
            sol, phi_f = simulate_linear_state_feedback(K_mat)
            z_t = sol(t_eval)
            # Calcul de phi sur toute la trajectoire
            phi_t = np.array([phi_f(tt, z_t[:, idx])[0] for idx, tt in enumerate(t_eval)])
        
            ax_tuning[0].plot(t_eval, z_t[2], label=label)
            ax_tuning[1].plot(t_eval, phi_t, label=label)
            ax_tuning[2].plot(t_eval, z_t[0], label=label)

        ax_tuning[0].set_ylabel(r"$\Delta \theta$ (rad)")
        ax_tuning[0].legend()
        ax_tuning[1].set_ylabel(r"$\Delta \phi$ (rad)")
        ax_tuning[2].set_ylabel(r"$\Delta x$ (m)")
        ax_tuning[2].set_xlabel("Temps (s)")
    
        for a in ax_tuning:
            a.grid(True)
            a.axhline(0, color='black', lw=1, ls='--')

        fig_tuning.suptitle("Réglage manuel : Comparaison des 3 essais")
        plt.tight_layout()
        return fig_tuning

    # Appel de la fonction pour afficher le graphique
    plot_manual_tuning()
    return (simulate_linear_state_feedback,)


@app.cell
def _(np):
    K_manual = np.array([[0.0, 0.0, -0.04, -1.0 / 6.0]], dtype=float)
    K_manual
    return (K_manual,)


@app.cell
def _(A_lat, B_lat, K_manual, np):
    A_manual_cl = A_lat - B_lat @ K_manual
    eig_manual_cl = np.linalg.eigvals(A_manual_cl)
    eig_manual_cl
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Stabilisation par Placement de Pôles

    Pour cette étape, nous utilisons le vecteur d'état latéral complet. La loi de commande par retour d'état s'écrit :

    $$
    \Delta \phi = -K_{pp}
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}
    $$

    #### 1. Choix des pôles cibles
    Pour garantir les performances souhaitées, j'ai sélectionné les pôles suivants :
    $$\{-0.4, \quad -0.45, \quad -0.6 \pm 0.25 i\}$$

    #### 2. Analyse du choix
    * **Stabilité garantie :** Tous les pôles ont une partie réelle négative, ce qui assure que l'erreur convergera vers zéro.
    * **Rapidité :** La convergence est plus rapide qu'avec le contrôleur manuel (PD).
    * **Amortissement :** La composante imaginaire ($\pm 0.25 i$) introduit une légère oscillation. C'est un compromis utile pour obtenir une réponse "vive" sans demander des angles de cardan (gimbal) excessifs qui pourraient saturer les actionneurs.

    ---

    ### Pourquoi est-ce "meilleur" que le réglage manuel ?
    Contrairement au contrôleur précédent qui ne stabilisait que l'angle, le placement de pôles permet de coupler la dynamique de la position $x$ et de l'angle $\theta$.

    Grâce à cette matrice $K_{pp}$ complète, le booster ne va pas seulement se remettre à la verticale : il va aussi **revenir activement vers sa position cible $x=0$**. On élimine ainsi la dérive résiduelle que tu as pu observer lors de tes simulations précédentes.
    """)
    return


@app.cell
def _(A_lat, B_lat, np, scipy):
    desired_poles_pp = np.array([-0.4, -0.45, -0.6 + 0.25j, -0.6 - 0.25j])
    K_pp = scipy.signal.place_poles(A_lat, B_lat, desired_poles_pp).gain_matrix
    A_pp_cl = A_lat - B_lat @ K_pp
    eig_pp_cl = np.linalg.eigvals(A_pp_cl)
    K_pp, eig_pp_cl
    return (K_pp,)


@app.cell
def _(K_pp, np, plt, simulate_linear_state_feedback):
    def pole_placement_example():
        sol, phi_fun = simulate_linear_state_feedback(K_pp, t_span=(0.0, 25.0))
        t = np.linspace(0.0, 25.0, 1000)
        z_t = sol(t)
        phi_t = np.array([phi_fun(tt, z_t[:, i])[0] for i, tt in enumerate(t)])

        fig, axes = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
        axes[0].plot(t, z_t[0], label=r"$\Delta x(t)$")
        axes[0].plot(t, z_t[2], label=r"$\Delta \theta(t)$")
        axes[0].axhline(0.0, color="black", lw=0.8, ls="--")
        axes[0].set_ylabel("states")
        axes[0].grid(True)
        axes[0].legend()

        axes[1].plot(t, phi_t, color="darkgreen", label=r"$\Delta \phi(t)$")
        axes[1].axhline(np.pi / 2, color="grey", lw=0.8, ls="--")
        axes[1].axhline(-np.pi / 2, color="grey", lw=0.8, ls="--")
        axes[1].set_ylabel(r"$\Delta \phi$")
        axes[1].grid(True)
        axes[1].legend()

        axes[2].plot(t, z_t[1], label=r"$\Delta \dot{x}(t)$")
        axes[2].plot(t, z_t[3], label=r"$\Delta \dot{\theta}(t)$")
        axes[2].axhline(0.0, color="black", lw=0.8, ls="--")
        axes[2].set_xlabel("time $t$")
        axes[2].set_ylabel("derivatives")
        axes[2].grid(True)
        axes[2].legend()

        fig.suptitle("Linear Closed Loop with Pole Placement")
        fig.tight_layout()
        return fig

    pole_placement_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Contrôle Optimal (LQR)

    Pour la conception du régulateur LQR, nous cherchons à minimiser le coût global défini par l'intégrale :

    $$
    \int_0^\infty
    \left(
    z_{\mathrm{lat}}^\top Q z_{\mathrm{lat}}
    +
    \Delta \phi^\top R \Delta \phi
    \right) dt
    $$

    #### 1. Paramètres de pondération
    J'ai choisi les matrices de poids suivantes :
    * **Matrice d'état :** $Q = \mathrm{diag}(1, 1, 5, 2)$
    * **Matrice de commande :** $R = [50]$

    #### 2. Analyse physique du réglage
    * **Priorité à l'angle ($\theta$) :** Le poids plus élevé sur $\theta$ (valeur de 5 dans la matrice $Q$) reflète le fait que maintenir le booster à la verticale est bien plus critique que de laisser la position $x$ s'écarter légèrement pendant un court instant.
    * **Économie d'actionneur ($R$) :** La valeur relativement élevée de $R$ (50) agit comme un "frein" sur le contrôleur. Cela l'empêche de commander des angles de cardan (gimbal) irréalistes ou trop brusques, ce qui protège la mécanique du drone.

    ---

    ### Pourquoi utiliser le LQR ici ?
    Le LQR est idéal car il trouve automatiquement le meilleur équilibre mathématique. Si tu augmentes $R$, ton booster sera plus "mou" mais consommera moins d'énergie. Si tu augmentes les valeurs de $Q$, il sera extrêmement réactif et précis, mais ses moteurs bougeront très vite.

    C'est cette méthode qui est généralement utilisée pour les systèmes aérospatiaux réels (comme ceux de SpaceX) pour gérer la descente des boosters.
    """)
    return


@app.cell
def _(A_lat, B_lat, np, scipy):
    Q_oc = np.diag([1.0, 1.0, 5.0, 2.0])
    R_oc = np.array([[50.0]], dtype=float)
    P_oc = scipy.linalg.solve_continuous_are(A_lat, B_lat, Q_oc, R_oc)
    K_oc = np.linalg.solve(R_oc, B_lat.T @ P_oc)
    A_oc_cl = A_lat - B_lat @ K_oc
    eig_oc_cl = np.linalg.eigvals(A_oc_cl)
    K_oc, eig_oc_cl
    return (K_oc,)


@app.cell
def _(K_oc, np, plt, simulate_linear_state_feedback):
    def lqr_example():
        sol, phi_fun = simulate_linear_state_feedback(K_oc, t_span=(0.0, 20.0))
        t = np.linspace(0.0, 20.0, 1000)
        z_t = sol(t)
        phi_t = np.array([phi_fun(tt, z_t[:, i])[0] for i, tt in enumerate(t)])

        fig, axes = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
        axes[0].plot(t, z_t[0], label=r"$\Delta x(t)$")
        axes[0].plot(t, z_t[2], label=r"$\Delta \theta(t)$")
        axes[0].axhline(0.0, color="black", lw=0.8, ls="--")
        axes[0].set_ylabel("states")
        axes[0].grid(True)
        axes[0].legend()

        axes[1].plot(t, phi_t, color="firebrick", label=r"$\Delta \phi(t)$")
        axes[1].axhline(np.pi / 2, color="grey", lw=0.8, ls="--")
        axes[1].axhline(-np.pi / 2, color="grey", lw=0.8, ls="--")
        axes[1].set_ylabel(r"$\Delta \phi$")
        axes[1].grid(True)
        axes[1].legend()

        axes[2].plot(t, z_t[1], label=r"$\Delta \dot{x}(t)$")
        axes[2].plot(t, z_t[3], label=r"$\Delta \dot{\theta}(t)$")
        axes[2].axhline(0.0, color="black", lw=0.8, ls="--")
        axes[2].set_xlabel("time $t$")
        axes[2].set_ylabel("derivatives")
        axes[2].grid(True)
        axes[2].legend()

        fig.suptitle("Linear Closed Loop with LQR")
        fig.tight_layout()
        return fig

    lqr_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Validation sur le modèle non-linéaire

    Les contrôleurs par placement de pôles et LQR ont été conçus uniquement pour le modèle latéral réduit. Pour les valider sur la **dynamique non-linéaire complète**, j'utilise ces lois latérales pour $\phi$ et j'ajoute une boucle de maintien d'altitude pour la poussée $f$ :

    #### 1. Loi de commande de la poussée
    Pour compenser la gravité et les inclinaisons, la force $f(t)$ est calculée ainsi :

    $$
    f(t) = \frac{M\bigl(g + k_y(y_{\mathrm{ref}} - y) - k_v \dot{y}\bigr)}{\cos(\theta + \phi)}
    $$

    * **Maintien d'altitude :** Le numérateur est un correcteur PD qui stabilise le drone à une hauteur de référence $y_{\mathrm{ref}}$.
    * **Compensation d'angle :** La division par $\cos(\theta + \phi)$ permet d'augmenter automatiquement la poussée lorsque le booster est incliné, afin de maintenir une force verticale constante malgré l'angle.

    #### 2. Sécurité et contraintes
    Pour rester dans un cadre de fonctionnement réaliste et sécurisé :
    * **Saturation du cardan (Gimbal) :** L'angle $\phi$ est limité (clippé) à l'intervalle $[-\pi/3, \pi/3]$.
    * **Respect des limites :** Cela garantit que la validation reste bien à l'intérieur de la zone de sécurité demandée ($|\phi| < \pi/2$), même en cas de fortes perturbations.

    ---

    ### Pourquoi cette étape est-elle "le test de vérité" ?
    Dans le monde réel, un booster ne reste pas sagement dans le domaine linéaire. En testant ton gain $K$ (calculé sur un modèle simplifié) avec cette formule de poussée non-linéaire, tu vérifies la **robustesse** de ton système. Si le drone parvient à se stabiliser malgré la division par le cosinus et la saturation des angles, cela signifie que ton design est prêt pour une application concrète.
    """)
    return


@app.cell
def _(K_oc, K_pp, M, g, np, redstart_solve):
    def nonlinear_hover_validation(K, t_span=(0.0, 25.0), y0=None, y_ref=None, phi_limit=np.pi / 3):
        if y0 is None:
            y0 = np.array([0.0, 0.0, 5.0, 0.0, np.pi / 4, 0.0], dtype=float)
        else:
            y0 = np.array(y0, dtype=float)

        if y_ref is None:
            y_ref = float(y0[2])

        k_y = 1.2
        k_vy = 1.8

        def f_phi(t, state):
            x, vx, y, vy, theta, omega = state
            z_lat = np.array([x, vx, theta, omega], dtype=float)
            phi = float(-(K @ z_lat.reshape(-1, 1))[0, 0])
            phi = float(np.clip(phi, -phi_limit, phi_limit))

            denom = max(np.cos(theta + phi), 0.25)
            vertical_command = g + k_y * (y_ref - y) - k_vy * vy
            f = max(M * vertical_command / denom, 0.0)
            return np.array([f, phi], dtype=float)

        sol = redstart_solve(t_span, y0, f_phi)
        return sol, f_phi

    validation_pp = nonlinear_hover_validation(K_pp)
    validation_oc = nonlinear_hover_validation(K_oc)
    return validation_oc, validation_pp


@app.cell
def _(np, plt):
    def plot_nonlinear_validation(validation, title):
        sol, f_phi = validation
        t = np.linspace(0.0, 25.0, 1200)
        state_t = sol(t)
        f_t = np.array([f_phi(tt, state_t[:, i])[0] for i, tt in enumerate(t)])
        phi_t = np.array([f_phi(tt, state_t[:, i])[1] for i, tt in enumerate(t)])

        fig, axes = plt.subplots(4, 1, figsize=(8, 11), sharex=True)

        axes[0].plot(t, state_t[0], label=r"$x(t)$")
        axes[0].plot(t, state_t[4], label=r"$\theta(t)$")
        axes[0].axhline(0.0, color="black", lw=0.8, ls="--")
        axes[0].set_ylabel("states")
        axes[0].grid(True)
        axes[0].legend()

        axes[1].plot(t, state_t[2], color="teal", label=r"$y(t)$")
        axes[1].axhline(state_t[2, 0], color="grey", lw=0.8, ls="--")
        axes[1].set_ylabel(r"$y$")
        axes[1].grid(True)
        axes[1].legend()

        axes[2].plot(t, phi_t, color="purple", label=r"$\phi(t)$")
        axes[2].axhline(np.pi / 2, color="grey", lw=0.8, ls="--")
        axes[2].axhline(-np.pi / 2, color="grey", lw=0.8, ls="--")
        axes[2].set_ylabel(r"$\phi$")
        axes[2].grid(True)
        axes[2].legend()

        axes[3].plot(t, f_t, color="darkred", label=r"$f(t)$")
        axes[3].axhline(1.0, color="grey", lw=0.8, ls="--", label=r"$Mg$")
        axes[3].set_xlabel("time $t$")
        axes[3].set_ylabel(r"$f$")
        axes[3].grid(True)
        axes[3].legend()

        fig.suptitle(title)
        fig.tight_layout()
        return fig

    return (plot_nonlinear_validation,)


@app.cell
def _(plot_nonlinear_validation, validation_pp):
    plot_nonlinear_validation(validation_pp, "Nonlinear Validation with Pole Placement")
    return


@app.cell
def _(plot_nonlinear_validation, validation_oc):
    plot_nonlinear_validation(validation_oc, "Nonlinear Validation with LQR")
    return


@app.cell
def _(booster_anim, mo, validation_pp, world):
    def validation_animation_pp():
        sol, f_phi = validation_pp
        T = 25.0
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t: sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -1, 8],
                booster_anim(x, y, theta, f, phi, T=T),
            )
        ).center()

    validation_animation_pp()
    return


@app.cell
def _(booster_anim, mo, validation_oc, world):
    def validation_animation_oc():
        sol, f_phi = validation_oc
        T = 25.0
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t: sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -1, 8],
                booster_anim(x, y, theta, f, phi, T=T),
            )
        ).center()

    validation_animation_oc()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
