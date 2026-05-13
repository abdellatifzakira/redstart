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

    return la, np, plt, sci, scipy


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


@app.cell
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


@app.cell
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our state is $s = (x, v_x, y, v_y,\theta, \omega)$ and the system is governed by
    $\dot{s} = F(s, f, \phi)$ with
    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    The equilibria are characterized by $F(s, f, \phi) = 0$. We obtain directly that
    $v_x = v_y = 0$ and $\omega = 0$. We also extract the two equations

    $$
    \begin{bmatrix}
    -(f / M) \sin (\theta + \phi) \\
    +(f / M) \cos(\theta +\phi)
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    $$
    which holds if when $|\theta| < \pi/2$ and $|\phi| < \pi/2$ and only if
    $\theta = \phi = 0$ and $f = M g$. The final equation is then satisfied if and only if
    $\omega = 0$. Finally, we obtain the equilibria as:
    $$
    \begin{bmatrix}
    x \\
    v_x \\
    y \\
    v_y \\
    \theta \\
    \omega \\
    f \\
    \phi
    \end{bmatrix}
    =
    \begin{bmatrix}
    ? \\
    0 \\
    ? \\
    0 \\
    0 \\
    0 \\
    M g \\
    0
    \end{bmatrix}
    $$
    where $?$ stands for "any possible value".
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $\Delta \theta = \theta$, $\Delta \phi = \phi$ and $\Delta f = f - M g$. Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and that for small values of $\alpha$, $\sin \alpha \approx \alpha$ and $\cos \alpha \approx 1$, we obtain:

    \begin{align*}
    M (d/dt)^2 \Delta x &= - Mg (\Delta \theta + \Delta \phi)  \\
    M (d/dt)^2 \Delta y &= \Delta f \\
    J (d/dt)^2 \Delta \theta &= - (Mg \ell /2) \Delta \phi \\
    \end{align*}
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
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note: remember that $J = (1/12) M \ell^2$.

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 1 \\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix}
    \;\;\;
    B =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & -M g \ell/(2J)\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & - 6 g / \ell\\
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(g, np):
    A = np.zeros((6, 6))
    A[0, 1] = 1.0
    A[1, 4] = -g
    A[2, 3] = 1.0
    A[4, -1] = 1.0
    A
    return (A,)


@app.cell(hide_code=True)
def _(M, g, l, np):
    B = np.zeros((6, 2))
    B[ 1, 1]  = -g 
    B[ 3, 0]  = 1/M
    B[-1, 1] = -6 * g / l
    B
    return (B,)


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
    ### 🔓 Solution

    No, since $0$ is the only eigenvalue of $A$ and $0$ doesn't have a negative real part.
    """)
    return


@app.cell(hide_code=True)
def _(A, la):
    eigenvalues, eigenvectors = la.eig(A)
    print(f"Eigenvalues of A: {eigenvalues}")
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
    ### 🔓 Solution

    The controllability matrix of the system is:
    """)
    return


@app.cell(hide_code=True)
def _(A, B, np):
    # Controllability
    cs = np.column_stack
    mp = np.linalg.matrix_power
    KC = cs([mp(A, k) @ B for k in range(6)])
    KC
    return (KC,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and its rank is
    """)
    return


@app.cell(hide_code=True)
def _(KC, np):
    int(np.linalg.matrix_rank(KC))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    which is equal to the state dimension, so the answer is yes, it's controllable.
    """)
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
    ### 🔓 Solution
    """)
    return


@app.cell
def _(g, l, np):
    A_lat = np.array([
        [0, 1, 0, 0], 
        [0, 0, -g, 0], 
        [0, 0, 0, 1], 
        [0, 0, 0, 0]], dtype=np.float64)
    B_lat = np.array([[0, -g, 0, - 6 * g / l]]).T

    print("A_lat:")
    print(A_lat)
    print("B_lat:")
    print(B_lat)
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(A_lat, B_lat, np):
    # Controllability
    _cs = np.column_stack
    _mp = np.linalg.matrix_power
    KC_lat = _cs([_mp(A_lat, k) @ B_lat for k in range(6)])
    KC_lat
    return (KC_lat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This reduced system of dimension 4 is controllable since the rank of its controllability matrix is 4:
    """)
    return


@app.cell(hide_code=True)
def _(KC_lat, np):
    np.linalg.matrix_rank(KC_lat)
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
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(g, l, np):
    def make_fun_lat(phi):
        def fun_lat(t, state):
            x, dx, theta, dtheta = state
            phi_ = phi(t, state)
            d2x = -g * (theta + phi_)
            d2theta = - 6 * g / l * phi_
            return np.array([dx, d2x, dtheta, d2theta])

        return fun_lat

    return (make_fun_lat,)


