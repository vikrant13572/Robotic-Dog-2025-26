import math
a1, a2, a3 = 5.0, 4.0, 3.0
def clamp(x, lo=-1.0, hi=1.0):
    return max(lo, min(hi, x))
def ik_xyz(x, y, z, a1=a1, a2=a2, a3=a3, degrees=True):
    sols = []
    r = math.hypot(x, y)
    if r < abs(a1) - 1e-9:
        return sols
    phi = math.atan2(y, x)
    cos_alpha = clamp(a1 / r)
    alpha = math.acos(cos_alpha)
    alphas = [alpha, -alpha]
    for alpha_val in alphas:
        t1 = phi - alpha_val
        Xp = r * math.sin(alpha_val)
        Zp = z
        L2, L3 = a2, a3
        dist2 = Xp**2 + Zp**2
        D = clamp((dist2 - L2**2 - L3**2) / (2 * L2 * L3))
        if abs(D) > 1:
            continue
        for sgn in [+1.0, -1.0]:
            sin_t3 = sgn * math.sqrt(max(0.0, 1.0 - D**2))
            t3 = math.atan2(sin_t3, D)
            num = L3 * math.sin(t3)
            den = L2 + L3 * math.cos(t3)
            t2 = math.atan2(Zp, Xp) - math.atan2(num, den)
            if degrees:
                sols.append((math.degrees(t1), math.degrees(t2), math.degrees(t3)))
            else:
                sols.append((t1, t2, t3))
    return sols
if __name__ == "__main__":
    x_in = float(input("Enter x: "))
    y_in = float(input("Enter y: "))
    z_in = float(input("Enter z: "))
    solutions = ik_xyz(x_in, y_in, z_in)
    if not solutions:
        print("No IK solution (target out of reach or singular).")
    else:
        first_sol = solutions[0]  
        print("First IK solution (t1, t2, t3) in degrees:")
        print(tuple(round(a, 4) for a in first_sol))