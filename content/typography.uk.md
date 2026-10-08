---
title: Типографіка
url: /typography/
draft: true
---

Сторінка для перевірки шрифтів і формул. Вона чернетка, тож на сайт не потрапляє: `hugo server -D`.

## Текст

Звичайний абзац New CM Sans Book: «лапки», тире — і апостроф у слові пʼять. *Курсив (Oblique)*, **жирний**, ***жирний курсив***. Ґанок, їжак, євшан-зілля, ₴ 100. Ligatures: office, file, fluffy. Grecian: αβγ ΔΣΩ.

## Код

Рядок із кодом: `power=minor_line`, `x := 1 << 8`.

```python
def mean(xs: list[float]) -> float:
    """Середнє арифметичне."""
    return sum(xs) / len(xs)  # 0O1lI|
```

## Формули

Рядкові: $E = mc^2$, \(a^2 + b^2 = c^2\), а також $\sqrt{2} \approx 1{,}414$ і $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$.

Виокремлені:

$$
\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}
$$

\[
\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1}
= \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
\]

$$
f(x) = \begin{cases} x^2, & \text{якщо } x \ge 0, \\ -x, & \text{інакше.} \end{cases}
\qquad
\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^{n} = e
$$

$$
\mathbb{R}, \quad \mathcal{L}\{f\}(s) = \int_0^\infty f(t)\,e^{-st}\,dt, \quad \nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}
$$

$$
\begin{aligned}
(a + b)^2 &= a^2 + 2ab + b^2, \\
(a - b)^2 &= a^2 - 2ab + b^2.
\end{aligned}
$$
