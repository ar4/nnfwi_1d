import numpy as np
from nnfwi_1d import propagators

nx = 100
num_data=50000
num_steps = 1250
source_len = 10
minvel = 1450
maxvel = 5000

dt=0.0006
dx=5

np.random.seed(0)

def ricker(f, length=0.128, dt=0.001):
    t = np.arange(-length/2, (length-dt)/2, dt)
    y = (1.0 - 2.0*(np.pi**2)*(f**2)*(t**2)) * np.exp(-(np.pi**2)*(f**2)*(t**2))
    return t, y
             
f = 50 # A low wavelength of 25 Hz
t, w = ricker(f, 70*dt, dt)
w = w.astype(np.float32)

#sources = np.zeros([num_data, source_len], np.float32)
#sources[:,:-1] = np.random.rand(num_data, source_len-1)-0.5
#sources[:,-1] = -np.sum(sources[:,:-1],axis=1)
sources = np.tile(w, [num_data, 1])
print(sources.shape)

data = np.zeros([num_data, num_steps], np.float32)

#V = np.random.rand(num_data, nx).astype(np.float32)*(maxvel-minvel)+minvel
V = np.zeros([num_data, nx], np.float32)
for i in range(num_data):
    v0 = np.random.rand()*(maxvel-minvel)+minvel
    v1 = np.random.rand()*(maxvel-minvel)+minvel
    vidx = np.random.randint(1,nx-1)
    V[i, :vidx] = v0
    V[i, vidx:] = v1

for i in range(num_data):
    p=propagators.propagator(V[i,:], dx, dt)
    data[i,:] = p.step(num_steps, sources[i,:])

np.save('data/sources_1layer.npy', sources)
np.save('data/data_1layer.npy', data)
np.save('data/V_1layer.npy', V)
