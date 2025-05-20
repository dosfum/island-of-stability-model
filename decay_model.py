import numpy as np

def semf_binding_energy(Z, A):
    a_v, a_s, a_c, a_sym = 15.8, 18.3, 0.714, 23.2
    delta = pairing_term(Z, A)
    return (a_v*A - a_s*A**(2/3) - a_c*(Z**2)/A**(1/3) - a_sym*((A - 2*Z)**2)/A + delta)

def pairing_term(Z, A):
    if A % 2 != 0:
        return 0
    elif Z % 2 == 0 and (A - Z) % 2 == 0:
        return 12 / A**0.5  # even-even
    else:
        return -12 / A**0.5  # odd-odd

def q_alpha(Z, A):
    be_parent = semf_binding_energy(Z, A)
    be_daughter = semf_binding_energy(Z-2, A-4)
    be_alpha = semf_binding_energy(2, 4)
    return be_daughter + be_alpha - be_parent

def alpha_half_life(Q_alpha, Z, a=1.66175, b=8.5166):
    return 10**(a*Z/np.sqrt(Q_alpha) - b)

def sf_half_life(Z, A, binding_per_nucleon):
    instability = Z**2 / binding_per_nucleon
    return 1 / instability

def stability_score(sf_hl, alpha_hl):
    return np.log10(sf_hl / alpha_hl)