import matplotlib.pyplot as plt
from figures import PATH as FIGURES_PATH
from scripts import PATH as SCRIPTS_PATH

fig, ax = plt.subplots(figsize=(10, 10))

# Big circle: FOL
fol = plt.Circle((0, 0), 2.9, edgecolor='black', facecolor='#d6eaf8', lw=2)
ax.add_patch(fol)
ax.text(0, 1.8, "First-Order Logic", fontsize=24, ha='center', weight='bold')

# Horn Logic inside FOL, left
horn = plt.Circle((-1, -1), 1.4, edgecolor='blue', facecolor='#85c1e9', lw=2)
ax.add_patch(horn)
ax.text(-1, 0, "Horn Logic", fontsize=18, ha='center', color='white', weight='bold')

# Datalog inside Horn Logic
datalog = plt.Circle((-1, -1.2), 1, edgecolor='navy', facecolor='#2874a6', lw=2)
ax.add_patch(datalog)
ax.text(-1, -0.6, "Datalog", fontsize=16, ha='center', color='white', weight='bold')

# Description Logic inside FOL, right
dl = plt.Circle((1.4, 0.2), 1.2, edgecolor='green', facecolor='#a9dfbf', lw=2)
ax.add_patch(dl)
ax.text(1.4, 0.65, "Description\nLogic", fontsize=18, ha='center', weight='bold')

# ALC inside DL
alc = plt.Circle((1.0, 0.15), 0.4, edgecolor='darkgreen', facecolor='#58d68d', lw=2)
ax.add_patch(alc)
ax.text(1.0, 0.15, r'$\mathcal{ALC}$', fontsize=16, ha='center', weight='bold')

# EL inside DL
el = plt.Circle((1.8, -0.35), 0.4, edgecolor='darkgreen', facecolor='#58d68d', lw=2)
ax.add_patch(el)
ax.text(1.8, -0.35, r'$\mathcal{EL}$', fontsize=16, ha='center', weight='bold')

# Propositional Logic inside FOL, bottom center
pl = plt.Circle((-1, -1.4), 0.65, edgecolor='orange', facecolor='#f7dc6f', lw=2)
ax.add_patch(pl)
ax.text(-1, -1.6, "Propositional\nLogic", fontsize=14, ha='center', weight='bold')

# Plot settings
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.axis('off')
# plt.title("Hierarchy of Logics", fontsize=16)

# remove white space around the figure
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.tight_layout()
plt.savefig(FIGURES_PATH / "venn_diagram_logics.pdf", dpi=300)
plt.savefig(SCRIPTS_PATH / "venn_diagram_logics.png", dpi=300)
