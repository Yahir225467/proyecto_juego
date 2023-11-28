import threading



def load_resources():
    # Load images
    for img in meteor_list:
        meteor_images.append(pygame.image.load(img).convert())

    # Load explosion images
    for i in range(9):
        file = "assets/regularExplosion0{}.png".format(i)
        img = pygame.image.load(file).convert()
        img.set_colorkey(BLACK)
        img_scale = pygame.transform.scale(img, (70, 70))
        explosion_anim.append(img_scale)

    # Load background
    global background
    background = pygame.image.load("assets/background.png").convert()

    # Load sounds
    global laser_sound, explosion_sound
    laser_sound = pygame.mixer.Sound("assets/laser5.ogg")
    explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
    pygame.mixer.music.load("assets/music.ogg")
    pygame.mixer.music.set_volume(0.2)

# Function to start the game
def start_game():
    # Initialize Pygame and other game elements

    # Start the music
    pygame.mixer.music.play(loops=-1)

    # Game loop
    # ...


# Load resources in a separate thread
resource_thread = threading.Thread(target=load_resources)
resource_thread.start()

# Wait for the resource thread to complete loading before starting the game
resource_thread.join()

# Start the game in a separate thread
game_thread = threading.Thread(target=start_game)
game_thread.start()
