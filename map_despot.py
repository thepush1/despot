import matplotlib.pyplot as plt

points = {
    '1. Viterbo': (12.1075465, 42.4204278), '2 & 5. Malta': (14.5220972, 35.8880695),
    '3. Creta': (24.8092691, 35.240117), '4. Chios': (26.1360248, 38.3712527),
    '6. Spania': (1.5208624, 41.5911589), '7. Montpellier': (3.8761323, 43.6108535),
    '8. Metz': (6.1760223, 49.1178601), '9. Paris': (2.0885134, 48.8999714),
    '10. Thérouanne': (2.256984, 50.637833), '11. Mansfeld': (11.4587747, 51.5981233),
    '12. Renty': (2.073133, 50.582903), '13. Antwerp': (4.4149903, 51.2199302),
    '14. Brussels': (4.3572001, 50.8477029), '15. Wittenberg': (12.6411506, 51.8704643),
    '16. Lübeck': (10.6865593, 53.8654673), '17. Copenhaga': (12.5683371, 55.6760968),
    '18. Rostock': (12.0991466, 54.0924406), '19. Gdańsk': (18.6466384, 54.3520252),
    '20. Kaliningrad': (20.4522144, 54.7104264), '21. Vilnius': (25.2796514, 54.6871555),
    '22. Cracovia': (19.9449799, 50.0646501), '23 & 29. Suceava': (26.2732302, 47.6634521),
    '24. Brașov': (25.5887252, 45.6426802), '25. Cluj-Napoca': (23.6236353, 46.7712101),
    '26. Lviv': (24.029717, 49.839683), '27. Viena': (16.3713095, 48.2080696),
    '28. Kežmarok': (20.4306967, 49.1332664),
}

sequence = [
    '1. Viterbo', '2 & 5. Malta', '3. Creta', '4. Chios', '2 & 5. Malta', '6. Spania', 
    '7. Montpellier', '8. Metz', '9. Paris', '10. Thérouanne', '11. Mansfeld', 
    '12. Renty', '13. Antwerp', '14. Brussels', '15. Wittenberg', '16. Lübeck', 
    '17. Copenhaga', '18. Rostock', '19. Gdańsk', '20. Kaliningrad', '21. Vilnius', 
    '22. Cracovia', '23 & 29. Suceava', '24. Brașov', '25. Cluj-Napoca', '26. Lviv', 
    '27. Viena', '28. Kežmarok', '23 & 29. Suceava'
]

fig, ax = plt.subplots(figsize=(16, 12), facecolor='#F7F5F0')
ax.set_facecolor('#F7F5F0')

x_path = [points[loc][0] for loc in sequence]
y_path = [points[loc][1] for loc in sequence]
ax.plot(x_path, y_path, color='#A89F91', linewidth=1.2, linestyle='-', alpha=0.6, zorder=1)

x_points = [coords[0] for coords in points.values()]
y_points = [coords[1] for coords in points.values()]
ax.scatter(x_points, y_points, color='#2C3E50', s=60, edgecolors='#F7F5F0', linewidth=1.5, zorder=2)
ax.scatter(x_points, y_points, color='#D4AF37', s=20, zorder=3)

for name, (x, y) in points.items():
    ax.text(x + 0.2, y + 0.2, name, fontsize=9, color='#1A1A1A', 
            fontfamily='serif', fontweight='500', 
            bbox=dict(facecolor='#F7F5F0', edgecolor='none', alpha=0.7, pad=0.5))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

plt.text(0.5, 0.95, "CĂLĂTORIILE LUI DESPOT VODĂ", fontsize=22, fontfamily='serif', 
         color='#2C3E50', fontweight='bold', ha='center', va='center', transform=ax.transAxes)
plt.text(0.5, 0.91, "O hartă minimalistă a traseului parcurs prin Europa secolului al XVI-lea", fontsize=12, fontfamily='serif', 
         color='#555555', ha='center', va='center', transform=ax.transAxes, style='italic')

plt.tight_layout()
plt.savefig('infografie_despot_voda.png', dpi=300, bbox_inches='tight')
print("Imaginea a fost salvată ca 'infografie_despot_voda.png'.")
