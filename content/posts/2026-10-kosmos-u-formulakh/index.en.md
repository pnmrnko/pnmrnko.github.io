---
title: "Space in Formulas"
slug: space-in-formulas
date: 2026-10-08T15:00:00+03:00
toc: true
draft: true
---

The blog can show formulas now. They’re written in LaTeX right in the text of a post: inline between dollar signs, like $E = mc^2$, or as a separate block between double ones. When the site is built they become MathML, so the browser draws them itself, in the same New Computer Modern as the text. No JavaScript at all.

To put it through its paces, here are some space formulas, from a rocket on the pad to the calendar.

## The rocket equation

A rocket flies by throwing mass backwards. Say in an instant $\mathrm{d}t$ it sheds mass $\mathrm{d}m$ at speed $v_e$ relative to itself. Momentum is conserved, so

$$
\begin{aligned}
m\,\mathrm{d}v &= -v_e\,\mathrm{d}m \\
\int_{v_0}^{v_0 + \Delta v} \mathrm{d}v &= -v_e \int_{m_0}^{m_f} \frac{\mathrm{d}m}{m} \\
\Delta v &= v_e \ln\frac{m_0}{m_f}.
\end{aligned}
$$

This is Tsiolkovsky’s equation. The initial mass has two parts:

$$
m_0 = \underbrace{m_f}_{\text{dry mass}} + \overbrace{m_p}^{\text{propellant}}
\quad\Longrightarrow\quad
\boxed{\frac{m_p}{m_0} = 1 - e^{-\Delta v / v_e}}
\tag{1}
$$

The exhaust speed is easiest to get from the engine’s specific impulse: a vacuum Raptor has $I_{sp} \approx 380$ s, and the seconds cancel out:

$$
v_e = I_{sp}\,g_0 = 380\,\cancel{\text{s}} \cdot 9.81\,\frac{\text{m}}{\text{s}^{\cancel{2}}} \approx 3.73\ \frac{\text{km}}{\text{s}}.
$$

Getting to low orbit, counting gravity and drag losses, takes $\Delta v \approx 9.4$ km/s. By equation (1) propellant must then be $1 - e^{-9.4/3.73} \approx 92\,\%$ of the rocket’s mass. That’s why rockets have stages.

## Kepler’s laws

Under gravity alone a body moves like this:

$$
\ddot{\mathbf r} = -\frac{\mu}{r^2}\,\hat{\mathbf r},
\qquad
\mu \overset{\text{def}}{=} GM,
\qquad
\mathbf h = \mathbf r \times \dot{\mathbf r} = \text{const}.
$$

The solution is a conic section, and its shape is set by the eccentricity $e$:

$$
r(\theta) = \frac{h^2/\mu}{1 + e\cos\theta},
\qquad
\text{orbit} =
\begin{cases}
\text{circle}, & e = 0, \\
\text{ellipse}, & 0 < e < 1, \\
\text{parabola}, & e = 1, \\
\text{hyperbola}, & e > 1.
\end{cases}
$$

The third law says $T^2 \propto a^3$, or more precisely

$$
T^2 = \frac{4\pi^2}{\mu}\,a^3
\qquad\Longleftrightarrow\qquad
a = \sqrt[3]{\frac{\mu T^2}{4\pi^2}}.
\tag{2}
$$

Let’s check it on the planets. Measuring $a$ in astronomical units and $T$ in years makes $4\pi^2/\mu = 1$ for the Sun, so $T^2/a^3$ should come out as one:

| Planet  | $a$, AU | $T$, years | $T^2/a^3$ |
|---------|--------:|-----------:|----------:|
| Mercury |   0.387 |      0.241 |     1.000 |
| Venus   |   0.723 |      0.615 |     1.000 |
| Earth   |   1.000 |      1.000 |     1.000 |
| Mars    |   1.524 |      1.881 |     1.000 |
| Jupiter |   5.203 |     11.862 |     0.999 |
| Saturn  |   9.555 |     29.457 |     0.995 |

Jupiter and Saturn are slightly off because they’re heavy: $\mu$ really holds the mass of the Sun plus the planet, and the planets also pull on each other.

Now the other way round: which orbit has a period of one sidereal day, $T = 86\,164$ s? From (2) for Earth ($\mu = 398\,600\ \text{km}^3/\text{s}^2$) we get $a \approx 42\,164$ km, or 35,786 km above the equator. That’s geostationary orbit.

## Energy and speed

