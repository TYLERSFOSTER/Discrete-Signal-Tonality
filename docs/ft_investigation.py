import numpy as np
import matplotlib.pyplot as plt

# Parameters
ell = 27                            # Modulus
t = 100                                # Time parameter
# s = np.random.rand(ell)             # Example signal s(n) defined over Z/ellZ
discrete_space = np.linspace(0, ell, ell)

for multiplier in range(ell):
    s = np.real(np.exp(complex(0,1)*(2*np.pi/ell)*multiplier*discrete_space))
    print(s)

    # Omega range
    omega_vals = np.linspace(0, 100, 1000)

    # Define f(omega)
    def f(omega):
        exp_term = np.exp(-2j * np.pi * np.arange(ell) * t / ell)
        total = np.sum(s * exp_term)    # Only this part depends on s(n) and t
        return total * np.sinc(omega / ell)

    # Vectorized computation
    f_vals = f(omega_vals)

    # Plot
    plt.figure(figsize=(8, 4))
    plt.plot(omega_vals, np.real(f_vals), label='Re[f(ω)]')
    plt.plot(omega_vals, np.imag(f_vals), label='Im[f(ω)]', linestyle='--')
    plt.axhline(0, color='gray', lw=0.5)
    plt.title(r"$f(\omega) = \sum_n s(n)\,e^{-2\pi i nt/\ell} \cdot \mathrm{sinc}(\omega/\ell)$")
    plt.xlabel(r'$\omega$')
    plt.ylabel(r'$f(\omega)$')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
