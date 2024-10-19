import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Define the transfer function parameters
zeros = [2, -4]  # zeros at s = 2 and s = -4
poles = [-1 + 2j, -1 - 2j]  # poles at s = -1 ± 2j

# Create the transfer function for open loop G(s)H(s) = K * (s+4)(s-2) / ((s+1-2j)(s+1+2j))
numerator = np.poly(zeros)
denominator = np.poly(poles)

# Define the open loop transfer function without gain K
system_open_loop = ctl.TransferFunction(numerator, denominator)

# Generate the root locus plot
plt.figure(figsize=(10, 7))
ctl.root_locus(system_open_loop, grid=True)
plt.title("Root Locus of the System")
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid(True)
plt.show()