In orbit the total energy per unit mass stays constant: $\textcolor{#228be6}{\text{kinetic}}$ plus $\textcolor{#e8590c}{\text{potential}}$.

$$
\textcolor{#228be6}{\frac{v^2}{2}} \textcolor{#e8590c}{{}- \frac{\mu}{r}} = -\frac{\mu}{2a}
\quad\Longrightarrow\quad
v = \sqrt{\mu\left(\frac{2}{r} - \frac{1}{a}\right)}.
$$

For a circular orbit $a = r$ and $v = \sqrt{\mu/r}$. For the ISS at 420 km that’s about 7.66 km/s, one lap in 93 minutes. Stretch the orbit out to infinity and you get escape velocity:

$$
\lim_{a \to \infty} \sqrt{\mu\left(\frac{2}{r} - \frac{1}{a}\right)} = \sqrt{\frac{2\mu}{r}} \approx 11.19\ \frac{\text{km}}{\text{s}} \quad \text{at Earth’s surface.}
$$

The cheapest way from one circular orbit to another is two burns along a Hohmann ellipse:

$$
\text{LEO}
\xrightarrow[\;\Delta v_1\;]{\text{burn}}
\text{transfer ellipse}
\xrightarrow[\;\Delta v_2\;]{\text{5.3 h later}}
\text{GEO}
$$

$$
\Delta v_1 = \sqrt{\frac{\mu}{r_1}}\left(\sqrt{\frac{2r_2}{r_1 + r_2}} - 1\right),
\qquad
\Delta v_2 = \sqrt{\frac{\mu}{r_2}}\left(1 - \sqrt{\frac{2r_1}{r_1 + r_2}}\right).
$$

From 300 km up to geostationary that’s $2.43 + 1.47 \approx 3.89$ km/s, without changing the orbit’s inclination.

## The gravitational field

The same gravity can be described as a field $\mathbf g = -\nabla\Phi$. Its flux through any closed surface depends only on the mass inside (Gauss’s law), and the potential satisfies Poisson’s equation:

$$
\oiint_{\partial V} \mathbf g \cdot \mathrm{d}\mathbf A = -4\pi G \iiint_V \rho\,\mathrm{d}V,
\qquad
\nabla^2 \Phi = \frac{\partial^2 \Phi}{\partial x^2} + \frac{\partial^2 \Phi}{\partial y^2} + \frac{\partial^2 \Phi}{\partial z^2} = 4\pi G\rho.
$$

## Rotations

An orbit’s orientation in space takes three angles: the longitude of the ascending node $\Omega$, the inclination $i$ and the argument of periapsis $\omega$. Going from the orbital plane to equatorial coordinates is three rotations, each like this:

$$
R_z(\theta) =
\begin{pmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{pmatrix},
\qquad
\det R_z(\theta) =
\begin{vmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{vmatrix}
= \cos^2\theta + \sin^2\theta = 1,
$$

$$
\begin{bmatrix} x \\ y \\ z \end{bmatrix}_{\text{eq}}
= R_z(\Omega)\,R_x(i)\,R_z(\omega)
\begin{bmatrix} x \\ y \\ z \end{bmatrix}_{\text{orb}}.
$$

Such matrices form the rotation group, and the skew-symmetric matrices form its Lie algebra:

$$
\begin{gathered}
\mathrm{SO}(3) = \left\{ R \in \mathbb R^{3 \times 3} \;\middle|\; R^{\top} R = I,\ \det R = 1 \right\}, \\
\mathfrak{so}(3) = \left\{ A \in \mathbb R^{3 \times 3} \;\middle|\; A^{\top} = -A \right\}.
\end{gathered}
$$

The rotation doesn’t depend on time, so it makes no difference whether you rotate the coordinates first and then differentiate, or the other way round. The diagram commutes:

$$
\begin{CD}
\mathbf r_{\text{orb}} @>{R}>> \mathbf r_{\text{eq}} \\
@V{\mathrm{d}/\mathrm{d}t}VV @VV{\mathrm{d}/\mathrm{d}t}V \\
\mathbf v_{\text{orb}} @>>{R}> \mathbf v_{\text{eq}}
\end{CD}
$$

## Time in orbit

A moving clock runs slow by a factor of $\gamma$. At low speeds the root is easiest to expand as a series:

$$
\gamma = \frac{1}{\sqrt{1 - \beta^2}}
= \sum_{k=0}^{\infty} \binom{2k}{k} \frac{\beta^{2k}}{4^k}
= 1 + \frac{\beta^2}{2} + \frac{3\beta^4}{8} + \cdots,
\qquad
\beta = \frac{v}{c} \ll 1.
$$

For the ISS $\beta \approx 2.56 \cdot 10^{-5}$, so $\gamma - 1 \approx 3.3 \cdot 10^{-10}$. Half a year on the station leaves an astronaut just 5 ms “younger”, and the weaker gravity up there partly makes up for even that.

## Chemistry and stars

Propellant burns in oxygen:

$$
\ce{2H2 + O2 -> 2H2O}
\qquad
\ce{CH4 + 2O2 -> CO2 + 2H2O}
$$

The first reaction powers hydrogen engines like the Shuttle’s RS-25, the second methane ones like Raptor. And the Sun shines thanks to the proton–proton chain, which in the end turns four protons into a helium nucleus:

$$
4\,{}^{1}_{1}\mathrm{H} \longrightarrow {}^{4}_{2}\mathrm{He} + 2\,\mathrm{e}^{+} + 2\,\nu_e,
\qquad
\Delta E \approx 26.7\ \text{MeV}.
$$

## The calendar

A tropical year lasts about $365.24219$ days. The fractional part is easiest to expand as a continued fraction:

$$
0.24219 = \cfrac{1}{4 + \cfrac{1}{7 + \cfrac{1}{1 + \cfrac{1}{3 + \cfrac{1}{24 + \dotsb}}}}}
$$

Each truncated fraction gives a leap-year rule:

$$
\begin{array}{c|c|c|l}
\text{fraction} & \text{value} & \text{error per year} & \text{calendar} \\
\hline
1/4 & 0.25 & +11\ \text{min} & \text{Julian} \\
7/29 & 0.24138 & -1.2\ \text{min} & \\
8/33 & 0.24242 & +20\ \text{s} & \text{Persian cycle} \\
\hline
97/400 & 0.2425 & +27\ \text{s} & \text{Gregorian}
\end{array}
$$

The Gregorian calendar didn’t take the most accurate fraction but a convenient one, whose rule is easy to check in your head. A year is a leap year if $y \equiv 0 \pmod{4}$, but not every century is:

$$
\text{days in year } y =
\begin{cases}
366, & 4 \mid y \ \land\ \bigl(100 \nmid y \ \lor\ 400 \mid y\bigr), \\
365 & \text{otherwise}.
\end{cases}
$$

It drifts by a day in about 3,200 years; the Julian calendar does in 128.

## What else formulas can do

Finally, a cabinet of curiosities, to show what else can be written.

- Number sets and alphabets: $\mathbb N \subset \mathbb Z \subset \mathbb Q \subset \mathbb R \subset \mathbb C$, a Lagrangian $\mathcal L = T - V$, an algebra $\mathfrak g$, angular velocity $\boldsymbol\omega$, an upright differential $\mathrm{d}x$.
- Accents: $\vec v$, $\hat n$, $\bar x$, $\tilde a$, $\dot x$, $\ddot x$, $\widehat{ABC}$, $\overline{z}$, $\overrightarrow{AB}$.
- Arrows that stretch to fit their label: $A \xrightarrow{\text{a long label}} B$, $X \xleftrightarrow[\text{below}]{} Y$.
- Logic: $\forall\, \varepsilon > 0\ \exists\, \delta > 0 \colon$ $|x - a| < \delta \implies |f(x) - f(a)| < \varepsilon$.
- Brackets that grow: $\left\lfloor \frac{n}{2} \right\rfloor$, $\left\lVert \mathbf v \right\rVert$, $\langle \psi \mid \phi \rangle$, $\bigl( \Bigl( \biggl( \Biggl($.
- Inline fractions: $\frac12$ and a bigger $\dfrac12$, binomials $\binom{n}{k}$, continued ones $\cfrac{1}{1 + \cfrac{1}{x}}$.
- An inline matrix: $\left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$, and next to it $e^{i\pi} + 1 = 0$.
- Colours: $\color{#228be6} x$, $\textcolor{#e8590c}{y}$, $\colorbox{#ffec99}{\textcolor{#212529}{z}}$, plus $\xcancel{\text{a mistake}}$, $\bcancel{5}$ and $\fbox{a box}$.
- Big operators: $\sum$, $\prod$, $\coprod$, $\bigcup$, $\bigcap$, $\bigoplus$, $\bigotimes$, $\int$, $\iint$, $\oint$.

A formula with a mistake in it won’t get through the build, so broken maths simply never reaches the site.
