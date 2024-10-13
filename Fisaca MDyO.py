import matplotlib.pyplot as plt

def plot_mode_normal(positions, amplitudes, labels, mode):
    fig, ax = plt.subplots()
    ax.set_title(f'Modo Normal de Oscilación {mode}')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')

    # Dibujando las masas
    for pos, amp, label in zip(positions, amplitudes, labels):
        ax.plot(pos, 0, 'o', markersize=20)
        ax.text(pos, 0.1, f'{label}', ha='center')
        if amp != 0:
            ax.arrow(pos, 0, 0, 0.5 if amp > 0 else -0.5, head_width=0.1, head_length=0.1, fc='black', ec='black')

    # Dibujando los resortes
    for i in range(len(positions) - 1):
        ax.plot([positions[i], positions[i+1]], [0, 0], 'k-')

    plt.axis('off')
    plt.show()

# Modo 1
positions1 = [-1, 0, 1]
amplitudes1 = [1, 0, 1]
labels1 = ['A1', '0', 'A1']
plot_mode_normal(positions1, amplitudes1, labels1, 1)

# Modo 2
positions2 = [-1, 0, 1]
amplitudes2 = [-1, 0, 1]
labels2 = ['-A1', '0', 'A1']
plot_mode_normal(positions2, amplitudes2, labels2, 2)

# Modo 3
positions3 = [-1, 0, 1]
amplitudes3 = [1, -2, 1]
labels3 = ['A1', '-2A1', 'A1']
plot_mode_normal(positions3, amplitudes3, labels3, 3)
