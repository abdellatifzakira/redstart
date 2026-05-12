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
    return


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


@app.cell
def _():
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
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


if __name__ == "__main__":
    app.run()
