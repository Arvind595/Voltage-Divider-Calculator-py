def solve_3_resistor_divider(Vin, Vout1, Vout2, R3=5000):
    """
    Solves for R1, R2 in a 3-resistor divider given Vin, Vout1, Vout2, and R3.
    Also calculates total current and power dissipated by each resistor.

    Returns:
    - Tuple: (R1, R2, R3, I_total, P_R1, P_R2, P_R3)
    """
    # Calculate total resistance from Vout2
    R_total = R3 * Vin / Vout2

    R1 = R_total * (Vin - Vout1) / Vin
    R2 = R_total - R1 - R3

    # Current from the source
    I_total = Vin / (R1 + R2 + R3)

    # Power dissipated in each resistor
    P_R1 = I_total ** 2 * R1
    P_R2 = I_total ** 2 * R2
    P_R3 = I_total ** 2 * R3

    return R1, R2, R3, I_total, P_R1, P_R2, P_R3

# Example usage
Vin = 12.0
Vout1 = 8.7
Vout2 = 6.7

R1, R2, R3, I, P1, P2, P3 = solve_3_resistor_divider(Vin, Vout1, Vout2)

print(f"Input Voltages:")
print(f"  Vin    = {Vin:.4f} V")
print(f"  Vout1  = {Vout1:.4f} V")
print(f"  Vout2  = {Vout2:.4f} V\n")

print(f"Resistor values:")
print(f"  R1 = {R1:.4f} Ω")
print(f"  R2 = {R2:.4f} Ω")
print(f"  R3 = {R3:.4f} Ω\n")

print(f"Total current from source: {I*1000:.4f} mA")

print(f"Power dissipated:")
print(f"  P_R1 = {P1:.4f} W")
print(f"  P_R2 = {P2:.4f} W")
print(f"  P_R3 = {P3:.4f} W")
