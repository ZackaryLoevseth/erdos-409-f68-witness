# erdos-409-f68-witness
Certificates and code verifying F(6,148,888,817) = 68 for Erdős Problem #409.
## Result

Define

\[
T(n)=\varphi(n)+1
\]

and let \(F(n)\) be the number of applications of \(T\) needed to reach a prime, with \(F(p)=0\) when \(p\) is already prime.

This repository verifies that

\[
\boxed{F(6{,}148{,}888{,}817)=68}.
\]

The trajectory reaches the prime

\[
9{,}500{,}401
\]

after exactly 68 applications of \(T\).

The starting value factors as

\[
6{,}148{,}888{,}817
=
75{,}503 \times 81{,}439.
\]

## Minimal verification

Install SymPy:

```bash
pip install sympy
