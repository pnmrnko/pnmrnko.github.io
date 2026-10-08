---
title: "Космос у формулах"
slug: kosmos-u-formulakh
date: 2026-10-08T15:00:00+03:00
toc: true
---

Блог навчився показувати формули. Їх пишуть у LaTeX просто в тексті допису: у рядку між доларами, як $E = mc^2$, або окремим блоком між подвійними. Під час збірки сайту вони перетворюються на MathML, тож браузер малює їх сам, тим самим шрифтом New Computer Modern, що й текст. Жодного JavaScript.

Щоб перевірити все це в ділі, візьму кілька улюблених космічних формул: від ракети на старті до календаря.

## Ракетне рівняння

Ракета летить, бо викидає назад масу. Нехай за мить $\mathrm{d}t$ вона позбувається маси $\mathrm{d}m$ зі швидкістю $v_e$ відносно себе. Імпульс зберігається, тож

$$
\begin{aligned}
m\,\mathrm{d}v &= -v_e\,\mathrm{d}m \\
\int_{v_0}^{v_0 + \Delta v} \mathrm{d}v &= -v_e \int_{m_0}^{m_f} \frac{\mathrm{d}m}{m} \\
\Delta v &= v_e \ln\frac{m_0}{m_f}.
\end{aligned}
$$

Це рівняння Ціолковського. Початкова маса складається з двох частин:

$$
m_0 = \underbrace{m_f}_{\text{суха маса}} + \overbrace{m_p}^{\text{пальне}}
\quad\Longrightarrow\quad
\boxed{\frac{m_p}{m_0} = 1 - e^{-\Delta v / v_e}}
\tag{1}
$$

Швидкість витікання зручно рахувати з питомого імпульсу двигуна: у вакуумному Raptor $I_{sp} \approx 380$ с, і секунди при множенні скорочуються:

$$
v_e = I_{sp}\,g_0 = 380\,\cancel{\text{с}} \cdot 9{,}81\,\frac{\text{м}}{\text{с}^{\cancel{2}}} \approx 3{,}73\ \frac{\text{км}}{\text{с}}.
$$

Щоб вийти на низьку орбіту, з урахуванням втрат на гравітацію й опір повітря, треба $\Delta v \approx 9{,}4$ км/с. За рівнянням (1) пальне має становити $1 - e^{-9{,}4/3{,}73} \approx 92\,\%$ маси ракети. Через це ракети й роблять ступінчастими.

## Закони Кеплера

Під дією самого лише тяжіння тіло рухається так:

$$
\ddot{\mathbf r} = -\frac{\mu}{r^2}\,\hat{\mathbf r},
\qquad
\mu \overset{\text{def}}{=} GM,
\qquad
\mathbf h = \mathbf r \times \dot{\mathbf r} = \text{const}.
$$

Розв’язок цього рівняння — конічний переріз, і його форму задає ексцентриситет $e$:

$$
r(\theta) = \frac{h^2/\mu}{1 + e\cos\theta},
\qquad
\text{орбіта} =
\begin{cases}
\text{коло}, & e = 0, \\
\text{еліпс}, & 0 < e < 1, \\
\text{парабола}, & e = 1, \\
\text{гіпербола}, & e > 1.
\end{cases}
$$

Третій закон каже, що $T^2 \propto a^3$, а точніше

$$
T^2 = \frac{4\pi^2}{\mu}\,a^3
\qquad\Longleftrightarrow\qquad
a = \sqrt[3]{\frac{\mu T^2}{4\pi^2}}.
\tag{2}
$$

Перевіримо на планетах. Якщо міряти $a$ в астрономічних одиницях, а $T$ у роках, для Сонця $4\pi^2/\mu = 1$, і відношення $T^2/a^3$ має бути одиницею:

| Планета  | $a$, а. о. | $T$, роки | $T^2/a^3$ |
|----------|-----------:|----------:|----------:|
| Меркурій |      0,387 |     0,241 |     1,000 |
| Венера   |      0,723 |     0,615 |     1,000 |
| Земля    |      1,000 |     1,000 |     1,000 |
| Марс     |      1,524 |     1,881 |     1,000 |
| Юпітер   |      5,203 |    11,862 |     0,999 |
| Сатурн   |      9,555 |    29,457 |     0,995 |

Юпітер і Сатурн трохи відхиляються, бо вони важкі: у $\mu$ насправді входить маса Сонця разом із планетою, а ще планети тягнуть одна одну.

А тепер навпаки: яка орбіта має період у зоряну добу, $T = 86\,164$ с? З (2) для Землі ($\mu = 398\,600\ \text{км}^3/\text{с}^2$) виходить $a \approx 42\,164$ км, тобто 35 786 км над екватором. Це геостаціонарна орбіта.

