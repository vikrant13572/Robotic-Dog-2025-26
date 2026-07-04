import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation




# Forward kinematics function (same as your original)
def forward_kinematics(theta1, theta2, theta3):
    theta1_rad = np.radians(theta1)
    theta2_rad = np.radians(theta2)
    theta3_rad = np.radians(theta3)
    
    c1, s1 = np.cos(theta1_rad), np.sin(theta1_rad)
    c2, s2 = np.cos(theta2_rad), np.sin(theta2_rad)
    c3, s3 = np.cos(theta3_rad), np.sin(theta3_rad)
    
    R1_0 = np.array([
        [-s1, 0, c1],
        [c1, 0, s1],
        [0, 1, 0]
    ])
    
    R2_1 = np.array([
        [c2, -s2, 0],
        [s2, c2, 0],
        [0, 0, 1]
    ])
    
    R3_2 = np.array([
        [c3, -s3, 0],
        [s3, c3, 0],
        [0, 0, 1]
    ])
    
    d1_0 = np.array([[a1 * c1], [a1 * s1], [0]])
    d2_1 = np.array([[a2 * c2], [a2 * s2], [0]])
    d3_2 = np.array([[a3 * c3], [a3 * s3], [0]])
    
    p0 = np.array([0.0, 0.0, 0.0])
    p1 = d1_0.flatten()
    p2 = p1 + (R1_0 @ d2_1).flatten()
    p3 = p2 + (R1_0 @ R2_1 @ d3_2).flatten()
    
    return [p0, p1, p2, p3]


# Animation simulation function
def simulate_movement(angle1_range, angle2_range, angle3_range, frames=200, interval=50):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-12, 12])
    ax.set_ylim([-12, 12])
    ax.set_zlim([-12, 12])
    ax.set_xlabel('X (forward)')
    ax.set_ylabel('Y (lateral)')
    ax.set_zlabel('Z (up)')
    ax.set_title('3R Robotic Dog Leg - Forward Kinematics Simulation')
    
    # Initialize plot with start angles
    positions = forward_kinematics(angle1_range[0], angle2_range[0], angle3_range[0])
    line1, = ax.plot([positions[0][0], positions[1][0]], [positions[0][1], positions[1][1]], [positions[0][2], positions[1][2]], 'o-', linewidth=3, markersize=8, color='blue', label='Coxa (Link 1)')
    line2, = ax.plot([positions[1][0], positions[2][0]], [positions[1][1], positions[2][1]], [positions[1][2], positions[2][2]], 'o-', linewidth=3, markersize=8, color='green', label='Femur (Link 2)')
    line3, = ax.plot([positions[2][0], positions[3][0]], [positions[2][1], positions[3][1]], [positions[2][2], positions[3][2]], 'o-', linewidth=3, markersize=8, color='red', label='Tibia (Link 3)')
    end_eff, = ax.plot([positions[3][0]], [positions[3][1]], [positions[3][2]], 's', markersize=10, color='black', label='End Effector')
    
    text = ax.text2D(0.05, 0.95, '', transform=ax.transAxes, fontsize=10, verticalalignment='top',
                     bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    ax.legend()
    
    # Interpolate angles between start and end for smooth movement
    def interpolate_angles(frame):
        t = frame / frames
        # Goes from start to end and back to start using a sine wave for looping
        interp_t = 0.5 * (1 - np.cos(2 * np.pi * t))  # smooth oscillation between 0 and 1
        
        theta1 = angle1_range[0] + interp_t * (angle1_range[1] - angle1_range[0])
        theta2 = angle2_range[0] + interp_t * (angle2_range[1] - angle2_range[0])
        theta3 = angle3_range[0] + interp_t * (angle3_range[1] - angle3_range[0])
        
        return theta1, theta2, theta3
    
    # Update function for animation frames
    def update(frame):
        theta1, theta2, theta3 = interpolate_angles(frame)
        positions = forward_kinematics(theta1, theta2, theta3)
        
        line1.set_data_3d([positions[0][0], positions[1][0]], [positions[0][1], positions[1][1]], [positions[0][2], positions[1][2]])
        line2.set_data_3d([positions[1][0], positions[2][0]], [positions[1][1], positions[2][1]], [positions[1][2], positions[2][2]])
        line3.set_data_3d([positions[2][0], positions[3][0]], [positions[2][1], positions[3][1]], [positions[2][2], positions[3][2]])
        end_eff.set_data_3d([positions[3][0]], [positions[3][1]], [positions[3][2]])
        
        text.set_text(f"End Effector Position: ({positions[3][0]:.3f}, {positions[3][1]:.3f}, {positions[3][2]:.3f})")
        
        return line1, line2, line3, end_eff, text
    
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=interval, blit=False, repeat=True)
    
    plt.show()


#Link Lengths
a1, a2, a3 = -5.0, 5.9, 5.5

# Call simulate_movement with angle ranges for each joint (degrees)
simulate_movement(angle1_range=(0, 0), angle2_range=(0, 30), angle3_range=(0, -30))
