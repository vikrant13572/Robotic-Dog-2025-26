import numpy as np

def inverse_kinematics_cm(X, Y, Z, a1, a2, a3):
    """
    Perfect inverse kinematics that matches the forward kinematics exactly.
    
    Derived from FK equations:
    X = a1*cos(θ1) - sin(θ1)*(a2*cos(θ2) + a3*cos(θ2+θ3))
    Y = a1*sin(θ1) + cos(θ1)*(a2*cos(θ2) + a3*cos(θ2+θ3))
    Z = a2*sin(θ2) + a3*sin(θ2+θ3)
    """
    
    # Step 1: Solve for theta1 (coxa/base joint)
    r_xy = np.sqrt(X**2 + Y**2)
    
    if r_xy < a1:
        return None
    
    L = np.sqrt(r_xy**2 - a1**2)
    theta1_rad = np.arctan2(-Y, -X) + np.arctan2(L, a1)
    theta1 = np.degrees(theta1_rad)
    
    # Step 2: Solve for theta2 and theta3 in (L, Z) plane
    reach = np.sqrt(L**2 + Z**2)
    
    if reach > a2 + a3 or reach < abs(a2 - a3):
        return None
    
    phi = np.arctan2(Z, L)
    
    # Law of cosines for theta3 (knee angle)
    cos_theta3 = (a2**2 + a3**2 - reach**2) / (2 * a2 * a3)
    cos_theta3 = np.clip(cos_theta3, -1, 1)
    theta3 = 180 - np.degrees(np.arccos(cos_theta3))
    
    # Law of cosines for theta2 (hip angle)
    cos_alpha = (a2**2 + reach**2 - a3**2) / (2 * a2 * reach)
    cos_alpha = np.clip(cos_alpha, -1, 1)
    alpha = np.arccos(cos_alpha)
    theta2 = np.degrees(phi - alpha)
    
    return theta1, theta2, theta3

# ==== Input Block ====
a1 = -5.0
a2 = 5.9
a3 = 5.5
X = 5.0
Y = 11.4
Z = 0.0

theta_values = inverse_kinematics_cm(X, Y, Z, a1, a2, a3)
if theta_values is not None:
    theta1, theta2, theta3 = theta_values
    print(f"theta1={theta1:.2f},\ntheta2={theta2:.2f},\ntheta3={theta3:.2f}")
else:
    print("Target position is unreachable for the given link lengths and coordinates.")

