# ... (código previo del juego)

# Mantén un contador de turnos para emular el comportamiento de Round Robin
turn_counter = 0

while running:
    # Lógica del juego por turnos (emulando Round Robin)
    if turn_counter % 2 == 0:
        # Acciones del jugador en este turno
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
        # Actualiza el jugador
        player.update()

    else:
        # Acciones de los meteoros en este turno
        for meteor in meteor_list:
            meteor.update()

        # Colisiones meteoros - jugador
        hits = pygame.sprite.spritecollide(player, meteor_list, True)
        for hit in hits:
            player.shield -= 25
            if player.shield <= 0:
                game_over = True

    # Incrementa el contador de turnos
    turn_counter += 1

    # ... (código restante del juego)
