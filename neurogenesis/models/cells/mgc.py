from brian2 import *
from neurogenesis.models.general import LIF

params = {
    "Cm"        : 106.2 * pF,
    "g_L"       : 3.4 * nS,
    "E_L"       : -75.0 * mV,
    "g_ahp_max" : 10.4 * nS,
    "tau_ahp"   : 20.0 * ms,
    "E_ahp"     : -80.0 * mV,
    "V_th"      : -53.4 * mV,
    "I_ampa"    : 0 * pA,
    "I_nmda"    : 0 * pA,
    "I_gaba"    : 0 * pA,
}

# Mature granule cell
def create_mgc(N):
  lif_eqs, threshold, reset, refractory = LIF()
  
  mgc = NeuronGroup(
      N          = N,
      model      = lif_eqs,
      threshold  = threshold,
      reset      = reset,
      refractory = refractory,
      method     = 'rk2',
  )
  for param, value in params.items():
    setattr(mgc, param, value)
  
  mgc.Vm = mgc.E_L
  
  return mgc
