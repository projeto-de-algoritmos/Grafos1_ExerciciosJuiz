#include <stdio.h>
#include <stdbool.h>
#define MAXSIZE 500

int par[MAXSIZE];

int parent(int);
int scanff(int *);

int main()
{
    int m, p, n;
    int u, v;

    scanff(&n), scanff(&m), scanff(&p);

    for (int i = 0; i <= n; ++i)
        par[i] = i;

    for (int i = 0; i < m; ++i)
    {
        scanff(&u), scanff(&v);

        while (par[u] != u)
            u = par[u];
        while (par[v] != v)
            v = par[v];

        if (u == v)
            continue;

        par[u] = v;
    }

    while (p--)
    {
        scanff(&u), scanff(&v);

        u = parent(u);
        v = parent(v);

        if (u == v)
            puts("Lets que lets");
        else
            puts("Deu ruim");
    }

    return 0;
}

int parent(int u)
{
    if (par[u] == u)
        return u;
    return par[u] = parent(par[u]);
}

int scanff(int *a)
{
    register int c = getchar_unlocked();
    *a = 0;

    while (c >= '0')
    {
        *a = *a * 10 + (c - '0');
        c = getchar_unlocked();
    }

    return c;
}
