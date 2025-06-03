import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))

# Big circle: FOL
fol = plt.Circle((0, 0), 3, edgecolor='black', facecolor='#d6eaf8', lw=2)
ax.add_patch(fol)
ax.text(0, 2.6, "First-Order Logic", fontsize=14, ha='center', weight='bold')

# Horn Logic inside FOL, left
horn = plt.Circle((-1.2, 0), 1.2, edgecolor='blue', facecolor='#85c1e9', lw=2)
ax.add_patch(horn)
ax.text(-1.2, -0.6, "Horn Logic", fontsize=12, ha='center', color='white', weight='bold')

# Datalog inside Horn Logic
datalog = plt.Circle((-1.2, 0.4), 0.5, edgecolor='navy', facecolor='#2874a6', lw=2)
ax.add_patch(datalog)
ax.text(-1.2, 0.4, "Datalog", fontsize=10, ha='center', color='white', weight='bold')

# Description Logic inside FOL, right
dl = plt.Circle((1.3, 0), 1.3, edgecolor='green', facecolor='#a9dfbf', lw=2)
ax.add_patch(dl)
ax.text(1.3, 0.8, "Description Logic", fontsize=12, ha='center', weight='bold')

# ALC inside DL
alc = plt.Circle((1.0, 0.2), 0.4, edgecolor='darkgreen', facecolor='#58d68d', lw=2)
ax.add_patch(alc)
ax.text(1.0, 0.2, r'$\mathcal{ALC}$', fontsize=10, ha='center', weight='bold')

# EL inside DL
el = plt.Circle((1.6, -0.3), 0.4, edgecolor='darkgreen', facecolor='#58d68d', lw=2)
ax.add_patch(el)
ax.text(1.6, -0.3, r'$\mathcal{EL}$', fontsize=10, ha='center', weight='bold')

# Propositional Logic inside FOL, bottom center
pl = plt.Circle((0, -1.7), 0.8, edgecolor='orange', facecolor='#f7dc6f', lw=2)
ax.add_patch(pl)
ax.text(0, -1.7, "Propositional\nLogic", fontsize=12, ha='center', weight='bold')

# Plot settings
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.axis('off')
plt.title("Hierarchy of Logics", fontsize=16)

plt.tight_layout()
plt.savefig("venn_diagram_logics.pdf", dpi=300)
