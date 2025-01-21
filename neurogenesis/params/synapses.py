from brian2 import *
from neurogenesis.utils.connections import (lamellar_conn, cross_lamellar_conn)
from neurogenesis.params.cells import (
    N_mgc_l,
    N_igc_l,
    N_bc_l,
    N_mc_l,
    N_hipp_l
) 

# Syntax: source_receptor_target
syn_params = {
    "ec_ampa_mgc": {
        "receptor" : "ampa",
        "K"        : 0.89 * pF,
        "tau_r"    : 0.1 * ms,
        "tau_d"    : 2.5 * ms,
        "delay"    : 3.0 * ms,
        "E"        : 0 * mV,
    },
    "ec_nmda_mgc": {
        "receptor" : "nmda",
        "K"        : 0.15 * pF,
        "tau_r"    : 0.33 * ms,
        "tau_d"    : 50.0 * ms,
        "delay"    : 3.0 * ms,
        "E"        : 0 * mV,
    },
    "ec_ampa_bc": {
        "receptor" : "ampa",
        "K"        : 0.75 * pF,
        "tau_r"    : 2.0 * ms,
        "tau_d"    : 6.3 * ms,
        "delay"    : 3.0 * ms,
        "E"        : 0 * mV,
    },
    "ec_nmda_bc": {
        "receptor" : "nmda",
        "K"        : 0.13 * pF,
        "tau_r"    : 6.6 * ms,
        "tau_d"    : 126.0 * ms,
        "delay"    : 3.0 * ms,
        "E"        : 0 * mV,
    },

    "mgc_ampa_bc": {
        "receptor"  : "ampa",
        "condition" : lamellar_conn(N_mgc_l, N_bc_l),
        "K"         : 0.38 * pF,
        "tau_r"     : 2.5 * ms,
        "tau_d"     : 3.5 * ms,
        "delay"     : 0.8 * ms,
        "E"         : 0 * mV,
    },
    "mgc_nmda_bc": {
        "receptor"  : "nmda",
        "condition" : lamellar_conn(N_mgc_l, N_bc_l),
        "K"         : 0.02 * pF,
        "tau_r"     : 10.0 * ms,
        "tau_d"     : 130.0 * ms,
        "delay"     : 0.8 * ms,
        "E"         : 0 * mV,
    },
    "mgc_ampa_mc": {
        "receptor"  : "ampa",
        "condition" : lamellar_conn(N_mgc_l, N_mc_l),
        "K"         : 9.58 * pF,
        "tau_r"     : 0.5 * ms,
        "tau_d"     : 6.2 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },
    "mgc_nmda_mc": {
        "receptor"  : "nmda",
        "condition" : lamellar_conn(N_mgc_l, N_mc_l),
        "K"         : 1.71 * pF,
        "tau_r"     : 4.0 * ms,
        "tau_d"     : 100.0 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },
    "mgc_ampa_hipp": {
        "receptor"  : "ampa",
        "condition" : lamellar_conn(N_mgc_l, N_hipp_l),
        "K"         : 0.08 * pF,
        "tau_r"     : 0.3 * ms,
        "tau_d"     : 0.6 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },
    "mgc_nmda_hipp": {
        "receptor"  : "nmda",
        "condition" : lamellar_conn(N_mgc_l, N_hipp_l),
        "K"         : 0.004 * pF,
        "tau_r"     : 1.2 * ms,
        "tau_d"     : 22.2 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },

    "bc_gaba_mgc": {
        "receptor"  : "gaba",
        "condition" : lamellar_conn(N_bc_l, N_mgc_l),
        "K"         : 15.0 * pF,
        "tau_r"     : 0.9 * ms,
        "tau_d"     : 6.8 * ms,
        "delay"     : 0.85 * ms,
        "E"         : -86.0 * mV,
    },
    "bc_gaba_mc": {
        "receptor"  : "gaba",
        "condition" : lamellar_conn(N_bc_l, N_mc_l),
        "K"         : 3.08 * pF,
        "tau_r"     : 0.3 * ms,
        "tau_d"     : 3.3 * ms,
        "delay"     : 1.5 * ms,
        "E"         : -86.0 * mV,
    },

    "mc_ampa_mgc": {
        "receptor"  : "ampa",
        "condition" : cross_lamellar_conn(N_mc_l, N_mgc_l),
        "p"         : 0.2,
        "K"         : 0.07 * pF,
        "tau_r"     : 0.1 * ms,
        "tau_d"     : 2.5 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_nmda_mgc": {
        "receptor"  : "nmda",
        "condition" : cross_lamellar_conn(N_mc_l, N_mgc_l),
        "p"         : 0.2,
        "K"         : 0.01 * pF,
        "tau_r"     : 0.33 * ms,
        "tau_d"     : 50.0 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_ampa_bc": {
        "receptor"  : "ampa",
        "condition" : cross_lamellar_conn(N_mc_l, N_bc_l),
        "p"         : 0.2,
        "K"         : 6.14 * pF,
        "tau_r"     : 2.5 * ms,
        "tau_d"     : 3.5 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_nmda_bc": {
        "receptor"  : "nmda",
        "condition" : cross_lamellar_conn(N_mc_l, N_bc_l),
        "p"         : 0.2,
        "K"         : 0.36 * pF,
        "tau_r"     : 10.0 * ms,
        "tau_d"     : 130.0 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_ampa_hipp": {
        "receptor"  : "ampa",
        "condition" : lamellar_conn(N_mc_l, N_hipp_l),
        "K"         : 4.09 * pF,
        "tau_r"     : 0.9 * ms,
        "tau_d"     : 3.6 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_nmda_hipp": {
        "receptor"  : "nmda",
        "condition" : lamellar_conn(N_mc_l, N_hipp_l),
        "K"         : 0.25 * pF,
        "tau_r"     : 3.6 * ms,
        "tau_d"     : 133.7 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },

    "hipp_gaba_mgc": {
        "receptor"  : "gaba",
        "condition" : lamellar_conn(N_hipp_l, N_mgc_l),
        "K"         : 3.0 * pF,
        "tau_r"     : 0.5 * ms,
        "tau_d"     : 6.0 * ms,
        "delay"     : 1.6 * ms,
        "E"         : -86.0 * mV,
    },
    "hipp_gaba_bc": {
        "receptor"  : "gaba",
        "condition" : lamellar_conn(N_hipp_l, N_bc_l),
        "K"         : 9.22 * pF,
        "tau_r"     : 0.4 * ms,
        "tau_d"     : 5.8 * ms,
        "delay"     : 1.6 * ms,
        "E"         : -86.0 * mV,
    },
    "hipp_gaba_mc": {
        "receptor"  : "gaba",
        "condition" : lamellar_conn(N_hipp_l, N_mc_l),
        "K"         : 2.05 * pF,
        "tau_r"     : 0.5 * ms,
        "tau_d"     : 6.0 * ms,
        "delay"     : 1.0 * ms,
        "E"         : -86.0 * mV,
    },
}