## Енергія і швидкість

На орбіті повна енергія на одиницю маси стала: $\textcolor{#228be6}{\text{кінетична}}$ плюс $\textcolor{#e8590c}{\text{потенціальна}}$.

$$
\textcolor{#228be6}{\frac{v^2}{2}} \textcolor{#e8590c}{{}- \frac{\mu}{r}} = -\frac{\mu}{2a}
\quad\Longrightarrow\quad
v = \sqrt{\mu\left(\frac{2}{r} - \frac{1}{a}\right)}.
$$

Для колової орбіти $a = r$ і $v = \sqrt{\mu/r}$. Для МКС на висоті 420 км це близько 7,66 км/с, оберт за 93 хвилини. Якщо ж розтягувати орбіту до нескінченності, вийде друга космічна швидкість:

$$
\lim_{a \to \infty} \sqrt{\mu\left(\frac{2}{r} - \frac{1}{a}\right)} = \sqrt{\frac{2\mu}{r}} \approx 11{,}19\ \frac{\text{км}}{\text{с}} \quad \text{біля поверхні Землі.}
$$

Найдешевше перейти з однієї колової орбіти на іншу двома імпульсами по еліпсу Гомана:

$$
\text{НОО}
\xrightarrow[\;\Delta v_1\;]{\text{розгін}}
\text{перехідний еліпс}
\xrightarrow[\;\Delta v_2\;]{\text{через 5,3 год}}
\text{ГСО}
$$

$$
\Delta v_1 = \sqrt{\frac{\mu}{r_1}}\left(\sqrt{\frac{2r_2}{r_1 + r_2}} - 1\right),
\qquad
\Delta v_2 = \sqrt{\frac{\mu}{r_2}}\left(1 - \sqrt{\frac{2r_1}{r_1 + r_2}}\right).
$$

З висоти 300 км на геостаціонарну це $2{,}43 + 1{,}47 \approx 3{,}89$ км/с, без зміни нахилу орбіти.

## Поле тяжіння

Те саме тяжіння можна описати полем $\mathbf g = -\nabla\Phi$. Його потік крізь будь-яку замкнену поверхню залежить лише від маси всередині (теорема Гаусса), а потенціал задовольняє рівняння Пуассона:

$$
\oiint_{\partial V} \mathbf g \cdot \mathrm{d}\mathbf A = -4\pi G \iiint_V \rho\,\mathrm{d}V,
\qquad
\nabla^2 \Phi = \frac{\partial^2 \Phi}{\partial x^2} + \frac{\partial^2 \Phi}{\partial y^2} + \frac{\partial^2 \Phi}{\partial z^2} = 4\pi G\rho.
$$

## Повороти

Орбіту в просторі задають три кути: довгота висхідного вузла $\Omega$, нахил $i$ і аргумент перицентру $\omega$. Перехід від площини орбіти до екваторіальних координат — це три повороти, кожен такого вигляду:

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
\begin{bmatrix} x \\ y \\ z \end{bmatrix}_{\text{екв}}
= R_z(\Omega)\,R_x(i)\,R_z(\omega)
\begin{bmatrix} x \\ y \\ z \end{bmatrix}_{\text{орб}}.
$$

Такі матриці утворюють групу обертань, а кососиметричні матриці — її алгебру Лі:

$$
\begin{gathered}
\mathrm{SO}(3) = \left\{ R \in \mathbb R^{3 \times 3} \;\middle|\; R^{\top} R = I,\ \det R = 1 \right\}, \\
\mathfrak{so}(3) = \left\{ A \in \mathbb R^{3 \times 3} \;\middle|\; A^{\top} = -A \right\}.
\end{gathered}
$$

Поворот не залежить від часу, тому байдуже, чи спершу повернути координати, а потім узяти похідну, чи навпаки. Діаграма комутує:

$$
\begin{CD}
\mathbf r_{\text{орб}} @>{R}>> \mathbf r_{\text{екв}} \\
@V{\mathrm{d}/\mathrm{d}t}VV @VV{\mathrm{d}/\mathrm{d}t}V \\
\mathbf v_{\text{орб}} @>>{R}> \mathbf v_{\text{екв}}
\end{CD}
$$

## Час на орбіті

Годинник, що рухається, відстає в $\gamma$ разів. Для малих швидкостей корінь зручно розкласти в ряд:

$$
\gamma = \frac{1}{\sqrt{1 - \beta^2}}
= \sum_{k=0}^{\infty} \binom{2k}{k} \frac{\beta^{2k}}{4^k}
= 1 + \frac{\beta^2}{2} + \frac{3\beta^4}{8} + \cdots,
\qquad
\beta = \frac{v}{c} \ll 1.
$$

Для МКС $\beta \approx 2{,}56 \cdot 10^{-5}$, тож $\gamma - 1 \approx 3{,}3 \cdot 10^{-10}$. За пів року на станції астронавт «молодшає» лише на 5 мс, а слабше тяжіння на висоті ще й частково це компенсує.

## Хімія і зорі

Пальне горить у кисні:

$$
\ce{2H2 + O2 -> 2H2O}
\qquad
\ce{CH4 + 2O2 -> CO2 + 2H2O}
$$

Перша реакція — це водневі двигуни, як RS-25 у шатлів, друга — метанові, як Raptor. А Сонце світить завдяки протон-протонному циклу, який зрештою перетворює чотири протони на ядро гелію:

$$
4\,{}^{1}_{1}\mathrm{H} \longrightarrow {}^{4}_{2}\mathrm{He} + 2\,\mathrm{e}^{+} + 2\,\nu_e,
\qquad
\Delta E \approx 26{,}7\ \text{МеВ}.
$$

## Календар

Тропічний рік триває приблизно $365{,}24219$ доби. Дробову частину зручно розкласти в ланцюговий дріб:

$$
0{,}24219 = \cfrac{1}{4 + \cfrac{1}{7 + \cfrac{1}{1 + \cfrac{1}{3 + \cfrac{1}{24 + \dotsb}}}}}
$$

Кожен обрізаний дріб дає правило високосних років:

$$
\begin{array}{c|c|c|l}
\text{дріб} & \text{значення} & \text{похибка на рік} & \text{календар} \\
\hline
1/4 & 0{,}25 & +11\ \text{хв} & \text{юліанський} \\
7/29 & 0{,}24138 & -1{,}2\ \text{хв} & \\
8/33 & 0{,}24242 & +20\ \text{с} & \text{перський цикл} \\
\hline
97/400 & 0{,}2425 & +27\ \text{с} & \text{григоріанський}
\end{array}
$$

Григоріанський календар узяв не найточніший дріб, а зручний: його правило легко перевірити в голові. Рік високосний, якщо $y \equiv 0 \pmod{4}$, але не кожне століття:

$$
\text{днів у році } y =
\begin{cases}
366, & 4 \mid y \ \land\ \bigl(100 \nmid y \ \lor\ 400 \mid y\bigr), \\
365 & \text{інакше}.
\end{cases}
$$

Він помиляється на добу десь за 3200 років, юліанський — за 128.

## Що ще вміють формули

Наостанок кунсткамера, щоб було видно, що ще можна писати.

- Числові множини та шрифти: $\mathbb N \subset \mathbb Z \subset \mathbb Q \subset \mathbb R \subset \mathbb C$, лагранжіан $\mathcal L = T - V$, алгебра $\mathfrak g$, вектор кутової швидкості $\boldsymbol\omega$, диференціал $\mathrm{d}x$ прямим шрифтом.
- Акценти: $\vec v$, $\hat n$, $\bar x$, $\tilde a$, $\dot x$, $\ddot x$, $\widehat{ABC}$, $\overline{z}$, $\overrightarrow{AB}$.
- Стрілки, що підлаштовуються під підпис: $A \xrightarrow{\text{довгий підпис}} B$, $X \xleftrightarrow[\text{знизу}]{} Y$.
- Логіка: $\forall\, \varepsilon > 0\ \exists\, \delta > 0 \colon$ $|x - a| < \delta \implies |f(x) - f(a)| < \varepsilon$.
- Дужки, що підлаштовуються: $\left\lfloor \frac{n}{2} \right\rfloor$, $\left\lVert \mathbf v \right\rVert$, $\langle \psi \mid \phi \rangle$, $\bigl( \Bigl( \biggl( \Biggl($.
- Дроби в рядку: $\frac12$ і більший $\dfrac12$, біноми $\binom{n}{k}$, ланцюгові $\cfrac{1}{1 + \cfrac{1}{x}}$.
- Матриця в рядку: $\left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$, а поруч $e^{i\pi} + 1 = 0$.
- Кольори: $\color{#228be6} x$, $\textcolor{#e8590c}{y}$, $\colorbox{#ffec99}{\textcolor{#212529}{z}}$, а ще $\xcancel{\text{помилка}}$, $\bcancel{5}$ і $\fbox{рамка}$.
- Великі оператори: $\sum$, $\prod$, $\coprod$, $\bigcup$, $\bigcap$, $\bigoplus$, $\bigotimes$, $\int$, $\iint$, $\oint$.

Формула з помилкою не пройде збірку, тож зламана математика на сайт просто не потрапить.
