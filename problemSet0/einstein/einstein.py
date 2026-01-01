def mass_to_energy(mass):
    energy=int(mass*(300000000**2))
    return energy

def main():
    mass=int(input())
    energy=mass_to_energy(mass)
    print(energy)

main()
