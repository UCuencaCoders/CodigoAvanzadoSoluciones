// https://csacademy.com/ieeextreme-practice/task/summation/
// 100% score

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct pair_hash {
    template <class T1, class T2>
    std::size_t operator() (const std::pair<T1, T2>& pair) const {
        return std::hash<T1>()(pair.first) ^ std::hash<T2>()(pair.second);
    }
};

vector<vector<ll>> B;
unordered_map<pair<ll, ll>, ll, pair_hash> S;

ll binomial(ll n, ll k, ll mod) {
    if (k > n) return 0;
    if (k == 0 || k == n) return 1;

    if (B.size() <= n){
        B.resize(n+1, vector<ll>(n+1, -1));
    }

    if (B[n][k] != -1) {
        return B[n][k];
    }

    return B[n][k] = (binomial(n-1, k, mod) + binomial(n-1, k-1, mod)) % mod;
}

long long power(ll base, ll exponent, ll mod){
    if (exponent == 0) return 1;
    if (exponent == 1) return base % mod;

    long long half = power(base, exponent / 2, mod);
    half = (half * half) % mod;

    if (exponent % 2 != 0) {
        half = (half * base) % mod;
    }

    return half;
}

ll summation(ll p, ll q, ll n, ll m) {
    if (n == 1) return p % m;
    
    ll term = 0;
    ll half = n / 2;

    for (ll i = 0; i <= q; i++) {
        pair<ll, ll> pair = {i, half};
        ll s;

        if (S.find(pair) != S.end()) {
            s = S[pair];
        } else {
            s = summation(p, i, half, m);
            S[pair] = s;
        }

        term = (term + binomial(q, i, m) * power(half, q - i, m) % m * s % m) % m;
    }

    pair<ll, ll> pair = {q, half};

    term = (S[pair] + power(p, half, m) * term % m) % m;

    if (n % 2 != 0) {
        term = (term + power(p, n, m) * power(n, q, m) % m) % m;
    }
    return term;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); 
    
    ll p, q, n, m;
    cin >> p >> q >> n >> m;
    
    cout << summation(p, q, n, m) << "\n";
}