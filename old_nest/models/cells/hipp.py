import nest

#  Params taken from doi.org/10.1007/s11571-024-10110-3

hipp_params = {
    "E_L": -59.0,
    "g_L": 1.930,
    "C_m": 58.4,
    "V_reset": -56.0,
    "V_th": -50.0,
    "Delta_T": 2.0,
    "a": 0.82,
    "tau_w": 93.0,
    "b": 15.0,
    "E_rev": [],
    "tau_syn": [],
}

nest.CopyModel("aeif_cond_alpha_multisynapse", "hipp", params=hipp_params)
