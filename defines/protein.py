from sim_class import *

RECALC = False
calc_range = [0,180,0,90]
omega_calc = solid_angle(angle_range = calc_range)
datapath = 'D:/desktop/data/'
filename = 'protein_sandwich_100um_psi45.h5'

# sample definition
protein = compound(CP = 'C30H50O10N9S')
water = compound(CP = 'H2O')
Zn = compound(CP = 'Zn')

p1 = mix_compound([protein, Zn],[1,1e-2/15.])
p1 = sample(p1,1.05,15e-4)

w1 = sample(water,1,47.5e-4)

p2 = mix_compound([water, protein, Zn],[.85,.15,1e-4])
p2 = sample(p2,1.05,100e-4)
s = sample_multilayer([w1,p1,w1])

# detector definition
det_center = 90
if det_center == 90:
	x = 10
	angle_range_gen = lambda x: [90-x, 90+x, -x, x]
elif det_center == 180:
	x = 11.5
	angle_range_gen = lambda x: [180-x, 180, -90, 90]
elif det_center == 0:
	x = 11.5
	angle_range_gen = lambda x: [0, x, 0, 360]
_omega=solid_angle(angle_range = angle_range_gen(x))
ch = channel()
resp = response()
det = detector(ch, resp, omega = deepcopy(_omega))

# illumination definition
il = illumination(ev0=1e4, psi=45, alpha=0)

# plot specs
PLOT_SPEC = True
DET_RESPONSE = True
xlim = [0,1.1e4]
ylim = [1e-16,5e-3]

# peak to background and snr calculations
CALC_SNR = False
from sim_snr import *
peak_center = 8630 # ev
bg_leftshift = 250 # ev
bg_rightshift = 250 # ev
pnb_func = pnb_expfit
pnb_func = pnb_fixedwidth
pnb_func = pnb_ascalc
element = 'Zn' # needed for pnb_ascalc
openings = np.arange(1,91)