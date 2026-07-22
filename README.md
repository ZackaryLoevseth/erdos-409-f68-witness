# An F = 68 witness for Erdős Problem #409

Certificates and code verifying

\[
F(6{,}148{,}888{,}817)=68
\]

for the iteration

\[
T(n)=\varphi(n)+1.
\]

Here \(F(p)=0\) when \(p\) is prime, and for composite \(n\),

\[
F(n)=1+F(T(n)).
\]

Starting from

\[
6{,}148{,}888{,}817
=
75{,}503 \times 81{,}439,
\]

the trajectory first reaches a prime after exactly 68 applications of \(T\). The terminal prime is

\[
9{,}500{,}401.
\]

## Minimal verification

Install the only dependency:

```bash
python -m pip install -r requirements.txt
```

Then run:

```bash
python verify.py
```

Expected output:

```text
68 9500401
```

The same check can also be run directly:

```python
from sympy import isprime, totient

n = 6_148_888_817
steps = 0

while not isprime(n):
    n = int(totient(n)) + 1
    steps += 1

print(steps, n)
```

## Scope of the result

This establishes the explicit computational lower bound

\[
\sup_{n\ge1}F(n)\ge68.
\]

It is a computational partial result related to [Erdős Problem #409](https://www.erdosproblems.com/409).

It does **not** resolve the broader questions concerning:

- upper bounds for \(F(n)\);
- whether infinitely many integers reach the same terminal prime;
- the density of integers reaching a fixed prime.

I am not currently aware of a previously published \(F\ge68\) example. Novelty remains subject to literature search and community review.

## Verification packet

The complete certificate packet contains:

- the full 69-node trajectory;
- exact factorizations of every composite node;
- exact recomputation of every totient;
- verification of every transition;
- independent implementations;
- a standalone certificate checker;
- a terminal-primality certificate;
- a 118-entry SHA-256 manifest.

Archive SHA-256:

```text
ca5b9a9e69f9a91e3de2642452259c307a416f659349c5067cb20c692f42d026
```

Canonical trajectory SHA-256:

```text
6a6758b8bb6e2d2cd812301b04eabc9d14699d18908a1cdf7066454934802ad7
```

The complete archive should be attached to the repository's first GitHub release.

## AI assistance and authorship

This result was produced through a substantially AI-assisted research workflow using OpenAI and Anthropic systems.

The research target, governing protocol, iterative prompt design, verification requirements, cross-model review, and final publication decisions were directed by **Zackary Loevseth**.

AI systems performed substantial parts of the search, code generation, computation, certificate production, and drafting.

See [AI_USAGE.md](AI_USAGE.md) for the full disclosure.

## Citation

T. F. Bloom, “Erdős Problem #409,”  
https://www.erdosproblems.com/409, accessed July 22, 2026.
