__author__ = 'zhangyl03'

# calculate the value of higher heating value (HVV) as mass fraction of the organic; x_ mean the mass fraction
# HVV is expressed in (MJ kg^-1)
def HHV(x_c, x_h, x_o, x_s=0, x_n=0, x_ash=0):
    return (0.3491 * x_c + 1.1783 * x_h + 0.1005 * x_s - 0.0151 * x_n - 0.1034 * x_o - 0.0221 * x_ash)*100

# LHV is expressed in (MJ kg^-1)
# h_vap means the enthalpy of vaporization of water at 25 C, 8.936 is the molecular mass ratio between H2O and H2
def LHV(hhv, x_h, w=0.18):
    h_vap = 2.444
    return hhv * (1-w) - h_vap * w - h_vap * x_h * 8.936 * (1-w)

x_c = 0.5
x_h = 0.06
x_o = 0.44

hhv = HHV(x_c, x_h, x_o)
print hhv
print LHV(hhv, x_h)