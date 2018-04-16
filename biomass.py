__author__ = 'zhangyl03'

# calculate the value of higher heating value (HVV) as mass fraction of the organic; x_ mean the mass fraction
# HVV is expressed in (MJ kg^-1)
def hhv(x_c, x_h, x_o, x_s=0, x_n=0, x_ash=0):
    return (0.3491 * x_c + 1.1783 * x_h + 0.1005 * x_s - 0.0151 * x_n - 0.1034 * x_o - 0.0221 * x_ash)*100

# LHV is expressed in (MJ kg^-1)
# h_vap means the enthalpy of vaporization of water at 25 C, 8.936 is the molecular mass ratio between H2O and H2
def lhv(hhv, x_h, w=0.18):
    h_vap = 2.444
    return hhv * (1-w) - h_vap * w - h_vap * x_h * 8.936 * (1-w)

# flue_temp means flue gas temperature, C
# flue_mass means flue gas mass, compared to 1 kg biomass, kg/(kg biomass)
def flue(f_lhv, air_temp, bio_temp, air_ratio, x_c, x_h, x_o, x_s=0, x_n=0, x_ash=0, loss=0):
    if air_ratio < 1.0:
        print 'Warning: air ratio less than 1.0, incomplete combustion!'
    x_co2 = (44.0/12.0)*x_c
    x_h2o = 9.0*x_h
    x_o2 = (air_ratio - 1.0) * (x_co2 - x_c + x_h2o - x_h - x_o)
    x_n2 = air_ratio * (x_co2 - x_c + x_h2o - x_h - x_o) * (28.0*0.79) / (32.0*0.21)
    cp_o2 = 1.1226
    cp_co2 = 1.2936
    cp_h2o = 2.4781
    cp_n2 = 1.2153
    sigma = cp_co2*x_co2 + cp_h2o*x_h2o + cp_o2*x_o2 + cp_n2*x_n2
    flue_temp = (f_lhv * (1-loss) * 1000 + (sigma*air_temp)) / (sigma)
    flue_mass = x_co2+x_h2o+x_o2+x_n2
    return flue_mass, flue_temp

# test results
x_c = 0.5
x_h = 0.06
x_o = 0.44

hhv = hhv(x_c, x_h, x_o,0.0,0.0,0.0)
lhv = lhv(hhv, x_h, 0.18)
flue_mass, flue_temp = flue(lhv, 20, 20, 2.0, x_c, x_h, x_o)
print hhv
print lhv
print flue_mass, flue_temp