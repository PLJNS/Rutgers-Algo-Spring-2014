
import random
import fractions

def Number_Theoretic_Algorithm(n)
    N = random.randint(0, (2 ** n) - 1);
    if (N % 2 == 0)
        N = N - 1;

    m = N % n;

    for (j = 0; j < N; j++)
        if (fractions.gcd(j, N) != 1)
            return false;


