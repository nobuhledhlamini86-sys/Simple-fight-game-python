import random

print("welcome to fight club")

player_name = input("Enter your fighter name:" )

player_health = 100
enemy_health = 100

while player_health > 0 and enemy_health > 0:
    print("\n" + player_name + "Health:", player_health)
    print("Enemy Health:", enemy_health)

    print("\nChoose your move:")
    print("1. kick")
    print("2. punch")
    print("3. jump")
    print("4. Heal")

    choice = input("Enter 1, 2, 3 or 4:")

    if choice =="1":
        damage = random.randint(10, 20)
        enemy_health -= damage
        print("you hit the enemy for", damage)

        enemy_damage = random.randint(5,15)
        player_health -= enemy_damage
        print("enemy hit you for", enemy_damage)
    
    elif choice == "2":
        damage = random.randint(10,20)
        enemy_health -= damage
        print(" you used PUNCH!!")
        print("you damaged the enemy for", damage)

        enemy_damage = random.randint(5,15)
        player_health -= enemy_damage
        print("Enemy attacked you for", enemy_damage)

    elif choice == "3":
        dodge = random.randint(1, 2)

        if dodge == 1:
            print("You jumped and dodged the attack!")

        else:
            enemy_damage = random.randint(5, 15)  
            player_health -= enemy_damage

            print("jump failed!")
            print("Enemy attacked you for", enemy_damage)

    elif choice == "4":
        heal = random.randint(10,20)
        player_health += heal
        print("you heal for", heal)

        enemy_damage = random.randint(5,15)
        player_health -= enemy_damage
        print("Enemy hits you for", enemy_damage)

if player_health > 0:
    print("\n you win, " + player_health + " !")         
else:
    print("\n you lost. Better luck next time !")