@app.cell(hide_code=True)
def _(make_fun_lat, mo, np, plt, sci):
    def lin_sim_1():
        def phi(t, state):
            return 0.0

        f_lat = make_fun_lat(phi)
        t_span = [0, 10]
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]
        r = sci.solve_ivp(
            fun=f_lat, y0=state_0, t_span=t_span, dense_output=True
        )
        t = np.linspace(t_span[0], t_span[1], 1000)
        sol_t = r.sol(t)
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(t, sol_t[0], label=r"$x(t)$")
        ax1.grid(True)
        ax1.legend()
        ax2.plot(t, sol_t[2], label=r"$\theta(t)$")
        ax2.grid(True)
        ax2.set_xlabel(r"time $t$")
        ax2.legend()
        return mo.center(fig)


    lin_sim_1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Since the reactor pushes (with a constant force) in the axis of the booster ($\phi=0$) and the initial title velocity $\omega = \dot{\theta}$ is zero, it's sensible that the title $\theta$ stays constant. That explains the second graph.
    - On the other hand, the constant projected force on the $x$-axis drives a constant acceleration which is towards the left since the initial tilt is positive. That explain the first graph.
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We try first a controller that corrects using only $\Delta \theta$ since it it's the simples think we can think of (a controller based only on the derivative would not achieve $\Delta \theta(t) \to 0$ since it would only knows $\Delta \theta(t)$ up to a constant). When $\Delta \theta > 0$, we want the reactor to be oriented on the right ($\Delta \phi > 0$) to compensate for this trend.

    Hence it makes sens to start for something simple such as
    $\Delta \phi =  \Delta \theta$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & 0
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    and

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    Let's make a simulation out of this!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k1():

        K = np.array([0.0, 0.0, -1.0, 0.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Unfortunately that doesn't work, we have introduced an oscillatory dynamics.

    To correct that, we may introduce some additionial "friction" that prevents our compensation to kick in too fast and end up the control
    $\Delta \phi = \Delta \theta + \beta (d \Delta \theta /dt)$, for some $\beta > 0$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & -\beta
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    Experimentally (see below), anything between $\beta = 0.1$ and $\beta = 5.0$ seems to satisfy the specification. The closed-loop dynamics is slower need $0.1$ and faster near $5.0$.

    In any case, there is a permament drift which is induced on $\Delta x$, which does not converge to $0$. This is corroborated by a double eigenvalue at $0$, which proves that our closed-loop dynamics is **not** asymptotically stable.
    """)
    return


@app.cell(hide_code=True)
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k2():

        K = np.array([0.0, 0.0, -1.0, -0.1])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k2()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k3():

        K = np.array([0.0, 0.0, -1.0, -5.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k3()
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We decide to try to cluster all our eigenvalue near a single real (negative) value
    $s$. If we want a convergence at 5% in 20 seconds at most, we know that $|\lambda|$
    should be at least $3 / 20 = 0.15$.

    Experimentally however this is a bit slow to converge (see below), the setup is better if we pick a faster dynamics, to have our eigenvalues clustered around $-0.5$ for example.

    There is actually quite a range of locations that work, but around $-0.1$, we start compensating too fast and to violate the constraint on the maximal value of $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_3():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-0.15 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_3()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Kpp = scipy.signal.place_poles(
        A=A_lat,
        B=B_lat,
        poles=-0.5 * np.array([1.0, 1.01, 1.02, 1.03]),
    ).gain_matrix.squeeze()


    def lin_sim_32():
        K = Kpp
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_32()
    return (Kpp,)


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_33():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-1.0 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_33()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
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
    The basic optimal control design, with

    $$
    Q = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix},
    $$

    and

    $$
    R = \begin{bmatrix}
    1
    \end{bmatrix},
    $$
    almost makes the job, except that it is a bit too fast and that results initially in large values of the angle $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_4():
        Q = np.eye(4,4)
        print("Q:", Q)
        R = np.eye(1) #10*l**2 * np.eye(1)
        print("R:", R)
        Pi = scipy.linalg.solve_continuous_are(
            a=A_lat, 
            b=B_lat, 
            q=Q, 
            r=R
        )
        Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_4()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A second design with the same $Q$ but $R$ increased by $100$ (to reduce the activation of the input at the price of some convergence speed) performs adequately!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Q = np.eye(4,4)
    print("Q:", Q)
    R = 100 * np.eye(1)
    print("R:", R)
    Pi = scipy.linalg.solve_continuous_are(
        a=A_lat, 
        b=B_lat, 
        q=Q, 
        r=R
    )
    Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

    def lin_sim_42():
        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_42()
    return (Koc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(Kpp, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Kpp.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(Koc, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Koc.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exact Linearization

    Let
    $$
    R(\alpha) =
    \begin{bmatrix} +\cos \alpha & -\sin \alpha \\ +\sin \alpha & +\cos \alpha
    \end{bmatrix}
    $$
    (réctifié)

    Consider an auxiliary system which is meant to compute the force $(f_x, f_y)$ applied to the booster.

    The inputs of the auxiliary system are

    $$
    v = (v_1, v_2) \in \mathbb{R}^2,
    $$

    its dynamics

    $$
    \ddot{z} = v_1 \qquad \text{ where } \qquad z \in \mathbb{R}
    $$

    and its output $(f_x, f_y) \in \mathbb{R}^2$ is given by

    \[
    \begin{bmatrix}
    f_x \\
    f_y
    \end{bmatrix} = R\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix}
    z - M\ell\dot{\theta}^2 / 6 \\
    {M\ell v_2}/{6z}
    \end{bmatrix}
    \]

    ⚠️ Note that the second component $f_y$ of the reactor force is undefined whenever $z=0$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Geometrical Interpretation


    Consider the output $h$ of the original system

    $$
    h :=
    \begin{bmatrix}
    x - (\ell/6) \sin \theta \\
    y + (\ell/6) \cos \theta
    \end{bmatrix} \in \mathbb{R}^2
    $$

    Provide a geometrical interpretation of $h$ (for example, make a drawing).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We define $\mathbf{b}$ such that :
    \[
    \mathbf{b} =
    \begin{pmatrix}
    -\sin\theta \\
    +\cos\theta
    \end{pmatrix}.
    \]

    We then recognize that:

    \[
    h =
    \begin{pmatrix}
    x \\
    y
    \end{pmatrix}
    +
    \frac{\ell}{6}\mathbf{b}.
    \]

    ### Conclusion

    The vector \( h \) represents the position of a point located on the booster axis, at a distance \( \ell/6 \) from the center of mass \( G \), in the upward direction along the booster axis.

    ---
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    def draw_h_geometry():
        # Parameters: booster of length l, tilted by theta
        l_val = 2.0
        theta = np.pi / 6   # 30° tilt for better visualization
        x_G, y_G = 0.0, 0.0  # center of mass located at the origin
    
        # Unit vector b along the booster axis
        bx, by = -np.sin(theta), np.cos(theta)
    
        # Key points
        P_top    = np.array([x_G + (l_val/2) * bx, y_G + (l_val/2) * by])  # top
        P_bot    = np.array([x_G - (l_val/2) * bx, y_G - (l_val/2) * by])  # base
        G        = np.array([x_G, y_G])
        h_point  = np.array([x_G + (l_val/6) * bx, y_G + (l_val/6) * by])
    
        # Figure
        fig, ax = plt.subplots(figsize=(8, 9))
    
        # Reference vertical axis (gray dotted line) through G
        ax.plot([x_G, x_G], [y_G - 1.4, y_G + 1.4],
                color='gray', linestyle=':', linewidth=1, alpha=0.6)
    
        # Booster body: thin rectangle oriented along b
        width = 0.10
        perp = np.array([-by, bx])  # vector perpendicular to b
        corners = np.array([
            P_bot - width/2 * perp,
            P_bot + width/2 * perp,
            P_top + width/2 * perp,
            P_top - width/2 * perp,
        ])
        booster = plt.Polygon(corners, closed=True,
                              facecolor='#2c3e50', edgecolor='black', linewidth=1.5)
        ax.add_patch(booster)
    
        # Booster axis (dashed line for visualization)
        extension = 1.3
        axe_haut = G + extension * (l_val/2) * np.array([bx, by])
        axe_bas  = G - extension * (l_val/2) * np.array([bx, by])
        ax.plot([axe_bas[0], axe_haut[0]], [axe_bas[1], axe_haut[1]],
                color='#2c3e50', linestyle='--', linewidth=1, alpha=0.5)
    
        # Key points
        ax.plot(*G,       'o', color='#e74c3c', markersize=12, zorder=5)
        ax.plot(*h_point, 'o', color='#27ae60', markersize=14, zorder=5)
        ax.plot(*P_top,   's', color='#3498db', markersize=10, zorder=5)
        ax.plot(*P_bot,   's', color='#9b59b6', markersize=10, zorder=5)
    
        # Labels
        offset = 0.18
        ax.annotate(r'$G$  (center of mass)',
                    xy=G, xytext=(G[0] + offset, G[1] - 0.05),
                    fontsize=13, color='#e74c3c', fontweight='bold')
        ax.annotate(r'$h$  ($\ell/6$ above $G$)',
                    xy=h_point, xytext=(h_point[0] + offset, h_point[1]),
                    fontsize=13, color='#27ae60', fontweight='bold')
        ax.annotate(r'top  ($\ell/2$ above $G$)',
                    xy=P_top, xytext=(P_top[0] + offset, P_top[1]),
                    fontsize=11, color='#3498db')
        ax.annotate(r'base $P$  (engine application point)',
                    xy=P_bot, xytext=(P_bot[0] + offset, P_bot[1]),
                    fontsize=11, color='#9b59b6')
    
        # Arrow showing the distance l/6
        mid_h = (G + h_point) / 2
        perp_label = np.array([-by, bx])
        arrow_offset = mid_h - 0.35 * perp_label
        ax.annotate('', xy=h_point - 0.30 * perp_label,
                    xytext=G - 0.30 * perp_label,
                    arrowprops=dict(arrowstyle='<->', color='#27ae60', lw=1.5))
        ax.text(*(arrow_offset - 0.05 * perp_label),
                r'$\ell/6$', fontsize=14, color='#27ae60',
                ha='center', va='center', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor='#27ae60'))
    
        # Angle theta between the vertical axis and the booster axis
        arc_r = 0.35
        arc_angles = np.linspace(np.pi/2, np.pi/2 + theta, 30)
        arc_x = x_G + arc_r * np.cos(arc_angles)
        arc_y = y_G + arc_r * np.sin(arc_angles)
        ax.plot(arc_x, arc_y, color='black', lw=1.2)
        ax.text(x_G - 0.05, y_G + arc_r + 0.10, r'$\theta$',
                fontsize=14, ha='center')
    
        # Vector b
        ax.annotate('', xy=G + 0.5 * np.array([bx, by]), xytext=G,
                    arrowprops=dict(arrowstyle='->', color='#16a085', lw=2))
        ax.text(*(G + 0.55 * np.array([bx, by]) + 0.1 * perp_label),
                r'$\vec{b}$', fontsize=15, color='#16a085', fontweight='bold')
    
        # Final formatting
        ax.set_xlim(-1.6, 2.2)
        ax.set_ylim(-1.8, 2.0)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title(
            r"Geometric interpretation of $h$: "
            r"point located on the booster axis, at $\ell/6$ above $G$",
            fontsize=12)
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
    
        plt.tight_layout()
        return plt.gcf()

    draw_h_geometry()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 First and Second-Order Derivatives

    Compute $\dot{h}$ as a function of $\dot{x}$, $\dot{y}$, $\theta$ and $\dot{\theta}$ (and constants) and then $\ddot{h}$ as a function of $\theta$ and $z$ (and constants) when the auxiliary system is plugged in the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    The output is
    $$h = \begin{pmatrix} x - (\ell/6)\sin\theta \\ y + (\ell/6)\cos\theta \end{pmatrix}.$$

    The rotation matrix used in the auxiliary system is
    $$R(\alpha) = \begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & +\cos\alpha \end{pmatrix}.$$

    Time derivatives of trigonometric functions:
    $$\frac{d}{dt}\sin\theta = \cos\theta \cdot \dot\theta, \qquad \frac{d}{dt}\cos\theta = -\sin\theta \cdot \dot\theta.$$

    ---

    ## Step 1: first derivative $\dot h$

    Differentiate $h$ component by component.

    For the first component:
    $$\frac{d}{dt}\big( x - (\ell/6)\sin\theta \big) = \dot x - (\ell/6)\cos\theta \cdot \dot\theta.$$

    For the second component:
    $$\frac{d}{dt}\big( y + (\ell/6)\cos\theta \big) = \dot y - (\ell/6)\sin\theta \cdot \dot\theta.$$

    So:
    $$\boxed{\dot h = \begin{pmatrix} \dot x - (\ell/6)\cos\theta \cdot \dot\theta \\ \dot y - (\ell/6)\sin\theta \cdot \dot\theta \end{pmatrix}}.$$

    This depends only on $\dot x, \dot y, \theta, \dot\theta$, as required.

    ---

    ## Step 2: second derivative $\ddot h$ (kinematic form)

    Differentiate again, component by component.

    **First component.** Differentiate $\dot x - (\ell/6)\cos\theta \cdot \dot\theta$ using the product rule:
    $$\ddot x - (\ell/6)\big[ -\sin\theta \cdot \dot\theta \cdot \dot\theta + \cos\theta \cdot \ddot\theta \big] = \ddot x + (\ell/6)\sin\theta \cdot \dot\theta^2 - (\ell/6)\cos\theta \cdot \ddot\theta.$$

    **Second component.** Differentiate $\dot y - (\ell/6)\sin\theta \cdot \dot\theta$ similarly:
    $$\ddot y - (\ell/6)\big[ \cos\theta \cdot \dot\theta \cdot \dot\theta + \sin\theta \cdot \ddot\theta \big] = \ddot y - (\ell/6)\cos\theta \cdot \dot\theta^2 - (\ell/6)\sin\theta \cdot \ddot\theta.$$

    So:
    $$\ddot h = \begin{pmatrix} \ddot x + (\ell/6)\sin\theta \cdot \dot\theta^2 - (\ell/6)\cos\theta \cdot \ddot\theta \\ \ddot y - (\ell/6)\cos\theta \cdot \dot\theta^2 - (\ell/6)\sin\theta \cdot \ddot\theta \end{pmatrix}. \tag{$\star$}$$

    ---

    ## Step 3: substitute Newton's equations

    From the dynamics:
    $$\ddot x = \frac{f_x}{M}, \qquad \ddot y = \frac{f_y}{M} - g, \qquad \ddot\theta = \frac{\tau}{J} \quad \text{with } J = \frac{M\ell^2}{12}.$$

    The torque about $G$ produced by the force $(f_x, f_y)$ applied at the base point $P$ (located at $G + ((\ell/2)\sin\theta, -(\ell/2)\cos\theta)^\top$) is:
    $$\tau = (\ell/2)\sin\theta \cdot f_y - \big(-(\ell/2)\cos\theta\big) \cdot f_x = (\ell/2)\big( \sin\theta \cdot f_y + \cos\theta \cdot f_x \big).$$

    Therefore:
    $$\ddot\theta = \frac{(\ell/2)(\sin\theta \cdot f_y + \cos\theta \cdot f_x)}{M\ell^2/12} = \frac{6}{M\ell}\big( \sin\theta \cdot f_y + \cos\theta \cdot f_x \big). \tag{$\tau$}$$

    ---

    ## Step 4: matrix calculation

    The auxiliary system gives:
    $$\begin{pmatrix} f_x \\ f_y \end{pmatrix} = R\!\left(\theta - \frac{\pi}{2}\right) \begin{pmatrix} z - M\ell\dot\theta^2/6 \\ M\ell\, v_2/(6z) \end{pmatrix}.$$

    ### Step 4a — Compute $R(\theta - \pi/2)$ explicitly

    Using $\cos(\theta - \pi/2) = \sin\theta$ and $\sin(\theta - \pi/2) = -\cos\theta$:
    $$R\!\left(\theta - \frac{\pi}{2}\right) = \begin{pmatrix} \cos(\theta-\pi/2) & -\sin(\theta-\pi/2) \\ \sin(\theta-\pi/2) & +\cos(\theta-\pi/2) \end{pmatrix} = \begin{pmatrix} \sin\theta & \cos\theta \\ -\cos\theta & \sin\theta \end{pmatrix}.$$

    ### Step 4b — Perform the matrix-vector product

    Let $A = z - M\ell\dot\theta^2/6$ and $B = M\ell v_2/(6z)$:
    $$\begin{pmatrix} f_x \\ f_y \end{pmatrix} = \begin{pmatrix} \sin\theta & \cos\theta \\ -\cos\theta & \sin\theta \end{pmatrix} \begin{pmatrix} A \\ B \end{pmatrix} = \begin{pmatrix} A\sin\theta + B\cos\theta \\ -A\cos\theta + B\sin\theta \end{pmatrix}.$$

    Writing out $A$ and $B$:
    $$f_x = \left( z - \frac{M\ell\dot\theta^2}{6} \right)\sin\theta + \frac{M\ell v_2}{6z}\,\cos\theta,$$
    $$f_y = -\left( z - \frac{M\ell\dot\theta^2}{6} \right)\cos\theta + \frac{M\ell v_2}{6z}\,\sin\theta.$$

    ### Step 4c — Compute $\ddot x = f_x/M$ and $\ddot y = f_y/M - g$

    Dividing by $M$:
    $$\ddot x = \left( \frac{z}{M} - \frac{\ell\dot\theta^2}{6} \right)\sin\theta + \frac{\ell v_2}{6z}\,\cos\theta,$$
    $$\ddot y = -\left( \frac{z}{M} - \frac{\ell\dot\theta^2}{6} \right)\cos\theta + \frac{\ell v_2}{6z}\,\sin\theta - g.$$

    ### Step 4d — Compute $\ddot\theta$ via formula $(\tau)$

    We need $\sin\theta \cdot f_y + \cos\theta \cdot f_x$:
    $$\sin\theta \cdot f_y = -\left( z - \frac{M\ell\dot\theta^2}{6} \right)\sin\theta\cos\theta + \frac{M\ell v_2}{6z}\sin^2\theta,$$
    $$\cos\theta \cdot f_x = \left( z - \frac{M\ell\dot\theta^2}{6} \right)\sin\theta\cos\theta + \frac{M\ell v_2}{6z}\cos^2\theta.$$

    Adding: the two $\sin\theta\cos\theta$ terms **cancel**, and $\sin^2\theta + \cos^2\theta = 1$:
    $$\sin\theta \cdot f_y + \cos\theta \cdot f_x = \frac{M\ell v_2}{6z}.$$

    Therefore:
    $$\ddot\theta = \frac{6}{M\ell} \cdot \frac{M\ell v_2}{6z} = \frac{v_2}{z}.$$

    ### Step 4e — Assemble $\ddot h$ from $(\star)$, first component

    $$\ddot h_1 = \ddot x + (\ell/6)\sin\theta \cdot \dot\theta^2 - (\ell/6)\cos\theta \cdot \ddot\theta.$$

    Substitute $\ddot x$ and $\ddot\theta = v_2/z$:
    $$\ddot h_1 = \left( \frac{z}{M} - \frac{\ell\dot\theta^2}{6} \right)\sin\theta + \frac{\ell v_2}{6z}\cos\theta + \frac{\ell\dot\theta^2 \sin\theta}{6} - \frac{\ell v_2 \cos\theta}{6z}.$$

    Group:
    - **$\dot\theta^2$ terms:** $-\dfrac{\ell\dot\theta^2 \sin\theta}{6} + \dfrac{\ell\dot\theta^2 \sin\theta}{6} = 0$. ✓
    - **$v_2$ terms:** $+\dfrac{\ell v_2 \cos\theta}{6z} - \dfrac{\ell v_2 \cos\theta}{6z} = 0$. ✓

    What's left:
    $$\ddot h_1 = +\frac{z}{M}\sin\theta.$$

    ### Step 4f — Assemble $\ddot h$ from $(\star)$, second component

    $$\ddot h_2 = \ddot y - (\ell/6)\cos\theta \cdot \dot\theta^2 - (\ell/6)\sin\theta \cdot \ddot\theta.$$

    Substitute:
    $$\ddot h_2 = -\left( \frac{z}{M} - \frac{\ell\dot\theta^2}{6} \right)\cos\theta + \frac{\ell v_2}{6z}\sin\theta - g - \frac{\ell\dot\theta^2 \cos\theta}{6} - \frac{\ell v_2 \sin\theta}{6z}.$$

    Group:
    - **$\dot\theta^2$ terms:** $+\dfrac{\ell\dot\theta^2 \cos\theta}{6} - \dfrac{\ell\dot\theta^2 \cos\theta}{6} = 0$. ✓
    - **$v_2$ terms:** $+\dfrac{\ell v_2 \sin\theta}{6z} - \dfrac{\ell v_2 \sin\theta}{6z} = 0$. ✓

    What's left:
    $$\ddot h_2 = -\frac{z}{M}\cos\theta - g.$$

    ### Step 4g — Final result

    $$\boxed{\;\ddot h = \begin{pmatrix} +\dfrac{z}{M}\sin\theta \\[6pt] -\dfrac{z}{M}\cos\theta - g \end{pmatrix} = \frac{z}{M}\begin{pmatrix} +\sin\theta \\ -\cos\theta \end{pmatrix} + \begin{pmatrix} 0 \\ -g \end{pmatrix}.\;}$$

    This depends only on $\theta$ and $z$ — no more $\dot\theta^2$, no more $v_2$, no more $\dot x, \dot y$. Mission accomplished.

    ---

    ## What this really means

    Look at the boxed result. It says something very simple:

    > The acceleration of $h$ is just **gravity plus a thrust along the booster's body axis**.

    The vector $(+\sin\theta, -\cos\theta)$ is exactly the unit vector pointing from the top of the booster down toward its base — the direction in which the reactor pushes the body. And the scalar $z/M$ is the magnitude of that thrust.

    So the booster, viewed through the output $h$, behaves like a **simple point mass with a controllable thrust** along its axis. No coupling with rotation, no quadratic velocity term, no rotational inertia effect. The system has become as simple as a rocket in a video game.

    This is the whole point of introducing the auxiliary variable $z$. By choosing the formula for $(f_x, f_y)$ very carefully, every awkward term that appears in the differentiation ($\dot\theta^2$ from rotation, $v_2$ from angular acceleration) is matched by an equal and opposite term coming from $f_x, f_y$. The two sets of terms erase each other, and what survives is the clean expression above.

    The variable $z$ plays the role of a "thrust knob." Since $\ddot z = v_1$, controlling $z$ is just controlling a double integrator — the easiest object in control theory. We trade a hard nonlinear problem for a much simpler one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Third and Fourth-Order Derivatives

    Compute the third derivative $h^{(3)}$ of $h$ as a function of $\theta$ and $z$ (and constants) and then the fourth derivative $h^{(4)}$ of $h$ with respect to time as a function of $\theta$, $\dot{\theta}$, $z$, $\dot{z}$, $v$ (and constants) when the auxiliary system is on.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    From the previous calculation:
    $$\ddot h = \begin{pmatrix} +\dfrac{z}{M}\sin\theta \\[6pt] -\dfrac{z}{M}\cos\theta - g \end{pmatrix}.$$

    We also have the dynamics of the auxiliary system:
    $$\ddot z = v_1, \qquad \ddot\theta = \frac{v_2}{z}.$$

    The goal is to differentiate $\ddot h$ once to get $h^{(3)}$, then a second time to get $h^{(4)}$.

    ---

    ## Step 1: third derivative $h^{(3)}$

    We differentiate $\ddot h$ component by component. The gravity term $-g$ is constant, so it disappears.

    ### Step 1a — First component

    Differentiate $\ddot h_1 = \dfrac{z}{M}\sin\theta$ using the product rule (both $z$ and $\sin\theta$ are functions of time):
    $$h^{(3)}_1 = \frac{d}{dt}\!\left( \frac{z}{M}\sin\theta \right) = \frac{\dot z}{M}\sin\theta + \frac{z}{M}\cos\theta \cdot \dot\theta = \frac{\dot z}{M}\sin\theta + \frac{z\dot\theta}{M}\cos\theta.$$

    ### Step 1b — Second component

    Differentiate $\ddot h_2 = -\dfrac{z}{M}\cos\theta - g$ similarly:
    $$h^{(3)}_2 = \frac{d}{dt}\!\left( -\frac{z}{M}\cos\theta \right) = -\frac{\dot z}{M}\cos\theta - \frac{z}{M}(-\sin\theta) \cdot \dot\theta = -\frac{\dot z}{M}\cos\theta + \frac{z\dot\theta}{M}\sin\theta.$$

    ### Step 1c — Final expression

    $$\boxed{\;h^{(3)} = \begin{pmatrix} +\dfrac{\dot z}{M}\sin\theta + \dfrac{z\dot\theta}{M}\cos\theta \\[8pt] -\dfrac{\dot z}{M}\cos\theta + \dfrac{z\dot\theta}{M}\sin\theta \end{pmatrix}.\;}$$

    This depends only on $\theta, \dot\theta, z, \dot z$ — no inputs yet, as required.

    ---

    ## Step 2: fourth derivative $h^{(4)}$

    Now we differentiate $h^{(3)}$ component by component. The inputs $v_1$ and $v_2$ finally appear, because:
    - differentiating $\dot z$ gives $\ddot z = v_1$,
    - differentiating $\dot\theta$ gives $\ddot\theta = v_2/z$.

    ### Step 2a — First component

    Start from:
    $$h^{(3)}_1 = \frac{\dot z}{M}\sin\theta + \frac{z\dot\theta}{M}\cos\theta.$$

    **Differentiate $\dfrac{\dot z}{M}\sin\theta$:**
    $$\frac{d}{dt}\!\left( \frac{\dot z}{M}\sin\theta \right) = \frac{\ddot z}{M}\sin\theta + \frac{\dot z}{M}\cos\theta \cdot \dot\theta = \frac{v_1}{M}\sin\theta + \frac{\dot z \dot\theta}{M}\cos\theta,$$
    using $\ddot z = v_1$.

    **Differentiate $\dfrac{z\dot\theta}{M}\cos\theta$.** First, we need the derivative of $z\dot\theta$ (a product):
    $$\frac{d}{dt}(z\dot\theta) = \dot z \cdot \dot\theta + z \cdot \ddot\theta = \dot z \dot\theta + z \cdot \frac{v_2}{z} = \dot z \dot\theta + v_2.$$

    Then, applying the product rule on the whole term:
    $$\frac{d}{dt}\!\left( \frac{z\dot\theta}{M}\cos\theta \right) = \frac{\dot z\dot\theta + v_2}{M}\cos\theta + \frac{z\dot\theta}{M}(-\sin\theta) \cdot \dot\theta = \frac{\dot z\dot\theta}{M}\cos\theta + \frac{v_2}{M}\cos\theta - \frac{z\dot\theta^2}{M}\sin\theta.$$

    **Sum:**
    $$h^{(4)}_1 = \frac{v_1}{M}\sin\theta + \frac{\dot z \dot\theta}{M}\cos\theta + \frac{\dot z\dot\theta}{M}\cos\theta + \frac{v_2}{M}\cos\theta - \frac{z\dot\theta^2}{M}\sin\theta.$$

    The two $\dfrac{\dot z\dot\theta}{M}\cos\theta$ terms combine:
    $$h^{(4)}_1 = \frac{v_1}{M}\sin\theta + \frac{2\dot z\dot\theta}{M}\cos\theta + \frac{v_2}{M}\cos\theta - \frac{z\dot\theta^2}{M}\sin\theta.$$

    Factor by grouping the $\sin\theta$ and $\cos\theta$ terms:
    $$h^{(4)}_1 = \frac{1}{M}\!\left[\,( v_1 - z\dot\theta^2 )\sin\theta + (v_2 + 2\dot z\dot\theta)\cos\theta\,\right].$$

    ### Step 2b — Second component

    Start from:
    $$h^{(3)}_2 = -\frac{\dot z}{M}\cos\theta + \frac{z\dot\theta}{M}\sin\theta.$$

    **Differentiate $-\dfrac{\dot z}{M}\cos\theta$:**
    $$\frac{d}{dt}\!\left( -\frac{\dot z}{M}\cos\theta \right) = -\frac{\ddot z}{M}\cos\theta - \frac{\dot z}{M}(-\sin\theta)\cdot\dot\theta = -\frac{v_1}{M}\cos\theta + \frac{\dot z\dot\theta}{M}\sin\theta.$$

    **Differentiate $\dfrac{z\dot\theta}{M}\sin\theta$**, using again $\dfrac{d}{dt}(z\dot\theta) = \dot z\dot\theta + v_2$:
    $$\frac{d}{dt}\!\left( \frac{z\dot\theta}{M}\sin\theta \right) = \frac{\dot z\dot\theta + v_2}{M}\sin\theta + \frac{z\dot\theta}{M}\cos\theta \cdot \dot\theta = \frac{\dot z\dot\theta}{M}\sin\theta + \frac{v_2}{M}\sin\theta + \frac{z\dot\theta^2}{M}\cos\theta.$$

    **Sum:**
    $$h^{(4)}_2 = -\frac{v_1}{M}\cos\theta + \frac{\dot z\dot\theta}{M}\sin\theta + \frac{\dot z\dot\theta}{M}\sin\theta + \frac{v_2}{M}\sin\theta + \frac{z\dot\theta^2}{M}\cos\theta.$$

    The two $\dfrac{\dot z\dot\theta}{M}\sin\theta$ terms combine:
    $$h^{(4)}_2 = -\frac{v_1}{M}\cos\theta + \frac{2\dot z\dot\theta}{M}\sin\theta + \frac{v_2}{M}\sin\theta + \frac{z\dot\theta^2}{M}\cos\theta.$$

    Factor by grouping:
    $$h^{(4)}_2 = \frac{1}{M}\!\left[\,-(v_1 - z\dot\theta^2)\cos\theta + (v_2 + 2\dot z\dot\theta)\sin\theta\,\right].$$

    ### Step 2c — Final expression

    Putting both components together:
    $$\boxed{\;h^{(4)} = \frac{1}{M}\begin{pmatrix} (v_1 - z\dot\theta^2)\sin\theta + (v_2 + 2\dot z\dot\theta)\cos\theta \\[6pt] -(v_1 - z\dot\theta^2)\cos\theta + (v_2 + 2\dot z\dot\theta)\sin\theta \end{pmatrix}.\;}$$

    This depends only on $\theta, \dot\theta, z, \dot z$ and the input $v = (v_1, v_2)$, as required.

    ---

    ## Structure of the result

    The expression above can be rewritten in matrix form:
    $$h^{(4)} = \frac{1}{M}\begin{pmatrix} \sin\theta & \cos\theta \\ -\cos\theta & \sin\theta \end{pmatrix}\begin{pmatrix} v_1 - z\dot\theta^2 \\ v_2 + 2\dot z\dot\theta \end{pmatrix}.$$

    The matrix is exactly $R(\theta - \pi/2)$ from the previous step. The relation between the input $v$ and $h^{(4)}$ is **affine**:
    $$h^{(4)} = \underbrace{\frac{1}{M}\,R\!\left(\theta - \frac{\pi}{2}\right)}_{\text{matrix in } \theta} v \;+\; \underbrace{\frac{1}{M}\,R\!\left(\theta - \frac{\pi}{2}\right)\begin{pmatrix} -z\dot\theta^2 \\ 2\dot z\dot\theta \end{pmatrix}}_{\text{residual in } \theta, \dot\theta, z, \dot z}.$$

    The matrix $\frac{1}{M}R(\theta - \pi/2)$ is invertible for every $\theta$ (a rotation is always invertible, $\det = 1$). This means we can pick any desired $h^{(4)}$ and recover the input $v$ that produces it.

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Exact Linearization

    Show that with yet another auxiliary system with input $u=(u_1, u_2)$ and output $v$ fed into the previous one, we can achieve the dynamics

    $$
    h^{(4)} = u
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    From the previous step, we have the affine relation
    $$h^{(4)} = \frac{1}{M}\,R\!\left(\theta - \frac{\pi}{2}\right)\begin{pmatrix} v_1 - z\dot\theta^2 \\ v_2 + 2\dot z\dot\theta \end{pmatrix},$$
    with
    $$R\!\left(\theta - \frac{\pi}{2}\right) = \begin{pmatrix} \sin\theta & \cos\theta \\ -\cos\theta & \sin\theta \end{pmatrix}.$$

    The map $v \mapsto h^{(4)}$ is invertible for every $\theta$, since $R(\theta - \pi/2)$ is a rotation ($\det = 1$).

    We now want to find a rule $u \mapsto v$ such that, when plugged in, the system satisfies
    $$h^{(4)} = u.$$

    ---

    ## Step 1: invert the relation

    Set $h^{(4)} = u$ and solve for $v$. Starting from
    $$u = \frac{1}{M}\,R\!\left(\theta - \frac{\pi}{2}\right)\begin{pmatrix} v_1 - z\dot\theta^2 \\ v_2 + 2\dot z\dot\theta \end{pmatrix},$$
    we multiply both sides by $M \cdot R(\theta - \pi/2)^{-1}$:
    $$\begin{pmatrix} v_1 - z\dot\theta^2 \\ v_2 + 2\dot z\dot\theta \end{pmatrix} = M\,R\!\left(\theta - \frac{\pi}{2}\right)^{-1} u.$$

    ## Step 2: compute the inverse rotation

    For any rotation, $R(\alpha)^{-1} = R(-\alpha) = R(\alpha)^\top$. So:
    $$R\!\left(\theta - \frac{\pi}{2}\right)^{-1} = \begin{pmatrix} \sin\theta & -\cos\theta \\ \cos\theta & \sin\theta \end{pmatrix}.$$

    A quick check: multiplying the original matrix by its transpose,
    $$\begin{pmatrix} \sin\theta & \cos\theta \\ -\cos\theta & \sin\theta \end{pmatrix}\begin{pmatrix} \sin\theta & -\cos\theta \\ \cos\theta & \sin\theta \end{pmatrix} = \begin{pmatrix} \sin^2\theta + \cos^2\theta & 0 \\ 0 & \sin^2\theta + \cos^2\theta \end{pmatrix} = I_2. \checkmark$$

    ## Step 3: write out $v$ as a function of $u$

    Carry out the product $M\,R(\theta - \pi/2)^{-1}\,u$:
    $$M\begin{pmatrix} \sin\theta & -\cos\theta \\ \cos\theta & \sin\theta \end{pmatrix}\begin{pmatrix} u_1 \\ u_2 \end{pmatrix} = M\begin{pmatrix} u_1\sin\theta - u_2\cos\theta \\ u_1\cos\theta + u_2\sin\theta \end{pmatrix}.$$

    Therefore:
    $$v_1 - z\dot\theta^2 = M\big(u_1\sin\theta - u_2\cos\theta\big),$$
    $$v_2 + 2\dot z\dot\theta = M\big(u_1\cos\theta + u_2\sin\theta\big).$$

    Isolating $v_1$ and $v_2$:
    $$\boxed{\;\begin{aligned} v_1 &= M\big(u_1\sin\theta - u_2\cos\theta\big) + z\,\dot\theta^2, \\[4pt] v_2 &= M\big(u_1\cos\theta + u_2\sin\theta\big) - 2\,\dot z\,\dot\theta. \end{aligned}\;}$$

    This is the **second auxiliary system**. It is a purely *static* feedback (no internal state): it takes as input the new control $u = (u_1, u_2)$ along with the values of $\theta, \dot\theta, z, \dot z$, and produces $v = (v_1, v_2)$.

    ---

    ## Step 4: verification

    Plug this $v$ back into the formula for $h^{(4)}$. With $v_1 - z\dot\theta^2 = M(u_1\sin\theta - u_2\cos\theta)$ and $v_2 + 2\dot z\dot\theta = M(u_1\cos\theta + u_2\sin\theta)$:
    $$h^{(4)} = \frac{1}{M}\begin{pmatrix} \sin\theta & \cos\theta \\ -\cos\theta & \sin\theta \end{pmatrix}\begin{pmatrix} M(u_1\sin\theta - u_2\cos\theta) \\ M(u_1\cos\theta + u_2\sin\theta) \end{pmatrix}.$$

    The $M$ cancels. Compute the matrix–vector product:

    **First component:**
    $$\sin\theta \cdot (u_1\sin\theta - u_2\cos\theta) + \cos\theta \cdot (u_1\cos\theta + u_2\sin\theta)$$
    $$= u_1\sin^2\theta - u_2\sin\theta\cos\theta + u_1\cos^2\theta + u_2\sin\theta\cos\theta = u_1\,(\sin^2\theta + \cos^2\theta) = u_1. \checkmark$$

    **Second component:**
    $$-\cos\theta \cdot (u_1\sin\theta - u_2\cos\theta) + \sin\theta \cdot (u_1\cos\theta + u_2\sin\theta)$$
    $$= -u_1\sin\theta\cos\theta + u_2\cos^2\theta + u_1\sin\theta\cos\theta + u_2\sin^2\theta = u_2\,(\sin^2\theta + \cos^2\theta) = u_2. \checkmark$$

    So:
    $$\boxed{\;h^{(4)} = u.\;}$$

    ---

    ## Summary of the cascade

    The full chain of feedbacks now reads:

    1. **Outer input:** $u = (u_1, u_2)$ — the new "virtual" control.
    2. **Second auxiliary system** (static, the one we just designed):
    $$v_1 = M(u_1\sin\theta - u_2\cos\theta) + z\dot\theta^2, \qquad v_2 = M(u_1\cos\theta + u_2\sin\theta) - 2\dot z\dot\theta.$$
    3. **First auxiliary system** (dynamic, given in the problem statement):
    $$\ddot z = v_1, \qquad \begin{pmatrix} f_x \\ f_y \end{pmatrix} = R\!\left(\theta - \frac{\pi}{2}\right)\begin{pmatrix} z - M\ell\dot\theta^2/6 \\ M\ell\, v_2/(6z) \end{pmatrix}.$$
    4. **Booster** (the original nonlinear system) driven by $(f_x, f_y)$.

    Viewed from the new input $u$ to the flat output $h$, the entire booster system becomes
    $$h^{(4)}_1 = u_1, \qquad h^{(4)}_2 = u_2.$$

    That is, **two independent chains of four integrators** — the simplest possible linear system. The nonlinearities have not been ignored or approximated: they have been **exactly cancelled** by the cascade of feedbacks.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 State to Derivatives of the Output

    Implement a function `Tr` of `x, dx, y, dy, theta, dtheta, z, dz` that returns `h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The formulas to implement are exactly those we derived in the previous steps:

    $$h=\begin{pmatrix}x-(\ell/6)\sin\theta\\ y+(\ell/6)\cos\theta\end{pmatrix},\qquad \dot h=\begin{pmatrix}\dot x-(\ell/6)\cos\theta\cdot\dot\theta\\ \dot y-(\ell/6)\sin\theta\cdot\dot\theta\end{pmatrix}$$

    $$\ddot h=\begin{pmatrix}(z/M)\sin\theta\\ -(z/M)\cos\theta-g\end{pmatrix},\qquad h^{(3)}=\begin{pmatrix}(\dot z/M)\sin\theta+(z\dot\theta/M)\cos\theta\\ -(\dot z/M)\cos\theta+(z\dot\theta/M)\sin\theta\end{pmatrix}$$

    Each line of code below corresponds directly to one of these formulas.
    """)
    return


@app.cell
def _(M, g, l, np):
    def Tr(x, dx, y, dy, theta, dtheta, z, dz):

        s = np.sin(theta)
        c = np.cos(theta)
    
        # h
        h_x = x - (l / 6) * s
        h_y = y + (l / 6) * c
    
        # dh
        dh_x = dx - (l / 6) * c * dtheta
        dh_y = dy - (l / 6) * s * dtheta
    
        # d2h
        d2h_x =  (z / M) * s
        d2h_y = -(z / M) * c - g
    
        # d3h
        d3h_x =  (dz / M) * s + (z * dtheta / M) * c
        d3h_y = -(dz / M) * c + (z * dtheta / M) * s
    
        return h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y

    return (Tr,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Inversion


    Assume for the sake of simplicity that $z<0$ at all times. Show that given the values of $h$, $\dot{h}$, $\ddot{h}$ and $h^{(3)}$, one can uniquely compute the booster state (the values of $x$, $\dot{x}$, $y$, $\dot{y}$, $\theta$, $\dot{\theta}$) and auxiliary system state (the values of $z$ and $\dot{z}$).

    Implement the corresponding function `T_inv`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    \[
    T_r : (x,\dot x,y,\dot y,\theta,\dot\theta,z,\dot z) \mapsto (h,\dot h,\ddot h,h^{(3)})
    \]

    The objective is to reconstruct the full booster state and auxiliary system state from:

    \[
    (h,\dot h,\ddot h,h^{(3)})
    \]

    assuming:

    \[
    z < 0
    \]

    ---

    # 1. Recovering \(z\)

    From the transformation:

    \[
    \ddot h_x = \frac{z}{M}\sin\theta
    \]

    and

    \[
    \ddot h_y = -\frac{z}{M}\cos\theta - g
    \]

    we obtain:

    \[
    \ddot h_y + g = -\frac{z}{M}\cos\theta
    \]

    Squaring and summing:

    \[
    (\ddot h_x)^2 + (\ddot h_y + g)^2 = \frac{z^2}{M^2}
    \]

    since:

    \[
    \sin^2\theta + \cos^2\theta = 1
    \]

    Thus:

    \[
    |z| = M\sqrt{(\ddot h_x)^2 + (\ddot h_y + g)^2}
    \]

    Because the assumption imposes:

    \[
    z < 0
    \]

    we uniquely obtain:

    \[
    z = -M\sqrt{(\ddot h_x)^2 + (\ddot h_y + g)^2}
    \]

    ---

    # 2. Recovering \(\theta\)

    Using:

    \[
    \sin\theta = \frac{M\ddot h_x}{z}
    \]

    and

    \[
    \cos\theta = -\frac{M(\ddot h_y+g)}{z}
    \]

    we reconstruct:

    \[
    \theta = \operatorname{atan2}\left(\frac{M\ddot h_x}{z},-\frac{M(\ddot h_y+g)}{z}\right)
    \]

    The use of `atan2` guarantees the correct quadrant.

    ---

    # 3. Recovering \(\dot z\) and \(\dot\theta\)

    From:

    \[
    h_x^{(3)} = \frac{\dot z}{M}\sin\theta + \frac{z\dot\theta}{M}\cos\theta
    \]

    and

    \[
    h_y^{(3)} = -\frac{\dot z}{M}\cos\theta + \frac{z\dot\theta}{M}\sin\theta
    \]

    we obtain the linear system:

    \[
    M\begin{pmatrix}h_x^{(3)} \\ h_y^{(3)}\end{pmatrix} = \begin{pmatrix}\sin\theta & z\cos\theta \\ -\cos\theta & z\sin\theta\end{pmatrix}\begin{pmatrix}\dot z \\ \dot\theta\end{pmatrix}
    \]

    The determinant is:

    \[
    \det = z
    \]

    which is nonzero because:

    \[
    z < 0
    \]

    Therefore the system is invertible.

    ---

    # 4. Recovering \(x\) and \(y\)

    From:

    \[
    h_x = x - \frac{\ell}{6}\sin\theta
    \]

    and

    \[
    h_y = y + \frac{\ell}{6}\cos\theta
    \]

    we obtain:

    \[
    x = h_x + \frac{\ell}{6}\sin\theta
    \]

    and

    \[
    y = h_y - \frac{\ell}{6}\cos\theta
    \]

    ---

    # 5. Recovering \(\dot x\) and \(\dot y\)

    From:

    \[
    \dot h_x = \dot x - \frac{\ell}{6}\cos\theta\,\dot\theta
    \]

    and

    \[
    \dot h_y = \dot y - \frac{\ell}{6}\sin\theta\,\dot\theta
    \]

    we obtain:

    \[
    \dot x = \dot h_x + \frac{\ell}{6}\cos\theta\,\dot\theta
    \]

    and

    \[
    \dot y = \dot h_y + \frac{\ell}{6}\sin\theta\,\dot\theta
    \]

    ---

    # Conclusion

    The transformation \(T_r\) is invertible as long as:

    \[
    z \neq 0
    \]

    and under the imposed assumption:

    \[
    z < 0
    \]

    the inversion becomes unique.

    This proves that the output \(h\) is a flat output since the full state and auxiliary variables can be reconstructed from a finite number of derivatives of \(h\).
    """)
    return


@app.cell
def _(M, g, l, np):
    def Tr_inv(
        h_x, h_y,
        dh_x, dh_y,
        d2h_x, d2h_y,
        d3h_x, d3h_y
    ):

        z = -M * np.sqrt(
            d2h_x**2 +
            (d2h_y + g)**2
        )

        s = M * d2h_x / z
        c = -M * (d2h_y + g) / z

        theta = np.arctan2(s, c)

        A = np.array([
            [s, z * c],
            [-c, z * s]
        ])

        b = M * np.array([
            d3h_x,
            d3h_y
        ])

        dz, dtheta = np.linalg.solve(A, b)

        x = h_x + (l / 6) * s
        y = h_y - (l / 6) * c

        dx = dh_x + (l / 6) * c * dtheta
        dy = dh_y + (l / 6) * s * dtheta

        return (
            x, dx,
            y, dy,
            theta, dtheta,
            z, dz
        )

    return (Tr_inv,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Admissible Path Computation

    Implement a function

    ```python
    def compute(
        x_0,
        dx_0,
        y_0,
        dy_0,
        theta_0,
        dtheta_0,
        z_0,
        dz_0,
        x_tf,
        dx_tf,
        y_tf,
        dy_tf,
        theta_tf,
        dtheta_tf,
        z_tf,
        dz_tf,
        tf,
    ):
        ...

    ```

    that returns a function `fun` such that `fun(t)` is a value of `x, dx, y, dy, theta, dtheta, z, dz, f, phi` at time `t` that match the initial and final values provided as arguments to `compute`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before diving into individual lines, keep in mind what the function does at a high level. It receives the initial state of the booster, the desired final state, and the transit time $t_f$. It must return a function `fun(t)` that gives, for every $t \in [0, t_f]$, the full state of the booster together with the command $(f, \phi)$ to apply.

    The plan has three stages:

    1. Translate the initial and final states into **boundary conditions on $h(t)$**.
    2. Find the coefficients of the **degree-7 polynomial** that satisfies these conditions.
    3. Build `fun(t)` which, for each $t$, **evaluates the polynomial** and then reconstructs the state and command.

    ---

    ## Step 1 — the signature

    ```python
    def compute(
        x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0,
        x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf,
        tf,
    ):
    ```

    Nothing tricky here: 8 arguments for the initial state at $t = 0$, 8 arguments for the final state at $t = t_f$, plus $t_f$ itself — 17 parameters in total.

    Each state contains:
    - the position $(x, y)$ and velocity $(\dot x, \dot y)$ of the center of mass,
    - the angle $\theta$ and angular velocity $\dot\theta$,
    - the auxiliary variable $z$ and its derivative $\dot z$.

    ---

    ## Step 2 — translation to flat coordinates

    ```python
    H0  = Tr(x_0,  dx_0,  y_0,  dy_0,  theta_0,  dtheta_0,  z_0,  dz_0)
    Htf = Tr(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf)
    ```

    We use the `Tr` function we wrote earlier. Recall what it does: it takes the 8 variables of the full state (booster + auxiliary) and returns 8 numbers — the components of $h, \dot h, \ddot h, h^{(3)}$:
    $$\texttt{H} = (h_x,\, h_y,\, \dot h_x,\, \dot h_y,\, \ddot h_x,\, \ddot h_y,\, h^{(3)}_x,\, h^{(3)}_y).$$

    So `H0` contains the values of $h$ and its three derivatives **at $t = 0$**, and `Htf` the same **at $t = t_f$**.

    Why this translation? Because exact linearization taught us that **planning in the world of $h$ is trivial** (chain of 4 integrators), whereas planning in the world of $(x, y, \theta)$ is hard (coupled nonlinear). We move to the easy side right away.

    ---

    ## Step 3 — packing the boundary conditions

    ```python
    cx = np.array([H0[0], H0[2], H0[4], H0[6], Htf[0], Htf[2], Htf[4], Htf[6]])
    cy = np.array([H0[1], H0[3], H0[5], H0[7], Htf[1], Htf[3], Htf[5], Htf[7]])
    ```

    We will build **two separate polynomials**: one for $h_x(t)$, one for $h_y(t)$. Each must satisfy 8 conditions.

    For $h_x$:
    - even indices of `H0` = $h_x,\, \dot h_x,\, \ddot h_x,\, h^{(3)}_x$ **at $t = 0$**,
    - even indices of `Htf` = the same **at $t = t_f$**.

    8 conditions total, packed into `cx`. Likewise for $h_y$ with odd indices, packed into `cy`.

    The chosen order is: value, first derivative, second derivative, third derivative — first at $t = 0$, then at $t = t_f$. This order must match exactly the row order of the matrix we build next.

    ---

    ## Step 4 — building the linear system

    We are looking for a polynomial $p(t) = a_0 + a_1 t + a_2 t^2 + \dots + a_7 t^7$, so 8 coefficients $a_0, \dots, a_7$ to determine. Each of the 8 conditions is one **linear equation** in these coefficients. We will solve $V \cdot a = c$ where $V$ is an $8 \times 8$ matrix.

    ```python
    V = np.zeros((8, 8))
    ```

    Initialize the matrix to zero.

    **Recall the general formula** for the $k$-th derivative of a polynomial. If $p(t) = \sum_n a_n t^n$, then:
    $$p^{(k)}(t) = \sum_{n \geq k} \frac{n!}{(n-k)!}\, a_n\, t^{n-k}.$$

    For example:
    - $p^{(0)}(t) = p(t) = a_0 + a_1 t + a_2 t^2 + \dots$
    - $p^{(1)}(t) = a_1 + 2 a_2 t + 3 a_3 t^2 + \dots$
    - $p^{(2)}(t) = 2 a_2 + 6 a_3 t + 12 a_4 t^2 + \dots$

    The coefficient $\frac{n!}{(n-k)!}$ is the **falling factorial**, equal to $n \times (n-1) \times \dots \times (n-k+1)$.

    **Evaluation at $t = 0$.** When we evaluate $p^{(k)}(0)$, all terms with $t^{n-k}$ for $n > k$ vanish, and only the $n = k$ term survives:
    $$p^{(k)}(0) = \frac{k!}{0!}\, a_k = k!\, a_k.$$

    This motivates these lines:

    ```python
    for k in range(4):
        V[k, k] = factorial(k)
    ```

    For $k = 0, 1, 2, 3$, we fill `V[k, k] = k!` (the other entries of row $k$ remain zero). Concretely:
    - row 0: `V[0, 0] = 1` → equation $a_0 = c_0$, i.e. $p(0) = h(0)$.
    - row 1: `V[1, 1] = 1` → equation $a_1 = c_1$, i.e. $\dot p(0) = \dot h(0)$.
    - row 2: `V[2, 2] = 2` → equation $2 a_2 = c_2$, i.e. $\ddot p(0) = \ddot h(0)$.
    - row 3: `V[3, 3] = 6` → equation $6 a_3 = c_3$, i.e. $p^{(3)}(0) = h^{(3)}(0)$.

    The first 4 rows are almost trivial: they say that $a_0, a_1, a_2, a_3$ are essentially determined by the conditions at $t = 0$.

    **Evaluation at $t = t_f$.** For the 4 conditions at $t = t_f$, all terms contribute:

    ```python
        for n in range(k, 8):
            V[k + 4, n] = (factorial(n) // factorial(n - k)) * tf ** (n - k)
    ```

    We fill row $k + 4$ (so rows 4 to 7) with the coefficients $\frac{n!}{(n-k)!}\, t_f^{n-k}$ for $n = k, k+1, \dots, 7$. This row represents the equation $p^{(k)}(t_f) = h^{(k)}(t_f)$.

    For example, for $k = 0$ (row 4):
    $$V[4, n] = t_f^n \text{ for } n = 0, \dots, 7,$$
    which encodes the equation $a_0 + a_1 t_f + a_2 t_f^2 + \dots + a_7 t_f^7 = h(t_f)$.

    The matrix $V$ is now complete. It's a variant of the Vandermonde matrix, adapted for derivative conditions rather than value-at-multiple-points conditions.

    ---

    ## Step 5 — solving the system

    ```python
    ax = np.linalg.solve(V, cx)
    ay = np.linalg.solve(V, cy)
    ```

    Two calls to `numpy.linalg.solve`: one per component. We get `ax` = the 8-vector of coefficients of $h_x(t)$, and `ay` = same for $h_y(t)$.

    Mathematically we have solved $V a_x = c_x$ and $V a_y = c_y$. Since $V$ is invertible (nonzero determinant whenever $t_f > 0$), the solution is unique.

    ---

    ## Step 6 — a polynomial-derivative evaluator

    ```python
    def p(a, k, t):
        return sum(factorial(n) // factorial(n - k) * a[n] * t ** (n - k) for n in range(k, 8))
    ```

    This inner function computes $p^{(k)}(t)$ for a polynomial whose coefficients are `a`. It is the Taylor-style formula written above, translated into Python. The comprehension `sum(... for n in range(k, 8))` sums the contributions $\frac{n!}{(n-k)!}\, a_n\, t^{n-k}$ for $n$ from $k$ to $7$.

    We will use it just below to evaluate $h, \dot h, \ddot h, h^{(3)}$, and $h^{(4)}$ at any instant.

    ---

    ## Step 7 — the returned function `fun(t)`

    Now we build the function that will be returned to the user. It does all the on-the-fly reconstruction work.

    ```python
    def fun(t):
        hx,  hy  = p(ax, 0, t), p(ay, 0, t)
        dhx, dhy = p(ax, 1, t), p(ay, 1, t)
        d2hx, d2hy = p(ax, 2, t), p(ay, 2, t)
        d3hx, d3hy = p(ax, 3, t), p(ay, 3, t)
        d4hx, d4hy = p(ax, 4, t), p(ay, 4, t)
    ```

    We evaluate $h, \dot h, \ddot h, h^{(3)}, h^{(4)}$ — 10 numbers in total (five (x, y) pairs). The first four pairs are needed for `T_inv` to recover the full state. The fifth pair ($h^{(4)}$) is needed to compute $\ddot\theta$.

    ```python
    x, dx, y, dy, theta, dtheta, z, dz = T_inv(hx, hy, dhx, dhy, d2hx, d2hy, d3hx, d3hy)
    ```

    We use `T_inv` from before. It takes the eight values $h, \dot h, \ddot h, h^{(3)}$ and returns the eight variables of the full state: position, velocity, angle, angular velocity, auxiliary variable, and its derivative. Half the answer is already there.

    What is still missing: the reactor command $(f, \phi)$. For that we need $\ddot x$ and $\ddot y$ (Newton gives $f_x = M \ddot x$ and $f_y = M(\ddot y + g)$), and therefore we need $\ddot\theta$ to relate $\ddot h$ to $\ddot x, \ddot y$.

    ---

    ## Step 8 — recovering $\ddot\theta$

    ```python
    s, c = np.sin(theta), np.cos(theta)
    v2 = M * (c * d4hx + s * d4hy) - 2 * dz * dtheta
    d2theta = v2 / z
    ```

    This is the most subtle step, so let's go slowly. We use the relation established earlier:
    $$h^{(4)} = \frac{1}{M}\, R(\theta - \pi/2) \begin{pmatrix} v_1 - z\dot\theta^2 \\ v_2 + 2\dot z\dot\theta \end{pmatrix}.$$

    We want to isolate $v_2$ (and hence $\ddot\theta = v_2/z$) from $h^{(4)}$. We left-multiply by $M \cdot R(\theta - \pi/2)^{-1}$. The inverse matrix is:
    $$R(\theta - \pi/2)^{-1} = \begin{pmatrix} \sin\theta & -\cos\theta \\ \cos\theta & \sin\theta \end{pmatrix}.$$

    The second row of this matrix, applied to $h^{(4)} = (h^{(4)}_x, h^{(4)}_y)$, gives $\cos\theta \cdot h^{(4)}_x + \sin\theta \cdot h^{(4)}_y$. Multiplying by $M$ and subtracting $2\dot z\dot\theta$ recovers $v_2$:
    $$v_2 = M\big(\cos\theta \cdot h^{(4)}_x + \sin\theta \cdot h^{(4)}_y\big) - 2\dot z\dot\theta.$$

    That is exactly the line `v2 = M * (c * d4hx + s * d4hy) - 2 * dz * dtheta`.

    Then $\ddot\theta = v_2/z$.

    ---

    ## Step 9 — reconstructing $\ddot x$ and $\ddot y$

    ```python
    d2x = d2hx + (l / 6) * (c * d2theta - s * dtheta ** 2)
    d2y = d2hy + (l / 6) * (s * d2theta + c * dtheta ** 2)
    ```

    Recall the calculation of $\ddot h$:
    $$\ddot h_x = \ddot x + (\ell/6) \sin\theta \cdot \dot\theta^2 - (\ell/6) \cos\theta \cdot \ddot\theta,$$
    $$\ddot h_y = \ddot y - (\ell/6) \cos\theta \cdot \dot\theta^2 - (\ell/6) \sin\theta \cdot \ddot\theta.$$

    We invert to get $\ddot x$ and $\ddot y$:
    $$\ddot x = \ddot h_x + (\ell/6)\big(\cos\theta \cdot \ddot\theta - \sin\theta \cdot \dot\theta^2\big),$$
    $$\ddot y = \ddot h_y + (\ell/6)\big(\sin\theta \cdot \ddot\theta + \cos\theta \cdot \dot\theta^2\big).$$

    These are literally the two Python lines.

    ---

    ## Step 10 — Newton for $(f_x, f_y)$

    ```python
    fx, fy = M * d2x, M * (d2y + g)
    ```

    Newton's equations for the center of mass:
    $$M \ddot x = f_x \quad \Rightarrow \quad f_x = M \ddot x,$$
    $$M \ddot y = f_y - Mg \quad \Rightarrow \quad f_y = M(\ddot y + g).$$

    One line, two formulas.

    ---

    ## Step 11 — from $(f_x, f_y)$ to $(f, \phi)$

    ```python
    f = np.sqrt(fx ** 2 + fy ** 2)
    phi = np.arctan2(-fx, fy) - theta
    ```

    We have the reactor force in Cartesian coordinates, but what we ultimately want is its magnitude $f$ and its angle $\phi$ relative to the booster's axis.

    **Magnitude $f$.** Obvious: $f = \sqrt{f_x^2 + f_y^2}$.

    **Angle $\phi$.** Recall from the very beginning of the model:
    $$f_x = -f\sin(\theta + \phi), \qquad f_y = +f\cos(\theta + \phi).$$

    So the angle $\theta + \phi$ satisfies $\sin(\theta + \phi) = -f_x/f$ and $\cos(\theta + \phi) = f_y/f$. The function `np.arctan2(y, x)` computes the angle whose sine is proportional to `y` and cosine to `x`. Thus:
    $$\theta + \phi = \arctan2(-f_x,\, f_y).$$

    And $\phi$ is obtained by subtracting $\theta$:
    $$\phi = \arctan2(-f_x,\, f_y) - \theta.$$

    ---

    ## Step 12 — return everything

    ```python
            return x, dx, y, dy, theta, dtheta, z, dz, f, phi

        return fun
    ```

    The function `fun` returns a 10-tuple: the 8 full-state variables plus the command $(f, \phi)$. And `compute` itself returns this function (without calling it — it is a closure that captures `ax`, `ay`, `tf`, and everything computed beforehand).

    ---

    ## Visual recap

    Here is the pipeline at a glance:

    | Stage | Input | Output | Tool |
    |---|---|---|---|
    | 1 | Initial and final states $(x, \dot x, y, \dot y, \theta, \dot\theta, z, \dot z)$ | Values of $h, \dot h, \ddot h, h^{(3)}$ at both boundaries | `Tr` |
    | 2 | These 16 values | Coefficients $a_0, \dots, a_7$ of two polynomials | `np.linalg.solve(V, c)` |
    | 3 (per $t$) | $t$ | $h(t), \dot h(t), \ddot h(t), h^{(3)}(t), h^{(4)}(t)$ | polynomial evaluation |
    | 4 | $h, \dot h, \ddot h, h^{(3)}$ | $x, \dot x, y, \dot y, \theta, \dot\theta, z, \dot z$ | `T_inv` |
    | 5 | $h^{(4)}, \theta, \dot\theta, z, \dot z$ | $\ddot\theta$ | inverting the $h^{(4)} = \ldots$ relation |
    | 6 | $\ddot h, \theta, \dot\theta, \ddot\theta$ | $\ddot x, \ddot y$ | inverting the $\ddot h$ formula |
    | 7 | $\ddot x, \ddot y$ | $f_x, f_y$ | Newton |
    | 8 | $f_x, f_y, \theta$ | $f, \phi$ | Cartesian-to-polar conversion |

    Stages 1 and 2 are done **once** when `compute` is called. Stages 3 to 8 are done **every time** `fun(t)` is called.

    That is all. There is no magic: every line translates an equation we have already established in previous chapters. The function `compute` is just the assembly of `Tr`, `T_inv`, polynomial interpolation, and Newton's laws.
    """)
    return


@app.cell
def _(M, Tr, Tr_inv, g, l, np):
    def compute(
        x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0,
        x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf,
        tf,
    ):
        H0  = Tr(x_0,  dx_0,  y_0,  dy_0,  theta_0,  dtheta_0,  z_0,  dz_0)
        Htf = Tr(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf)

        cx = np.array([H0[0], H0[2], H0[4], H0[6], Htf[0], Htf[2], Htf[4], Htf[6]])
        cy = np.array([H0[1], H0[3], H0[5], H0[7], Htf[1], Htf[3], Htf[5], Htf[7]])

        def factorial(k):
            if k == 0 :
                return 1
            return k * factorial(k-1)
        V = np.zeros((8, 8))
        for k in range(4):
            V[k, k] = factorial(k)
            for n in range(k, 8):
                V[k + 4, n] = (factorial(n) // factorial(n - k)) * tf ** (n - k)

        ax = np.linalg.solve(V, cx)
        ay = np.linalg.solve(V, cy)

        def p(a, k, t):
            return sum(factorial(n) // factorial(n - k) * a[n] * t ** (n - k) for n in range(k, 8))

        def fun(t):
            hx,  hy  = p(ax, 0, t), p(ay, 0, t)
            dhx, dhy = p(ax, 1, t), p(ay, 1, t)
            d2hx, d2hy = p(ax, 2, t), p(ay, 2, t)
            d3hx, d3hy = p(ax, 3, t), p(ay, 3, t)
            d4hx, d4hy = p(ax, 4, t), p(ay, 4, t)

            x, dx, y, dy, theta, dtheta, z, dz = Tr_inv(hx, hy, dhx, dhy, d2hx, d2hy, d3hx, d3hy)

            s, c = np.sin(theta), np.cos(theta)
            v2 = M * (c * d4hx + s * d4hy) - 2 * dz * dtheta
            d2theta = v2 / z

            d2x = d2hx + (l / 6) * (c * d2theta - s * dtheta ** 2)
            d2y = d2hy + (l / 6) * (s * d2theta + c * dtheta ** 2)

            fx, fy = M * d2x, M * (d2y + g)
            f = np.sqrt(fx ** 2 + fy ** 2)
            phi = np.arctan2(-fx, fy) - theta

            return x, dx, y, dy, theta, dtheta, z, dz, f, phi

        return fun

    return (compute,)


@app.cell
def _(Tr):
    Tr(1.0, 2.0, 3.0, 4.0, 0.1, 0.2, -0.3, -0.4)
    return


@app.cell
def _(Tr, Tr_inv):
    Tr_inv(*Tr(1.0, 2.0, 3.0, 4.0, 0.1, 0.2, -0.3, -0.4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pour bien visualiser le calcul
    \[
    V a = c
    \]

    avec

    \[
    a=
    \begin{bmatrix}
    a_0\\
    a_1\\
    a_2\\
    a_3\\
    a_4\\
    a_5\\
    a_6\\
    a_7
    \end{bmatrix}
    \]

    et

    \[
    c=
    \begin{bmatrix}
    h(0)\\
    \dot h(0)\\
    \ddot h(0)\\
    h^{(3)}(0)\\
    h(t_f)\\
    \dot h(t_f)\\
    \ddot h(t_f)\\
    h^{(3)}(t_f)
    \end{bmatrix}
    \]

    La matrice \(V\) est :

    \[
    V=
    \begin{bmatrix}
    1&0&0&0&0&0&0&0\\
    0&1&0&0&0&0&0&0\\
    0&0&2&0&0&0&0&0\\
    0&0&0&6&0&0&0&0\\
    1&t_f&t_f^2&t_f^3&t_f^4&t_f^5&t_f^6&t_f^7\\
    0&1&2t_f&3t_f^2&4t_f^3&5t_f^4&6t_f^5&7t_f^6\\
    0&0&2&6t_f&12t_f^2&20t_f^3&30t_f^4&42t_f^5\\
    0&0&0&6&24t_f&60t_f^2&120t_f^3&210t_f^4
    \end{bmatrix}
    \]

    \[
    \begin{bmatrix}
    1&0&0&0&0&0&0&0\\
    0&1&0&0&0&0&0&0\\
    0&0&2&0&0&0&0&0\\
    0&0&0&6&0&0&0&0\\
    1&t_f&t_f^2&t_f^3&t_f^4&t_f^5&t_f^6&t_f^7\\
    0&1&2t_f&3t_f^2&4t_f^3&5t_f^4&6t_f^5&7t_f^6\\
    0&0&2&6t_f&12t_f^2&20t_f^3&30t_f^4&42t_f^5\\
    0&0&0&6&24t_f&60t_f^2&120t_f^3&210t_f^4
    \end{bmatrix}
    \begin{bmatrix}
    a_0\\
    a_1\\
    a_2\\
    a_3\\
    a_4\\
    a_5\\
    a_6\\
    a_7
    \end{bmatrix}
    =\begin{bmatrix}
    h(0)\\
    \dot h(0)\\
    \ddot h(0)\\
    h^{(3)}(0)\\
    h(t_f)\\
    \dot h(t_f)\\
    \ddot h(t_f)\\
    h^{(3)}(t_f)
    \end{bmatrix}
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Graphical Validation

    Test your `compute` function with

    - `(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0) = (5.0, 0.0, 20.0, -1.0, -np.pi/8, 0.0, -M*g, 0.0`),
    - `(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf) = (0.0, 0.0, 2/3*l, 0.0,     0.0, 0.0, -M*g, 0.0`),
    - `tf = 10.0`.

    Make the graph of the relevant variables as a function of time, then make an animation out of the same result. Comment and iterate if necessary!
    """)
    return


@app.cell
def _(M, compute, g, l, np, plt):
    tf = 10.0
    fun = compute(
        5.0, 0.0, 20.0, -1.0, -np.pi/8, 0.0, -M*g, 0.0,
        0.0, 0.0, (2/3)*l, 0.0,  0.0, 0.0, -M*g, 0.0,
        tf,
    )

    t_arr = np.linspace(0, tf, 500)
    X = np.array([fun(t) for t in t_arr])
    # Columns of X : x, dx, y, dy, theta, dtheta, z, dz, f, phi

    fig, axes = plt.subplots(3, 2, figsize=(12, 9), sharex=True)

    axes[0, 0].plot(t_arr, X[:, 0], color='steelblue')
    axes[0, 0].axhline(0.0, color='gray', linestyle='--', alpha=0.5, label='cible')
    axes[0, 0].set_ylabel('$x(t)$')
    axes[0, 0].legend(); axes[0, 0].grid(alpha=0.3)

    axes[0, 1].plot(t_arr, X[:, 2], color='steelblue')
    axes[0, 1].axhline(l/2, color='gray', linestyle='--', alpha=0.5, label='$y = \\ell/2$')
    axes[0, 1].set_ylabel('$y(t)$')
    axes[0, 1].legend(); axes[0, 1].grid(alpha=0.3)

    axes[1, 0].plot(t_arr, X[:, 4], color='darkorange')
    axes[1, 0].axhline( np.pi/2, color='red', linestyle='--', alpha=0.5)
    axes[1, 0].axhline(-np.pi/2, color='red', linestyle='--', alpha=0.5)
    axes[1, 0].set_ylabel(r'$\theta(t)$')
    axes[1, 0].grid(alpha=0.3)

    axes[1, 1].plot(t_arr, X[:, 6], color='purple')
    axes[1, 1].axhline(0.0, color='red', linestyle='--', alpha=0.5, label='$z = 0$ (singularité)')
    axes[1, 1].set_ylabel('$z(t)$')
    axes[1, 1].legend(); axes[1, 1].grid(alpha=0.3)

    axes[2, 0].plot(t_arr, X[:, 8], color='seagreen')
    axes[2, 0].axhline(0.0, color='red', linestyle='--', alpha=0.5, label='$f = 0$')
    axes[2, 0].set_ylabel('$f(t)$')
    axes[2, 0].set_xlabel('$t$')
    axes[2, 0].legend(); axes[2, 0].grid(alpha=0.3)

    axes[2, 1].plot(t_arr, X[:, 9], color='seagreen')
    axes[2, 1].axhline( np.pi/2, color='red', linestyle='--', alpha=0.5)
    axes[2, 1].axhline(-np.pi/2, color='red', linestyle='--', alpha=0.5)
    axes[2, 1].set_ylabel(r'$\phi(t)$')
    axes[2, 1].set_xlabel('$t$')
    axes[2, 1].grid(alpha=0.3)

    plt.tight_layout()
    plt.show()
    return fun, tf


@app.cell
def _(booster_anim, fun, mo, tf, world):
    x_t     = lambda t: fun(t)[0]
    y_t     = lambda t: fun(t)[2]
    theta_t = lambda t: fun(t)[4]
    f_t     = lambda t: fun(t)[8]
    phi_t   = lambda t: fun(t)[9]

    mo.Html(
        world(
            [-3, 8, -2, 22],
            booster_anim(x_t, y_t, theta_t, f_t, phi_t, T=tf),
        )
    ).center()
    return


if __name__ == "__main__":
    app.run()
