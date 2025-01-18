from brian2 import *
from neurogenesis.models.general.lif import LIF

params = {
    "Cm"        : 106.2 * pF,
    "g_L"       : 3.4 * nS,
    "E_L"       : -75.0 * mV,
    "g_ahp_max" : 10.4 * nS,
    "tau_ahp"   : 20.0 * ms,
    "E_ahp"     : -80.0 * mV,
    "V_th"      : -53.4 * mV,
    "I_ampa"    : -250 * pA,
    "I_nmda"    : 0 * pA,
    "I_gaba"    : 0 * pA,
}

lif_eqs = LIF()

gc = NeuronGroup(
    10,
    model      = lif_eqs,
    threshold  = 'Vm > V_th',
    reset      = 'Vm = E_L',
    method     = 'rk2',
    refractory = 0*ms          # A way to have lastspike
)
for param, value in params.items():
  setattr(gc, param, value)

gc.Vm = gc.E_L

