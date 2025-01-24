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
        "receptor" : "ampa_1",
        "p"        : 0.2,
        "g_max"    : 0.89 * nS,
        "tau_r"    : 0.1 * ms,
        "tau_d"    : 2.5 * ms,
        "delay"    : 3.0 * ms,
        "E"        : 0 * mV,
    },
    "ec_nmda_mgc": {
        "receptor" : "nmda_1",
        "p"        : 0.2,
        "g_max"    : 0.15 * nS,
        "tau_r"    : 0.33 * ms,
        "tau_d"    : 50.0 * ms,
        "delay"    : 3.0 * ms,
        "E"        : 0 * mV,
    },
    "ec_ampa_igc": {
        "receptor" : "ampa_1",
        "p"        : 0.2,
        "g_max"    : 0.89 * nS,
        "tau_r"    : 0.1 * ms,
        "tau_d"    : 2.5 * ms,
        "delay"    : 3.0 * ms,
        "E"        : 0 * mV,
    },
    "ec_nmda_igc": {
        "receptor" : "nmda_1",
        "p"        : 0.2,
        "g_max"    : 0.15 * nS,
        "tau_r"    : 0.33 * ms,
        "tau_d"    : 50.0 * ms,
        "delay"    : 3.0 * ms,
        "E"        : 0 * mV,
    },
    "ec_ampa_bc": {
        "receptor" : "ampa_1",
        "g_max"    : 0.75 * nS,
        "tau_r"    : 2.0 * ms,
        "tau_d"    : 6.3 * ms,
        "delay"    : 3.0 * ms,
        "E"        : 0 * mV,
    },
    "ec_nmda_bc": {
        "receptor" : "nmda_1",
        "g_max"    : 0.13 * nS,
        "tau_r"    : 6.6 * ms,
        "tau_d"    : 126.0 * ms,
        "delay"    : 3.0 * ms,
        "E"        : 0 * mV,
    },

    "mgc_ampa_bc": {
        "receptor"  : "ampa_2",
        "condition" : lamellar_conn(N_mgc_l, N_bc_l),
        "g_max"     : 0.38 * nS,
        "tau_r"     : 2.5 * ms,
        "tau_d"     : 3.5 * ms,
        "delay"     : 0.8 * ms,
        "E"         : 0 * mV,
    },
    "mgc_nmda_bc": {
        "receptor"  : "nmda_2",
        "condition" : lamellar_conn(N_mgc_l, N_bc_l),
        "g_max"     : 0.02 * nS,
        "tau_r"     : 10.0 * ms,
        "tau_d"     : 130.0 * ms,
        "delay"     : 0.8 * ms,
        "E"         : 0 * mV,
    },
    "mgc_ampa_mc": {
        "receptor"  : "ampa_1",
        "condition" : lamellar_conn(N_mgc_l, N_mc_l),
        "g_max"     : 9.58 * nS,
        "tau_r"     : 0.5 * ms,
        "tau_d"     : 6.2 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },
    "mgc_nmda_mc": {
        "receptor"  : "nmda_1",
        "condition" : lamellar_conn(N_mgc_l, N_mc_l),
        "g_max"     : 1.71 * nS,
        "tau_r"     : 4.0 * ms,
        "tau_d"     : 100.0 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },
    "mgc_ampa_hipp": {
        "receptor"  : "ampa_1",
        "condition" : lamellar_conn(N_mgc_l, N_hipp_l),
        "g_max"     : 0.08 * nS,
        "tau_r"     : 0.3 * ms,
        "tau_d"     : 0.6 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },
    "mgc_nmda_hipp": {
        "receptor"  : "nmda_1",
        "condition" : lamellar_conn(N_mgc_l, N_hipp_l),
        "g_max"     : 0.004 * nS,
        "tau_r"     : 1.2 * ms,
        "tau_d"     : 22.2 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },

    "igc_ampa_bc": {
        "receptor"  : "ampa_3",
        "condition" : lamellar_conn(N_igc_l, N_bc_l),
        "g_max"     : 0.38 * nS,
        "tau_r"     : 2.5 * ms,
        "tau_d"     : 3.5 * ms,
        "delay"     : 0.8 * ms,
        "E"         : 0 * mV,
    },
    "igc_nmda_bc": {
        "receptor"  : "nmda_3",
        "condition" : lamellar_conn(N_igc_l, N_bc_l),
        "g_max"     : 0.02 * nS,
        "tau_r"     : 10.0 * ms,
        "tau_d"     : 130.0 * ms,
        "delay"     : 0.8 * ms,
        "E"         : 0 * mV,
    },
    "igc_ampa_mc": {
        "receptor"  : "ampa_2",
        "condition" : lamellar_conn(N_igc_l, N_mc_l),
        "g_max"     : 9.58 * nS,
        "tau_r"     : 0.5 * ms,
        "tau_d"     : 6.2 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },
    "igc_nmda_mc": {
        "receptor"  : "nmda_2",
        "condition" : lamellar_conn(N_igc_l, N_mc_l),
        "g_max"     : 1.71 * nS,
        "tau_r"     : 4.0 * ms,
        "tau_d"     : 100.0 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },
    "igc_ampa_hipp": {
        "receptor"  : "ampa_2",
        "condition" : lamellar_conn(N_igc_l, N_hipp_l),
        "g_max"     : 0.08 * nS,
        "tau_r"     : 0.3 * ms,
        "tau_d"     : 0.6 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },
    "igc_nmda_hipp": {
        "receptor"  : "nmda_2",
        "condition" : lamellar_conn(N_igc_l, N_hipp_l),
        "g_max"     : 0.004 * nS,
        "tau_r"     : 1.2 * ms,
        "tau_d"     : 22.2 * ms,
        "delay"     : 1.5 * ms,
        "E"         : 0 * mV,
    },

    "bc_gaba_mgc": {
        "receptor"  : "gaba_1",
        "condition" : lamellar_conn(N_bc_l, N_mgc_l),
        "g_max"     : 15.0 * nS,
        "tau_r"     : 0.9 * ms,
        "tau_d"     : 6.8 * ms,
        "delay"     : 0.85 * ms,
        "E"         : -86.0 * mV,
    },
    "bc_gaba_mc": {
        "receptor"  : "gaba_1",
        "condition" : lamellar_conn(N_bc_l, N_mc_l),
        "g_max"     : 3.08 * nS,
        "tau_r"     : 0.3 * ms,
        "tau_d"     : 3.3 * ms,
        "delay"     : 1.5 * ms,
        "E"         : -86.0 * mV,
    },

    "mc_ampa_mgc": {
        "receptor"  : "ampa_2",
        "condition" : cross_lamellar_conn(N_mc_l, N_mgc_l),
        "p"         : 0.2,
        "g_max"     : 0.07 * nS,
        "tau_r"     : 0.1 * ms,
        "tau_d"     : 2.5 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_nmda_mgc": {
        "receptor"  : "nmda_2",
        "condition" : cross_lamellar_conn(N_mc_l, N_mgc_l),
        "p"         : 0.2,
        "g_max"     : 0.01 * nS,
        "tau_r"     : 0.33 * ms,
        "tau_d"     : 50.0 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_ampa_igc": {
        "receptor"  : "ampa_2",
        "condition" : cross_lamellar_conn(N_mc_l, N_igc_l),
        "p"         : 0.2,
        "g_max"     : 0.07 * nS,
        "tau_r"     : 0.1 * ms,
        "tau_d"     : 2.5 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_nmda_igc": {
        "receptor"  : "nmda_2",
        "condition" : cross_lamellar_conn(N_mc_l, N_igc_l),
        "p"         : 0.2,
        "g_max"     : 0.01 * nS,
        "tau_r"     : 0.33 * ms,
        "tau_d"     : 50.0 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_ampa_bc": {
        "receptor"  : "ampa_4",
        "condition" : cross_lamellar_conn(N_mc_l, N_bc_l),
        "p"         : 0.2,
        "g_max"     : 6.14 * nS,
        "tau_r"     : 2.5 * ms,
        "tau_d"     : 3.5 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_nmda_bc": {
        "receptor"  : "nmda_4",
        "condition" : cross_lamellar_conn(N_mc_l, N_bc_l),
        "p"         : 0.2,
        "g_max"     : 0.36 * nS,
        "tau_r"     : 10.0 * ms,
        "tau_d"     : 130.0 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_ampa_hipp": {
        "receptor"  : "ampa_3",
        "condition" : lamellar_conn(N_mc_l, N_hipp_l),
        "g_max"     : 4.09 * nS,
        "tau_r"     : 0.9 * ms,
        "tau_d"     : 3.6 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },
    "mc_nmda_hipp": {
        "receptor"  : "nmda_3",
        "condition" : lamellar_conn(N_mc_l, N_hipp_l),
        "g_max"     : 0.25 * nS,
        "tau_r"     : 3.6 * ms,
        "tau_d"     : 133.7 * ms,
        "delay"     : 3.0 * ms,
        "E"         : 0 * mV,
    },

    "hipp_gaba_mgc": {
        "receptor"  : "gaba_2",
        "condition" : lamellar_conn(N_hipp_l, N_mgc_l),
        "g_max"     : 3.0 * nS,
        "tau_r"     : 0.5 * ms,
        "tau_d"     : 6.0 * ms,
        "delay"     : 1.6 * ms,
        "E"         : -86.0 * mV,
    },
    "hipp_gaba_bc": {
        "receptor"  : "gaba_1",
        "condition" : lamellar_conn(N_hipp_l, N_bc_l),
        "g_max"     : 9.22 * nS,
        "tau_r"     : 0.4 * ms,
        "tau_d"     : 5.8 * ms,
        "delay"     : 1.6 * ms,
        "E"         : -86.0 * mV,
    },
    "hipp_gaba_mc": {
        "receptor"  : "gaba_2",
        "condition" : lamellar_conn(N_hipp_l, N_mc_l),
        "g_max"     : 2.05 * nS,
        "tau_r"     : 0.5 * ms,
        "tau_d"     : 6.0 * ms,
        "delay"     : 1.0 * ms,
        "E"         : -86.0 * mV,
    },
}
