import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
temperature = [30, 35, 40, 38, 45]
fig, ax = plt.subplots()
ax.plot(hours, temperature, label="Actual Temperature")
ax.set_title("Machine Temperature Monitoring")
ax.set_xlabel("Hours")
ax.set_ylabel("Temperature (°C)")
ax.legend()
plt.show()

machines = ["Machine A", "Machine B", "Machine C", "Machine D"]
production = [120, 180, 150, 200]
fig, ax = plt.subplots()
ax.bar(machines, production)
ax.set_title("Machine Production Comparison")
ax.set_xlabel("Machines")
ax.set_ylabel("Components Produced")
plt.show()

load = [50, 100, 150, 200, 250]
deformation = [2.1, 4.3, 6.2, 8.5, 10.4]
fig, ax = plt.subplots()
ax.scatter(load, deformation)
ax.set_title("Load vs Deformation Analysis")
ax.set_xlabel("Applied Load (N)")
ax.set_ylabel("Deformation (mm)")
plt.show()

temperatures = [
    30,
    32,
    35,
    36,
    38,
    40,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    52,
    54,
    55,
    58,
    60,
]
fig, ax = plt.subplots()
ax.hist(temperatures, bins=[30, 40, 50, 60, 70])
ax.set_title("Machine Temperature Distribution")
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Number of Machines")
plt.show()
