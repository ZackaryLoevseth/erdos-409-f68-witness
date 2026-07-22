# An F = 68 witness for Erdős Problem #409

Certificates and code verifying

$$
F(6{,}148{,}888{,}817)=68
$$

for the iteration

$$
T(n)=\varphi(n)+1.
$$

Here $F(p)=0$ when $p$ is prime, and for composite $n$,

$$
F(n)=1+F(T(n)).
$$

Starting from

$$
6{,}148{,}888{,}817
=
75{,}503 \times 81{,}439,
$$

the trajectory first reaches a prime after exactly 68 applications of $T$. The terminal prime is

$$
9{,}500{,}401.
$$

## Minimal verification

Install the only dependency:

```bash
python -m pip install -r requirements.txt
