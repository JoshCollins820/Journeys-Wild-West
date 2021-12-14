## JOURNEYS WILD WEST
## v0.4
## Developed by: Josh Collins
## --------------------------

# Modules
import pygame
import random
import time
import sys
import pickle

# SimpleGUI Module
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# window resolution
height = 600
width = 600

# pygame initialization
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
clock = pygame.time.Clock()
random.seed()

# window properties
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("JOURNEYS: WILD WEST")
pygame.display.set_icon(pygame.image.load("assets/icon/window_icon.png"))
collapse = True
version = "0.4"

# values and statements
if collapse:
    # MAKE SURE TO ALSO CHANGE VALUES IN RESETVALUES METHOD -------------------------------------------------------
    # player vals
    playerHP = 100
    bodyWeight = 12
    moneyCount = 0
    revRoundsMag = 6
    revRoundsTotal = 24
    revolverFireRate = 12
    revolverReloadSpeed = 500
    sniperRoundsMag = 1
    sniperRoundsTotal = 3
    hpPotionCount = 5
    drinkTime = 100
    score = 0
    highscore = 0
    masterVolumeStored = 0
    musicVolumeStored = 0

    # speed
    speedMove = 50
    boardWalk = 80
    cloudMove = 8
    cloudAuto = 0.2
    tumbleAuto = 15
    banMove = 8

    # x,y cords
    cloud1x = 100
    cloud2x = 600
    tumweed1x = 700
    store1x = 700
    store2x = 1400
    cactusx = 450
    cooldown_sweat_y = 252
    activeSlotx1 = -50
    activeSlotx2 = -50
    bulletx = 330

    # ban 1
    banHP = 100
    banx1 = 1990
    banFPx1 = 300
    scopeWalk = 0
    ban1W = 200
    ban1H = 330

    # ban 2
    ban2HP = 100
    banx2 = 2490
    ban2FPx1 = 300
    scope2Walk = 0
    ban2W = 200
    ban2H = 330

    # ban 3
    ban3HP = 100
    banx3 = -1000
    ban3FPx1 = 300
    scope3Walk = 0
    ban3W = 200
    ban3H = 330


    # statements
    invincibility = False
    moveAbility = True
    banMoveAbility = True
    interactText = False
    buyText = False
    sitting = False
    standing = True
    walkingRight = False
    walkingLeft = False
    walkingBoth = False
    rolling = False
    moneyPick = False
    moneyPickText = False
    showMoney = True
    insufFundsText = False
    purchasedText = False
    lookingLeft = False
    lookingRight = True
    hotbarSlot1 = False
    hotbarSlot2 = False
    hotbarSlot3 = False
    hotbarSlot4 = False
    hotbarSlot5 = False
    hotbarSlot6 = False
    startGame = False
    reloadUI = False
    outAmmoUI = False
    revolverOutMag = False
    sniperOutMag = False
    revolverOutAmmo = False
    sniperOutAmmo = False
    dead = False
    scopeScreen = False
    ban1left = False
    ban2left = False
    ban3left = True
    ban1InScope = False
    ban2InScope = False
    ban3InScope = False
    insideShop = False
    ownSniperRifle = True
    catalog = False
    catalogPage1 = False
    catalogPage2 = False
    catalogPage3 = False
    playerIdle = True
    playerWalk = False
    playerHolster = False
    playerLegsIdle = True
    playerShoot = False
    playerDrink = False
    playerSniper = False
    playerGrab = False
    readyToFireRevolver = True
    playButtonHover = False
    playButtonClicked = False
    restartButtonHover = False
    restartButtonClicked = False
    mainMenuButtonHover = False
    mainMenuButtonClicked = False
    pause = False
    resumeButtonHover = False
    resumeButtonClicked = False
    settingsButtonHover = False
    settingsButtonClicked = False
    mainMenu2ButtonHover = False
    mainMenu2ButtonClicked = False
    confirmYesButtonHover = False
    confirmYesButtonClicked = False
    confirmNoButtonHover = False
    confirmNoButtonClicked = False
    confirmationBox = False
    settings = False
    settingsDoneButtonHover = False
    settingsDoneButtonClicked = False
    masterLeftButtonHover = False
    masterLeftButtonClicked = False
    masterRightButtonHover = False
    masterRightButtonClicked = False
    musicLeftButtonHover = False
    musicLeftButtonClicked = False
    musicRightButtonHover = False
    musicRightButtonClicked = False
    musicIconButtonClicked = False
    musicIconButtonHover = False
    masterIconButtonClicked = False
    masterIconButtonHover = False
    masterVolumeMuted = False
    musicVolumeMuted = False
    playerRoll1Right = False
    playerRoll2Right = False
    playerRoll3Right = False
    playerRoll1Left = False
    playerRoll2Left = False
    playerRoll3Left = False
    rollReady = True
    # MAKE SURE TO ALSO CHANGE VALUES IN RESETVALUES METHOD -------------------------------------------------------

# audio
if collapse:
    masterVolume = 1  # (0-1)
    musicVolume = 1  # (0-1)
    step = pygame.mixer.Sound('assets/sounds/step.wav')
    woodstep = pygame.mixer.Sound('assets/sounds/woodstep.wav')
    intro = pygame.mixer.Sound('assets/sounds/start_music.wav')
    button = pygame.mixer.Sound('assets/sounds/button.wav')
    griprevolver = pygame.mixer.Sound('assets/sounds/griprevolver.wav')
    shot = pygame.mixer.Sound('assets/sounds/shot.wav')
    empty = pygame.mixer.Sound('assets/sounds/empty.wav')
    reload = pygame.mixer.Sound('assets/sounds/reload.wav')
    revolverspin = pygame.mixer.Sound('assets/sounds/revolverspin.wav')
    death = pygame.mixer.Sound('assets/sounds/death.wav')
    playerhit = pygame.mixer.Sound('assets/sounds/playerhit.wav')
    banpain = pygame.mixer.Sound('assets/sounds/banpain.wav')
    snipershot = pygame.mixer.Sound('assets/sounds/snipershot.wav')
    heartbeat = pygame.mixer.Sound('assets/sounds/heartbeat.wav')
    breath = pygame.mixer.Sound('assets/sounds/breath.wav')
    intromusic = pygame.mixer.Sound('assets/sounds/menu_music.wav')
    door = pygame.mixer.Sound('assets/sounds/door.wav')
    openbook = pygame.mixer.Sound('assets/sounds/openbook.wav')
    turnpage = pygame.mixer.Sound('assets/sounds/turnpage.wav')
    cashregister = pygame.mixer.Sound('assets/sounds/cashregister.wav')
    error = pygame.mixer.Sound('assets/sounds/error.wav')
    music = pygame.mixer.Sound('assets/sounds/bg_music.wav')
    potion = pygame.mixer.Sound('assets/sounds/beer_drink.wav')
    sniper_reload = pygame.mixer.Sound('assets/sounds/sniper_reload.wav')
    combatroll = pygame.mixer.Sound('assets/sounds/combatroll.wav')

# sprites
if collapse:
    asset_cactus = pygame.image.load("assets/vegetation/cactus.png")
    asset_cloud1 = pygame.image.load("assets/sky/cloud1.png")
    asset_cloud2 = pygame.image.load("assets/sky/cloud2.png")
    asset_saloon = pygame.image.load("assets/buildings/cianfarano_saloon.png")
    asset_store = pygame.image.load("assets/buildings/solee_os_store.png")
    asset_hotbar = pygame.image.load("assets/UI/hotbar.png")
    asset_revolver = pygame.image.load("assets/UI/revolver_icon.png")
    asset_sniper = pygame.image.load("assets/UI/sniper_rifle_icon.png")
    asset_bandit1left = pygame.image.load("assets/npc/bandit1.png")
    asset_bandit2left = pygame.image.load("assets/npc/bandit2.png")
    asset_bandit3left = pygame.image.load("assets/npc/bandit3.png")
    asset_bandit1right = pygame.image.load("assets/npc/bandit1right.png")
    asset_bandit2right = pygame.image.load("assets/npc/bandit2right.png")
    asset_bandit3right = pygame.image.load("assets/npc/bandit3right.png")
    asset_bandit1left_dead = pygame.image.load("assets/npc/bandit1dead.png")
    asset_bandit2left_dead = pygame.image.load("assets/npc/bandit2dead.png")
    asset_bandit3left_dead = pygame.image.load("assets/npc/bandit3dead.png")
    asset_bandit1right_dead = pygame.image.load("assets/npc/bandit1rightdead.png")
    asset_bandit2right_dead = pygame.image.load("assets/npc/bandit2rightdead.png")
    asset_bandit3right_dead = pygame.image.load("assets/npc/bandit3rightdead.png")
    asset_holster_right = pygame.image.load("assets/player/holster_right.png")
    asset_bandana_right = pygame.image.load("assets/player/bandana_right.png")
    asset_bandana_left = pygame.image.load("assets/player/bandana_left.png")
    asset_revolver_vert_right = pygame.image.load("assets/weapons/revolver_vert_right.png")
    asset_revolver_vert_grip_left = pygame.image.load("assets/weapons/revolver_vert_grip_left.png")
    asset_revolver_right = pygame.image.load("assets/weapons/revolver_right.png")
    asset_revolver_left = pygame.image.load("assets/weapons/revolver_left.png")
    asset_sniper_left = pygame.image.load("assets/weapons/rolling_block_left.png")
    asset_sniper_right = pygame.image.load("assets/weapons/rolling_block_right.png")
    asset_muzzleflash_right = pygame.image.load("assets/weapons/muzzle_flash_bullet_right.png")
    asset_muzzleflash_left = pygame.image.load("assets/weapons/muzzle_flash_bullet_left.png")
    asset_sniperscope = pygame.image.load("assets/weapons/sniper_scope.png")
    asset_bandit1_fp = pygame.image.load("assets/npc/bandit1_fp.png")
    asset_bandit2_fp = pygame.image.load("assets/npc/bandit2_fp.png")
    asset_bandit3_fp = pygame.image.load("assets/npc/bandit3_fp.png")
    asset_scope_back_right = pygame.image.load("assets/weapons/scope_back_right.png")
    asset_scope_back_left = pygame.image.load("assets/weapons/scope_back_left.png")
    asset_sniper_rifle_right = pygame.image.load("assets/weapons/sniper_rifle_right.png")
    asset_sniper_rifle_left = pygame.image.load("assets/weapons/sniper_rifle_left.png")
    asset_shop_interior = pygame.image.load("assets/buildings/shop_interior.png")
    asset_text_1000_green = pygame.image.load("assets/UI/text_1000_green.png")
    asset_text_1000_red = pygame.image.load("assets/UI/text_1000_red.png")
    asset_text_100_green = pygame.image.load("assets/UI/text_100_green.png")
    asset_text_100_red = pygame.image.load("assets/UI/text_100_red.png")
    asset_text_50_green = pygame.image.load("assets/UI/text_50_green.png")
    asset_text_50_red = pygame.image.load("assets/UI/text_50_red.png")
    asset_text_owned = pygame.image.load("assets/UI/text_owned.png")
    asset_text_purchased = pygame.image.load("assets/UI/text_purchased.png")
    asset_text_insufficient = pygame.image.load("assets/UI/text_insufficient.png")
    asset_catalog_1 = pygame.image.load("assets/UI/catalog_pages_1.png")
    asset_catalog_2 = pygame.image.load("assets/UI/catalog_pages_2.png")
    asset_catalog_3 = pygame.image.load("assets/UI/catalog_pages_3.png")
    asset_hp_icon = pygame.image.load("assets/UI/player_hp.png")
    asset_money_icon = pygame.image.load("assets/UI/player_money.png")
    asset_kills_icon = pygame.image.load("assets/UI/player_kills.png")
    asset_ammo_icon = pygame.image.load("assets/UI/player_bullet.png")
    asset_journey_cover = pygame.image.load("assets/UI/Journeys_Wild_West_Cover.png")
    asset_player_right = pygame.image.load("assets/player/player_idle_right.png")
    asset_player_left = pygame.image.load("assets/player/player_idle_left.png")
    asset_player_arms_idle = pygame.image.load("assets/player/player_arms_idle.png")
    asset_player_legs_idle_right = pygame.image.load("assets/player/player_legs_idle_right.png")
    asset_player_legs_idle_left = pygame.image.load("assets/player/player_legs_idle_left.png")
    asset_player_arms_walk_right = pygame.image.load("assets/player/player_arms_walk_right.png")
    asset_player_arms_walk_left = pygame.image.load("assets/player/player_arms_walk_left.png")
    asset_player_legs_walk_right = pygame.image.load("assets/player/player_legs_walk_right.png")
    asset_player_legs_walk_left = pygame.image.load("assets/player/player_legs_walk_left.png")
    asset_player_holster_right = pygame.image.load("assets/player/player_arms_holster_right.png")
    asset_player_holster_left = pygame.image.load("assets/player/player_arms_holster_left.png")
    asset_player_holsterwalk_right = pygame.image.load("assets/player/player_arms_holsterwalk_right.png")
    asset_player_holsterwalk_left = pygame.image.load("assets/player/player_arms_holsterwalk_left.png")
    asset_player_shoot_right = pygame.image.load("assets/player/player_shoot_revolver_right.png")
    asset_player_shoot_left = pygame.image.load("assets/player/player_shoot_revolver_left.png")
    asset_player_drink_right = pygame.image.load("assets/player/player_drink_right.png")
    asset_player_drink_left = pygame.image.load("assets/player/player_drink_left.png")
    asset_player_roll1_right = pygame.image.load("assets/player/player_roll1_right.png")
    asset_player_roll2_right = pygame.image.load("assets/player/player_roll2_right.png")
    asset_player_roll3_right = pygame.image.load("assets/player/player_roll3_right.png")
    asset_player_roll1_left = pygame.image.load("assets/player/player_roll1_left.png")
    asset_player_roll2_left = pygame.image.load("assets/player/player_roll2_left.png")
    asset_player_roll3_left = pygame.image.load("assets/player/player_roll3_left.png")
    asset_player_cooldown_sweat_right = pygame.image.load("assets/player/cooldown_sweat_right.png")
    asset_player_cooldown_sweat_left = pygame.image.load("assets/player/cooldown_sweat_left.png")
    asset_hearty_beer_icon = pygame.image.load("assets/UI/hearty_beer_icon.png")
    asset_hearty_beer_right = pygame.image.load("assets/props/hearty_beer_right.png")
    asset_hearty_beer_left = pygame.image.load("assets/props/hearty_beer_left.png")
    asset_death_screen = pygame.image.load("assets/UI/death_screen.png")
    asset_sky_day = pygame.image.load("assets/sky/sky_day.png")
    asset_tumbleweed = pygame.image.load("assets/vegetation/tumbleweed.png")
    asset_ground_sand = pygame.image.load("assets/vegetation/ground_sand.png")
    asset_hotbar_select = pygame.image.load("assets/UI/hotbar_select.png")
    asset_main_menu = pygame.image.load("assets/UI/main_menu2.png")
    asset_button_normal = pygame.image.load("assets/UI/button_normal.png")
    asset_button_hover = pygame.image.load("assets/UI/button_hover.png")
    asset_button_clicked = pygame.image.load("assets/UI/button_clicked.png")
    asset_restart_button_normal = pygame.image.load("assets/UI/restart_button_normal.png")
    asset_restart_button_hover = pygame.image.load("assets/UI/restart_button_hover.png")
    asset_restart_button_clicked = pygame.image.load("assets/UI/restart_button_clicked.png")
    asset_main_menu_button_normal = pygame.image.load("assets/UI/main_menu_button_normal.png")
    asset_main_menu_button_hover = pygame.image.load("assets/UI/main_menu_button_hover.png")
    asset_main_menu_button_clicked = pygame.image.load("assets/UI/main_menu_button_clicked.png")
    asset_paused_overlay = pygame.image.load("assets/UI/paused.png")
    asset_paused_darken = pygame.image.load("assets/UI/pause_darken.png")
    asset_resume_button_normal = pygame.image.load("assets/UI/resume_button_normal.png")
    asset_resume_button_hover = pygame.image.load("assets/UI/resume_button_hover.png")
    asset_resume_button_clicked = pygame.image.load("assets/UI/resume_button_clicked.png")
    asset_settings_button_normal = pygame.image.load("assets/UI/settings_button_normal.png")
    asset_settings_button_hover = pygame.image.load("assets/UI/settings_button_hover.png")
    asset_settings_button_clicked = pygame.image.load("assets/UI/settings_button_clicked.png")
    asset_main_menu2_button_normal = pygame.image.load("assets/UI/main_menu2_button_normal.png")
    asset_main_menu2_button_hover = pygame.image.load("assets/UI/main_menu2_button_hover.png")
    asset_main_menu2_button_clicked = pygame.image.load("assets/UI/main_menu2_button_clicked.png")
    asset_confirm_yes_button_normal = pygame.image.load("assets/UI/confirm_yes_button_normal.png")
    asset_confirm_yes_button_hover = pygame.image.load("assets/UI/confirm_yes_button_hover.png")
    asset_confirm_yes_button_clicked = pygame.image.load("assets/UI/confirm_yes_button_clicked.png")
    asset_confirm_no_button_normal = pygame.image.load("assets/UI/confirm_no_button_normal.png")
    asset_confirm_no_button_hover = pygame.image.load("assets/UI/confirm_no_button_hover.png")
    asset_confirm_no_button_clicked = pygame.image.load("assets/UI/confirm_no_button_clicked.png")
    asset_confirmation_box = pygame.image.load("assets/UI/confirmation.png")
    asset_settings_menu = pygame.image.load("assets/UI/settings.png")
    asset_settings_done_button_normal = pygame.image.load("assets/UI/settings_done_button_normal.png")
    asset_settings_done_button_hover = pygame.image.load("assets/UI/settings_done_button_hover.png")
    asset_settings_done_button_clicked = pygame.image.load("assets/UI/settings_done_button_clicked.png")
    asset_master_left_button_normal = pygame.image.load("assets/UI/master_left_button_normal.png")
    asset_master_left_button_hover = pygame.image.load("assets/UI/master_left_button_hover.png")
    asset_master_left_button_clicked = pygame.image.load("assets/UI/master_left_button_clicked.png")
    asset_master_right_button_normal = pygame.image.load("assets/UI/master_right_button_normal.png")
    asset_master_right_button_hover = pygame.image.load("assets/UI/master_right_button_hover.png")
    asset_master_right_button_clicked = pygame.image.load("assets/UI/master_right_button_clicked.png")
    asset_music_left_button_normal = pygame.image.load("assets/UI/music_left_button_normal.png")
    asset_music_left_button_hover = pygame.image.load("assets/UI/music_left_button_hover.png")
    asset_music_left_button_clicked = pygame.image.load("assets/UI/music_left_button_clicked.png")
    asset_music_right_button_normal = pygame.image.load("assets/UI/music_right_button_normal.png")
    asset_music_right_button_hover = pygame.image.load("assets/UI/music_right_button_hover.png")
    asset_music_right_button_clicked = pygame.image.load("assets/UI/music_right_button_clicked.png")
    asset_music_icon_button_normal = pygame.image.load("assets/UI/music_icon_button_normal.png")
    asset_music_icon_button_hover = pygame.image.load("assets/UI/music_icon_button_hover.png")
    asset_music_icon_button_clicked = pygame.image.load("assets/UI/music_icon_button_clicked.png")
    asset_master_icon_button_normal = pygame.image.load("assets/UI/master_icon_button_normal.png")
    asset_master_icon_button_hover = pygame.image.load("assets/UI/master_icon_button_hover.png")
    asset_master_icon_button_clicked = pygame.image.load("assets/UI/master_icon_button_clicked.png")
    asset_volume_muted_strikethrough = pygame.image.load("assets/UI/muted_crossout.png")

# text
if collapse:
    font1 = pygame.font.Font("assets/fonts/BAHNSCHRIFT.TTF", 13)
    font2 = pygame.font.Font("assets/fonts/BAHNSCHRIFT.TTF", 18)
    font3 = pygame.font.SysFont("ebrima", 20, True)
    # syntax - (Name, Size, Bold, Italic)

    ban1Tag = font1.render("Bandit: Nicholas", True, (150,240,41))
    ban1HPTag = font1.render(("HP: " + str(banHP)), True, (255,255,255))
    ban2Tag = font1.render("Bandit: Darius", True, (150,240,41))
    ban2HPTag = font1.render(("HP: " + str(ban2HP)), True, (255,255,255))
    ban3Tag = font1.render("Bandit: Olyander", True, (150,240,41))
    ban3HPTag = font1.render(("HP: " + str(ban3HP)), True, (255,255,255))
    playerHP_text = font2.render((str(playerHP)), True, (255,255,255))
    playerScore_text = font2.render((str(score)), True, (255,255,255))
    playerMoney_text = font2.render((str(moneyCount)), True, (255,255,255))
    revolverAmmo_text = font2.render((str(revRoundsMag) + "/" + str(revRoundsTotal)), True, (255,255,255))
    sniperAmmo_text = font2.render((str(sniperRoundsMag) + "/" + str(sniperRoundsTotal)), True, (255,255,255))
    blankAmmo_text = font2.render("-", True, (255,255,255))
    reload_text = font1.render("RELOAD", True, (255,0,0))
    outAmmo_text = font1.render("Out of Ammo", True, (255,0,0))
    interact_text = font1.render("INTERACT", True, (255,255,255))
    buy_text = font1.render("BUY", True, (255,255,255))
    potionCount_text = font1.render((str(hpPotionCount)), True, (255,255,255))
    clickPlay_text = font1.render("Click Here to PLAY", True, (255,255,255))
    deathScore_text = font2.render(("Score: " + str(score)), True, (255,255,255))
    shopWarning_text = font1.render("\"Take your hand off the gun, son..\"", True, (0, 0, 0))
    version_text = font1.render(("v " + version), True, (255, 255, 255))
    masterVolume_text = font1.render((str(masterVolume)), True, (255, 255, 255))
    musicVolume_text = font1.render((str(musicVolume)), True, (255, 255, 255))
    playerHighscore_text = font1.render("Highscore: " + (str(highscore)), True, (255, 255, 255))
    # syntax - (Message, AntiAliasing, Color, Background=None)

# Name list
list_names = ['Bob', 'Richard', 'Aaron', 'Arthur', 'Henry', 'Frank', 'Edward', 'Albert','James', 'John', 'Walter',
              'Roy', 'Louis', 'Carl', 'Paul', 'Pedro', 'Samuel', 'Raymond', 'Howard', 'Oscar', 'Leo', 'Jack', 'Lee']


# bandit methods
def getBanditRespawn():
    x = random.randint(-1200, 1200)
    if x <= 700 and x >= -100:
        x += 900
    return x


# Bandit class
class Bandit:
    instances = []
    # dictionary for types of bandits
    TYPE_MAP = {
                1: (asset_bandit1left, asset_bandit1right, asset_bandit1left_dead, asset_bandit1right_dead),
                2: (asset_bandit2left, asset_bandit2right, asset_bandit2left_dead, asset_bandit2right_dead),
                3: (asset_bandit3left, asset_bandit3right, asset_bandit3left_dead, asset_bandit3right_dead)
                }

    # constructor
    def __init__(self):
        self.__class__.instances.append(self)
        self.name = random.choice(list_names)  # assign random name
        self.bandit_left_img, self.bandit_right_img, self.bandit_leftdead_img, self.bandit_rightdead_img = \
            self.TYPE_MAP[random.randint(1,3)]  # assign random type
        self.level = 1  # assign level
        self.hp = 100  # assign starting hp
        self.x_location = getBanditRespawn()  # assign x-location
        self.bandit_left = None  # is the bandit on the left side of player
        self.nameTag = font1.render("Bandit: " + self.name, True, (150, 240, 41))
        self.hpTag = font1.render(("HP: " + str(self.hp)), True, (255,255,255))

    # class methods

    # move method
    def move(self, vel=8):
        # bandit is right of player
        if self.x_location >= 280:
            self.x_location -= vel
            self.bandit_left = False
        # bandit is left of player
        elif self.x_location <= 220:
            self.x_location += vel
            self.bandit_left = True

    def draw(self):
        if self.hp > 0:
            screen.blit(self.nameTag, (self.x_location-30,232))
            screen.blit(self.hpTag, (self.x_location-6,246))
            if self.bandit_left == False:
                screen.blit(self.bandit_left_img, (self.x_location-39.5, 262))
            elif self.bandit_left == True:
                screen.blit(self.bandit_right_img, (self.x_location-7, 262))
        if insideShop == False:
            if self.hp <= 0:
                if self.bandit_left == False:
                    screen.blit(self.bandit_leftdead_img, (self.x_location-23, 377))
                elif self.bandit_left == True:
                    screen.blit(self.bandit_rightdead_img, (self.x_location-123, 377))

    def respawn(self):
        self.x_location = getBanditRespawn()

    # getters
    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_hp(self):
        return self.hp

    def get_x_location(self):
        return self.x_location




def worldLeft(multiplier=1):
    global cloud1x, cloud2x, standing, cactusx, store1x, store2x, tumweed1x, banx1, banx2, banx3, \
        playerIdle, playerWalk, playerLegsIdle, playerShoot, playerHolster, playerSniper

    if standing == True:
        playerIdle = False
        playerLegsIdle = False
        if playerShoot == True:
            playerHolster = True
            playerShoot = False
        if lookingRight == True:
            playerWalk = True
        if lookingLeft == True:
            playerWalk = True

    cloud1x += cloudMove*multiplier
    if cloud1x + 85 >= 800:
        cloud1x = -100
    cloud2x += cloudMove*multiplier
    if cloud2x + 85 >= 800:
        cloud2x = -100
    cactusx += speedMove*multiplier
    store1x += speedMove*multiplier
    store2x += speedMove*multiplier
    tumweed1x += speedMove*multiplier
    banx1 += speedMove*multiplier
    banx2 += speedMove*multiplier
    banx3 += speedMove*multiplier

    # move bandits
    for instance in Bandit.instances:
        instance.x_location += speedMove*multiplier


def worldRight(multiplier=1):
    global cloud1x, cloud2x, standing, cactusx, store1x, store2x, tumweed1x, banx1, banx2, banx3, \
        playerIdle, playerWalk, playerLegsIdle, playerShoot, playerHolster, playerSniper

    if standing == True:
        playerIdle = False
        playerLegsIdle = False
        if playerShoot == True:
            playerHolster = True
            playerShoot = False
        if lookingRight == True:
            playerWalk = True
        if lookingLeft == True:
            playerWalk = True
        if playerShoot == True:
            playerHolster = True

    cloud1x -= cloudMove*multiplier
    if cloud1x + 85 <= -100:
        cloud1x = 800
    cloud2x -= cloudMove*multiplier
    if cloud2x + 85 <= -100:
        cloud2x = 1100
    cactusx -= speedMove*multiplier
    store1x -= speedMove*multiplier
    store2x -= speedMove*multiplier
    tumweed1x -= speedMove*multiplier
    banx1 -= speedMove*multiplier
    banx2 -= speedMove*multiplier
    banx3 -= speedMove*multiplier

    # move bandits
    for instance in Bandit.instances:
        instance.x_location -= speedMove*multiplier


def walkRight():
    global moveAbility, hotbarSlot2, moneyPickText, interactText, insufFundsText, purchasedText, lookingRight,\
        lookingLeft, hotbarSlot1, store1x, store2x, scopeScreen, insideShop, playerShoot, playerHolster,\
        banMoveAbility, cactusx

    if moveAbility == True and pause == False and rolling == False:
        if scopeScreen == False:
            worldRight()
            disableText()
            lookingRight = True
            lookingLeft = False
            if hotbarSlot1 == True:
                playerHolster = True
            if insideShop == False:
                step.stop()
                step.play()
            elif insideShop == True:
                woodstep.stop()
                woodstep.play()
    # Exit Store
    if insideShop == True:
        if (store1x - 200) >= 0:
            insideShop = False
            store1x = 50
            store2x = 750
            cactusx = -200
            banMoveAbility = True
            door.stop()
            door.play()
    # Shop Wall Collision
    if insideShop == True:
        if (store1x + 700) <= 0:
            moveAbility = False


def walkLeft():
    global moveAbility, hotbarSlot2, moneyPickText, interactText, insufFundsText, purchasedText, lookingRight,\
        lookingLeft, hotbarSlot1, store1x, store2x, scopeScreen, insideShop, playerShoot, playerHolster,\
        banMoveAbility, cactusx

    if moveAbility == True and pause == False and rolling == False:
        if scopeScreen == False:
            worldLeft()
            disableText()
            lookingRight = False
            lookingLeft = True
            if hotbarSlot1 == True:
                playerHolster = True
            if insideShop == False:
                step.stop()
                step.play()
            elif insideShop == True:
                woodstep.stop()
                woodstep.play()
    # Exit Store
    if insideShop == True:
        if (store1x - 200) >= 0:
            insideShop = False
            store1x = 50
            store2x = 750
            cactusx = -200
            banMoveAbility = True
            door.stop()
            door.play()
    # Shop Wall Collision
    if insideShop == True:
        if (store1x + 700) <= 0:
            moveAbility = True
            walkLeft()


def checkWalkBoth():
    global walkingBoth
    # If trying to walk both left and right
    if walkingLeft and walkingRight:
        walkingBoth = True
    else:
        walkingBoth = False


def roll():
    global moveAbility, hotbarSlot2, moneyPickText, interactText, insufFundsText, purchasedText, lookingRight,\
        lookingLeft, hotbarSlot1, store1x, store2x, scopeScreen, insideShop, playerShoot, playerHolster, playerSniper
    if lookingRight:
        if moveAbility == True and pause == False:
            if rollReady == True:
                disableText()
                # start roll
                rollStart_timer.start()
                lookingRight = True
                lookingLeft = False
                if hotbarSlot1 == True:
                    playerHolster = True
                if insideShop == False:
                    step.stop()
                    step.play()
                elif insideShop == True:
                    woodstep.stop()
                    woodstep.play()
    elif lookingLeft:
        if moveAbility == True and pause == False:
            if rollReady == True:
                disableText()
                # start roll
                rollStart_timer.start()
                lookingRight = False
                lookingLeft = True
                if hotbarSlot1 == True:
                    playerHolster = True
                if insideShop == False:
                    step.stop()
                    step.play()
                elif insideShop == True:
                    woodstep.stop()
                    woodstep.play()


def disableText():
    global moneyPickText, interactText, insufFundsText, purchasedText
    moneyPickText = False
    insufFundsText = False
    purchasedText = False


def fire():
    global score, moneyCount, startGame, moveAbility, hotbarSlot2, hotbarSlot6, dead, bulletx, hotbarSlot1, \
        lookingLeft, lookingRight, revRoundsMag, reloadUI, outAmmoUI, interactText, banHP, banx2, ban2HP, scopeScreen,\
        ban3HP, banx3, ban3FPx1, scope3Walk, playerShoot, playerHolster, revRoundsTotal,sniperRoundsMag,\
        sniperRoundsTotal, playerSniper, pause

    if pause == False and dead == False:
        # Revolver
        if hotbarSlot1 == True:
            playerShoot = True
            playerHolster = False
            interactText = False
            if revRoundsMag > 0:
                if lookingRight == True:
                    bulletx = 330
                if lookingLeft == True:
                    bulletx = 330
                shot.stop()
                shot.play()
                revRoundsMag -= 1
                stopRevolverReload()

            elif revRoundsMag == 0:
                empty.stop()
                empty.play()

            if revRoundsMag > 0:
                if lookingRight:
                    if banx1 <= 600 and banx1 >= 250:
                        if banHP > -10:
                            banHP -= 20
                            if banHP == 0:
                                banpain.play()
                                score += 1
                                giveMoney()
                    if banx2 <= 600 and banx2 >= 250:
                        if ban2HP > -10:
                            ban2HP -= 20
                            if ban2HP == 0:
                                banpain.play()
                                score += 1
                                giveMoney()
                    if banx3 <= 600 and banx3 >= 250:
                        if ban3HP > -10:
                            ban3HP -= 20
                            if ban3HP == 0:
                                banpain.play()
                                score += 1
                                giveMoney()
                if lookingLeft:
                    if banx1 >= 0 and banx1 <= 250:
                        if banHP > -10:
                            banHP -= 20
                            if banHP == 0:
                                banpain.play()
                                score += 1
                                giveMoney()
                    if banx2 >= 0 and banx2 <= 250:
                        if ban2HP > -10:
                            ban2HP -= 20
                            if ban2HP == 0:
                                banpain.play()
                                score += 1
                                giveMoney()
                    if banx3 >= 0 and banx3 <= 250:
                        if ban3HP > -10:
                            ban3HP -= 20
                            if ban3HP == 0:
                                banpain.play()
                                score += 1
                                giveMoney()

        # sniper rifle
        if hotbarSlot2 == True and scopeScreen == True:
            interactText = False
            if sniperRoundsMag > 0:
                snipershot.stop()
                snipershot.play()
                scopeScreen = False
                sniperRoundsMag -= 1
                sniper_reload.stop()
            else:
                empty.stop()
                empty.play()
            if lookingRight:
                if banx1 <= 700 and banx1 >= 250:
                    if banHP > -10:
                        banHP -= 100
                        if banHP == 0:
                            banpain.play()
                            score += 1
                            giveMoney()
                if banx2 <= 700 and banx2 >= 250:
                    if ban2HP > -10:
                        ban2HP -= 100
                        if ban2HP == 0:
                            banpain.play()
                            score += 1
                if banx3 <= 700 and banx3 >= 250:
                    if ban3HP > -10:
                        ban3HP -= 100
                        if ban3HP == 0:
                            banpain.play()
                            score += 1
                            giveMoney()
            if lookingLeft:
                if banx1 >= -100 and banx1 <= 250:
                    if banHP > -10:
                        banHP -= 100
                        if banHP == 0:
                            banpain.play()
                            score += 1
                            giveMoney()
                if banx2 >= -100 and banx2 <= 250:
                    if ban2HP > -10:
                        ban2HP -= 100
                        if ban2HP == 0:
                            banpain.play()
                            score += 1
                            giveMoney()
                if banx3 >= -100 and banx3 <= 250:
                    if ban3HP > -10:
                        ban3HP -= 100
                        if ban3HP == 0:
                            banpain.play()
                            score += 1
                            giveMoney()


def hpPotion():
    global playerHP, hpPotionCount, playerDrink
    for i in range(0, 1):
        time.sleep(0.09)
        for j in range(0, 50):
            if playerHP < 100:
                playerHP += 1
            else:
                j = 50
    hpPotionCount -= 1
    playerDrink = True
    potion.stop()
    potion.play()


def giveMoney():
    global moneyCount
    x = random.randint(30, 100)
    moneyCount += x


def stopSounds():
    intro.stop()
    reload.stop()
    sniper_reload.stop()
    heartbeat.stop()
    breath.stop()
    intromusic.stop()
    music.stop()
    snipershot.stop()
    shot.stop()
    death.stop()
    playerhit.stop()
    combatroll.stop()


def mainMenu():
    global startGame, tumbleAuto, playButtonHover, moveAbility, banMoveAbility, mouse_posx, mouse_posy, \
        settingsButtonHover
    # Background
    screen.blit(asset_main_menu, (0, 0))
    # Version Number
    screen.blit(version_text, (6, 580))
    # Play Button ---------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 365) and (420 <= mouse_posy <= 465) and settings == False and playButtonClicked == False:
        screen.blit(asset_button_hover, (0, 0))
        playButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 365) and (420 <= mouse_posy <= 465) and playButtonClicked == True:
        screen.blit(asset_button_clicked, (0, 0))
        playButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_button_normal, (0, 0))
        playButtonHover = False
    # Settings Button -------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 367) and (494 <= mouse_posy <= 540) and settingsButtonClicked == False \
            and settings == False:
        screen.blit(asset_settings_button_hover, (0, 170))
        settingsButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 367) and (494 <= mouse_posy <= 540) and settingsButtonClicked == True:
        screen.blit(asset_settings_button_clicked, (0, 170))
        settingsButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_settings_button_normal, (0, 170))
        settingsButtonHover = False
    # In Settings Menu
    if settings == True:
        showSettings()
    moveAbility = False
    banMoveAbility = False
    music_timer.stop()


def pauseGame():
    global resumeButtonHover, settingsButtonHover, mainMenu2ButtonHover, confirmYesButtonHover, \
        confirmNoButtonHover, settingsDoneButtonHover, masterLeftButtonHover, masterRightButtonHover, \
        musicLeftButtonHover, musicRightButtonHover

    # Pause Screen -------------------------------------------------------------------------------
    screen.blit(asset_paused_overlay, (0, 0))
    # Resume Button ------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 367) and (257 <= mouse_posy <= 302) and resumeButtonClicked == False \
            and confirmationBox == False:
        screen.blit(asset_resume_button_hover, (0, 0))
        resumeButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 367) and (257 <= mouse_posy <= 302) and resumeButtonClicked == True:
        screen.blit(asset_resume_button_clicked, (0, 0))
        resumeButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_resume_button_normal, (0, 0))
        resumeButtonHover = False

    # Settings Button -------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 367) and (324 <= mouse_posy <= 370) and settingsButtonClicked == False \
            and confirmationBox == False:
        screen.blit(asset_settings_button_hover, (0, 0))
        settingsButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 367) and (324 <= mouse_posy <= 370) and settingsButtonClicked == True:
        screen.blit(asset_settings_button_clicked, (0, 0))
        settingsButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_settings_button_normal, (0, 0))
        settingsButtonHover = False

    # Main Menu Button ------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 367) and (393 <= mouse_posy <= 438) and mainMenu2ButtonClicked == False \
            and confirmationBox == False:
        screen.blit(asset_main_menu2_button_hover, (0, 0))
        mainMenu2ButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 367) and (393 <= mouse_posy <= 438) and mainMenu2ButtonClicked == True:
        screen.blit(asset_main_menu2_button_clicked, (0, 0))
        mainMenu2ButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_main_menu2_button_normal, (0, 0))
        mainMenu2ButtonHover = False

    # Confirmation Screen --------------------------------------------------------------------------------
    if confirmationBox == True:
        screen.blit(asset_confirmation_box, (0, 0))
        # Yes --------------------------------------------------------------------------------------------
        # Hover Button
        if (189 <= mouse_posx <= 267) and (292 <= mouse_posy <= 329) and confirmYesButtonClicked == False:
            screen.blit(asset_confirm_yes_button_hover, (0, 0))
            confirmYesButtonHover = True
        # Click Button
        elif (189 <= mouse_posx <= 267) and (292 <= mouse_posy <= 329) and confirmYesButtonClicked == True:
            screen.blit(asset_confirm_yes_button_clicked, (0, 0))
            confirmYesButtonHover = False
        # Normal Button
        else:
            screen.blit(asset_confirm_yes_button_normal, (0, 0))
            confirmYesButtonHover = False
        # No --------------------------------------------------------------------------------------------
        # Hover Button
        if (333 <= mouse_posx <= 412) and (292 <= mouse_posy <= 329) and confirmNoButtonClicked == False:
            screen.blit(asset_confirm_no_button_hover, (0, 0))
            confirmNoButtonHover = True
        # Click Button
        elif (333 <= mouse_posx <= 412) and (292 <= mouse_posy <= 329) and confirmNoButtonClicked == True:
            screen.blit(asset_confirm_no_button_clicked, (0, 0))
            confirmNoButtonHover = False
        # Normal Button
        else:
            screen.blit(asset_confirm_no_button_normal, (0, 0))
            confirmNoButtonHover = False
    # Settings Menu ----------------------------------------------------------------------------------
    if settings == True:
        showSettings()


def showSettings():
    global resumeButtonHover, settingsButtonHover, mainMenu2ButtonHover, confirmYesButtonHover, \
        confirmNoButtonHover, settingsDoneButtonHover, masterLeftButtonHover, masterRightButtonHover, \
        musicLeftButtonHover, musicRightButtonHover, masterIconButtonClicked, musicIconButtonClicked, \
        masterIconButtonHover, musicIconButtonHover

    masterVolumePercent = round(masterVolume * 100)
    musicVolumePercent = round(musicVolume * 100)
    masterVolume_text = font3.render((str(masterVolumePercent) + "%"), True, (255, 255, 255))
    musicVolume_text = font3.render((str(musicVolumePercent) + "%"), True, (255, 255, 255))
    masterVolumeBack_text = font3.render((str(masterVolumePercent) + "%"), True, (18, 15, 23))
    musicVolumeBack_text = font3.render((str(musicVolumePercent) + "%"), True, (18, 15, 23))

    screen.blit(asset_settings_menu, (0, 0))
    screen.blit(masterVolumeBack_text, (406, 178))
    screen.blit(masterVolume_text, (408, 177))
    screen.blit(musicVolumeBack_text, (394, 230))
    screen.blit(musicVolume_text, (396, 229))
    # Done Button ---------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 367) and (433 <= mouse_posy <= 471) and settingsDoneButtonClicked == False:
        screen.blit(asset_settings_done_button_hover, (0, 0))
        settingsDoneButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 367) and (433 <= mouse_posy <= 471) and settingsDoneButtonClicked == True:
        screen.blit(asset_settings_done_button_clicked, (0, 0))
        settingsDoneButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_settings_done_button_normal, (0, 0))
        settingsDoneButtonHover = False
    # Master Left -----------------------------------------------------------------------------------
    # Hover Button
    if (112 <= mouse_posx <= 140) and (174 <= mouse_posy <= 204) and masterLeftButtonClicked == False and \
            masterVolumeMuted == False:
        screen.blit(asset_master_left_button_hover, (0, 0))
        masterLeftButtonHover = True
    # Click Button
    elif (112 <= mouse_posx <= 140) and (174 <= mouse_posy <= 204) and masterLeftButtonClicked == True and \
            masterVolumeMuted == False:
        screen.blit(asset_master_left_button_clicked, (0, 0))
        masterLeftButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_master_left_button_normal, (0, 0))
        masterLeftButtonHover = False
    # Master Right -----------------------------------------------------------------------------------
    # Hover Button
    if (474 <= mouse_posx <= 504) and (174 <= mouse_posy <= 204) and masterRightButtonClicked == False and \
            masterVolumeMuted == False:
        screen.blit(asset_master_right_button_hover, (0, 0))
        masterRightButtonHover = True
    # Click Button
    elif (474 <= mouse_posx <= 504) and (174 <= mouse_posy <= 204) and masterRightButtonClicked == True and \
            masterVolumeMuted == False:
        screen.blit(asset_master_right_button_clicked, (0, 0))
        masterRightButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_master_right_button_normal, (0, 0))
        masterRightButtonHover = False
    # Master Icon -----------------------------------------------------------------------------------
    # Hover Button
    if (155 <= mouse_posx <= 180) and (172 <= mouse_posy <= 206) and masterIconButtonClicked == False:
        screen.blit(asset_master_icon_button_hover, (0, 0))
        masterIconButtonHover = True
    # Click Button
    elif (155 <= mouse_posx <= 180) and (172 <= mouse_posy <= 206) and masterIconButtonClicked == True:
        screen.blit(asset_master_icon_button_clicked, (0, 0))
        masterIconButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_master_icon_button_normal, (0, 0))
        masterIconButtonHover = False
    # Music Left -----------------------------------------------------------------------------------
    # Hover Button
    if (112 <= mouse_posx <= 140) and (226 <= mouse_posy <= 257) and musicLeftButtonClicked == False and \
            musicVolumeMuted == False:
        screen.blit(asset_music_left_button_hover, (0, 0))
        musicLeftButtonHover = True
    # Click Button
    elif (112 <= mouse_posx <= 140) and (226 <= mouse_posy <= 257) and musicLeftButtonClicked == True and \
            musicVolumeMuted == False:
        screen.blit(asset_music_left_button_clicked, (0, 0))
        musicLeftButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_music_left_button_normal, (0, 0))
        musicLeftButtonHover = False
    # Music Right -----------------------------------------------------------------------------------
    # Hover Button
    if (474 <= mouse_posx <= 504) and (226 <= mouse_posy <= 257) and musicRightButtonClicked == False and \
            musicVolumeMuted == False:
        screen.blit(asset_music_right_button_hover, (0, 0))
        musicRightButtonHover = True
    # Click Button
    elif (474 <= mouse_posx <= 504) and (226 <= mouse_posy <= 257) and musicRightButtonClicked == True and \
            musicVolumeMuted == False:
        screen.blit(asset_music_right_button_clicked, (0, 0))
        musicRightButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_music_right_button_normal, (0, 0))
        musicRightButtonHover = False
    # Music Icon -----------------------------------------------------------------------------------
    # Hover Button
    if (155 <= mouse_posx <= 181) and (230 <= mouse_posy <= 258) and musicIconButtonClicked == False:
        screen.blit(asset_music_icon_button_hover, (0, 0))
        musicIconButtonHover = True
    # Click Button
    elif (155 <= mouse_posx <= 181) and (230 <= mouse_posy <= 258) and musicIconButtonClicked == True:
        screen.blit(asset_music_icon_button_clicked, (0, 0))
        musicIconButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_music_icon_button_normal, (0, 0))
        musicIconButtonHover = False
    # Master Volume Muted Strike --------------------------------------------------------------------
    if masterVolumeMuted == True:
        screen.blit(asset_volume_muted_strikethrough, (2, -53))
    # Music Volume Muted Strike ---------------------------------------------------------------------
    if musicVolumeMuted == True:
        screen.blit(asset_volume_muted_strikethrough, (0, 0))

    # volume refresh
    step.set_volume(masterVolume)
    woodstep.set_volume(masterVolume)
    button.set_volume(masterVolume)
    griprevolver.set_volume(masterVolume)
    shot.set_volume(masterVolume)
    empty.set_volume(masterVolume)
    reload.set_volume(masterVolume)
    revolverspin.set_volume(masterVolume)
    death.set_volume(masterVolume)
    playerhit.set_volume(masterVolume)
    banpain.set_volume(masterVolume)
    snipershot.set_volume(masterVolume)
    heartbeat.set_volume(masterVolume)
    breath.set_volume(masterVolume)
    door.set_volume(masterVolume)
    openbook.set_volume(masterVolume)
    turnpage.set_volume(masterVolume)
    cashregister.set_volume(masterVolume)
    error.set_volume(masterVolume)
    potion.set_volume(masterVolume)
    sniper_reload.set_volume(masterVolume)
    combatroll.set_volume(masterVolume)
    intromusic.set_volume(musicVolume * masterVolume)
    intro.set_volume(musicVolume * masterVolume)
    music.set_volume(musicVolume * masterVolume)


def showHUD():
    # hp
    screen.blit(asset_hp_icon, (11, 507))
    screen.blit(playerHP_text, (41, 505))
    # kills
    screen.blit(asset_kills_icon, (11, 530))
    screen.blit(playerScore_text, (41, 528))
    # money
    screen.blit(asset_money_icon, (11, 552))
    screen.blit(playerMoney_text, (41, 550))
    # ammo
    screen.blit(asset_ammo_icon, (11, 573))
    if hotbarSlot1 == True:
        screen.blit(revolverAmmo_text, (41, 571))
    elif hotbarSlot2 == True:
        screen.blit(sniperAmmo_text, (41, 571))
    else:
        screen.blit(blankAmmo_text, (42, 569))
    # popup text
    if purchasedText == True:
        screen.blit(asset_text_purchased, (201, 60))
    if insufFundsText == True:
        screen.blit(asset_text_insufficient, (201, 60))
    # interact text
    if interactText == True and rolling == False and scopeScreen == False:
        if sitting == True:
            screen.blit(interact_text, (221, 265))
        else:
            screen.blit(interact_text, (221, 235))
    # buy text
    if buyText == True:
        screen.blit(buy_text, (137, 255))

    # ammo text
    if standing == True:
        if reloadUI == True:
            screen.blit(reload_text, (226, 233))
        if outAmmoUI == True:
            screen.blit(outAmmo_text, (215, 233))
    # hotbar
    if startGame == True and scopeScreen == False:
        screen.blit(asset_hotbar, (300 - 153.5, 560 - 28.5))
        screen.blit(asset_revolver, (300 - 153.5, 560 - 28.5))
        if ownSniperRifle == True:
            screen.blit(asset_sniper, (300 - 153.5, 560 - 28.5))
        if hpPotionCount > 0:
            screen.blit(asset_hearty_beer_icon, (500 - 153.5, 562 - 28.5))
            screen.blit(potionCount_text, (403, 537))
        screen.blit(asset_hotbar_select, (activeSlotx1 - 3, 565 - 33))


def interactCheck():
    global interactText

    # Check if in front of store
    if store1x <= 100 and store1x >= 0:
        if playerShoot == False and scopeScreen == False and insideShop == False:
            interactText = True
    # Open Catalog
    elif store1x + 420 <= 100 and store1x + 420 >= 0:
        if playerHolster == False and playerShoot == False and insideShop == True and catalog == False \
                and playerSniper == False:
            interactText = True
    # Holding sniper rifle
    elif playerSniper == True and sniperRoundsMag > 0 and insideShop == False:
        interactText = True
    else:
        interactText = False


def playerHit(damage):
    global playerHP, invincibility

    if playerHP > 0 and invincibility == False:
        playerHP -= damage
        playerHitSound_timer.start()


def playerDead():
    global dead, moveAbility, startGame
    dead = True
    # death screen
    screen.blit(asset_death_screen, (300 - 300, 300 - 300))
    screen.blit(deathScore_text, (278, 250))
    screen.blit(playerHighscore_text, (264, 270))

    moveAbility = False
    startGame = False
    stopAllTimers(timerTuple)
    stopSounds()
    if playerHP == 0:
        death.stop()
        death.play()


def resetValues():
    global playerHP, moneyCount, revRoundsMag, revRoundsTotal, revolverFireRate, sniperRoundsMag, sniperRoundsTotal, \
        hpPotionCount, score, cloud1x, cloud2x, tumweed1x, store1x, store2x, cactusx, activeSlotx1, activeSlotx2, \
        bulletx, banHP, banx1, banFPx1, scopeWalk, ban2HP, banx2, ban2FPx1, scope2Walk, ban3HP, banx3, ban3FPx1, \
        scope3Walk, startGame, dead, moveAbility, banMoveAbility, interactText, buyText, sitting, standing, \
        insufFundsText, purchasedText, lookingLeft, lookingRight, hotbarSlot1, hotbarSlot2, hotbarSlot3, hotbarSlot4, \
        hotbarSlot5, hotbarSlot6, reloadUI, outAmmoUI, scopeScreen,ban1InScope,ban2InScope,ban3InScope,insideShop, \
        ownSniperRifle, catalog, catalogPage1, catalogPage2, catalogPage3, playerIdle, playerWalk, playerHolster, \
        playerLegsIdle, playerShoot, playerDrink, playerSniper, playerGrab, playButtonHover, playButtonClicked, \
        readyToFireRevolver, restartButtonHover, restartButtonClicked, mainMenuButtonHover, mainMenuButtonClicked, \
        resumeButtonHover, resumeButtonClicked, settingsButtonHover, settingsButtonClicked, mainMenu2ButtonHover, \
        mainMenu2ButtonClicked, confirmYesButtonHover, confirmYesButtonClicked, confirmNoButtonHover, \
        confirmNoButtonClicked, confirmationBox, settings, settingsDoneButtonHover, settingsDoneButtonClicked, \
        masterLeftButtonHover, masterLeftButtonClicked, masterRightButtonHover, masterRightButtonClicked, \
        musicLeftButtonHover, musicLeftButtonClicked, musicRightButtonHover, musicRightButtonClicked, \
        ban1H, ban1W, ban2H, ban2W, ban3H, ban3W, playerRoll1Right, playerRoll2Right, playerRoll3Right,\
        playerRoll1Left, playerRoll2Left, playerRoll3Left, rolling, rollReady, cooldown_sweat_y, walkingLeft, \
        walkingRight, walkingBoth, musicIconButtonClicked, musicIconButtonHover, masterIconButtonClicked, \
        masterIconButtonHover, revolverOutAmmo, sniperOutAmmo, revolverOutMag, sniperOutMag

    # player vals
    playerHP = 100
    moneyCount = 0
    revRoundsMag = 6
    revRoundsTotal = 24
    revolverFireRate = 120
    sniperRoundsMag = 1
    sniperRoundsTotal = 3
    hpPotionCount = 0
    score = 0

    # x-pos
    cloud1x = 100
    cloud2x = 600
    tumweed1x = 700
    store1x = 700
    store2x = 1400
    cactusx = 450
    cooldown_sweat_y = 252
    activeSlotx1 = -50
    activeSlotx2 = -50
    bulletx = 330

    # ban 1
    banHP = 100
    banx1 = 1990
    banFPx1 = 300
    scopeWalk = 0
    ban1W = 200
    ban1H = 330
    # ban 2
    ban2HP = 100
    banx2 = 2490
    ban2FPx1 = 300
    scope2Walk = 0
    ban2W = 200
    ban2H = 330
    # ban 3
    ban3HP = 100
    banx3 = -1000
    ban3FPx1 = 300
    scope3Walk = 0
    ban3W = 200
    ban3H = 330

    invincibility = False
    moveAbility = True
    banMoveAbility = True
    interactText = False
    buyText = False
    sitting = False
    standing = True
    walkingRight = False
    walkingLeft = False
    walkingBoth = False
    rolling = False
    insufFundsText = False
    purchasedText = False
    lookingLeft = False
    lookingRight = True
    hotbarSlot1 = False
    hotbarSlot2 = False
    hotbarSlot3 = False
    hotbarSlot4 = False
    hotbarSlot5 = False
    hotbarSlot6 = False
    reloadUI = False
    outAmmoUI = False
    revolverOutMag = False
    sniperOutMag = False
    revolverOutAmmo = False
    sniperOutAmmo = False
    scopeScreen = False
    ban1InScope = False
    ban2InScope = False
    ban3InScope = False
    insideShop = False
    ownSniperRifle = True
    catalog = False
    catalogPage1 = False
    catalogPage2 = False
    catalogPage3 = False
    playerIdle = True
    playerWalk = False
    playerHolster = False
    playerLegsIdle = True
    playerShoot = False
    playerDrink = False
    playerSniper = False
    playerGrab = False
    readyToFireRevolver = True
    playButtonHover = False
    playButtonClicked = False
    restartButtonHover = False
    mainMenuButtonHover = False
    mainMenuButtonClicked = False
    pause = False
    resumeButtonHover = False
    resumeButtonClicked = False
    settingsButtonHover = False
    settingsButtonClicked = False
    mainMenu2ButtonHover = False
    mainMenu2ButtonClicked = False
    confirmYesButtonHover = False
    confirmYesButtonClicked = False
    confirmNoButtonHover = False
    confirmNoButtonClicked = False
    confirmationBox = False
    settings = False
    settingsDoneButtonHover = False
    settingsDoneButtonClicked = False
    masterLeftButtonHover = False
    masterLeftButtonClicked = False
    masterRightButtonHover = False
    masterRightButtonClicked = False
    musicLeftButtonHover = False
    musicLeftButtonClicked = False
    musicRightButtonHover = False
    musicRightButtonClicked = False
    musicIconButtonClicked = False
    musicIconButtonHover = False
    masterIconButtonClicked = False
    masterIconButtonHover = False
    playerRoll1Right = False
    playerRoll2Right = False
    playerRoll3Right = False
    playerRoll1Left = False
    playerRoll2Left = False
    playerRoll3Left = False
    rollReady = True


def stopAllTimers(tup):
    for timer in tuple(tup):
        timer.stop()


def masterVolumeDown():
    global masterVolume
    if masterVolume > 0.1:
        masterVolume = masterVolume - 0.1


def masterVolumeUp():
    global masterVolume
    if masterVolume < 1:
        masterVolume = masterVolume + 0.1


def masterVolumeMute(previous_volume):
    global masterVolume, masterVolumeMuted
    if masterVolumeMuted == True:
        masterVolume = previous_volume
        masterVolumeMuted = False
    elif masterVolumeMuted == False:
        masterVolume = 0
        masterVolumeMuted = True


def musicVolumeDown():
    global musicVolume
    if musicVolume > 0.1:
        musicVolume = musicVolume - 0.1


def musicVolumeUp():
    global musicVolume
    if musicVolume < 1:
        musicVolume = musicVolume + 0.1


def musicVolumeMute(previous_volume):
    global musicVolume, musicVolumeMuted
    if musicVolumeMuted == True:
        musicVolume = previous_volume
        musicVolumeMuted = False
    elif musicVolumeMuted == False:
        musicVolume = 0
        musicVolumeMuted = True


def switchSlots(slot):
    global hotbarSlot1,hotbarSlot2,hotbarSlot3,hotbarSlot4,hotbarSlot5,hotbarSlot6,playerHolster,playerIdle,reloadUI, \
        playerShoot, playerSniper, interactText, playerGrab, outAmmoUI
    if slot == 1:
        hotbarSlot1 = not hotbarSlot1
        hotbarSlot2 = False
        hotbarSlot3 = False
        hotbarSlot4 = False
        hotbarSlot5 = False
        hotbarSlot6 = False
        stopRevolverReload()
        griprevolver.stop()
        griprevolver.play()
        playerHolster = not playerHolster
        playerIdle = not playerIdle
        playerSniper = False
        if hotbarSlot1 == False:
            playerShoot = False
            playerHolster = False

    elif slot == 2:
        if scopeScreen == False:
            hotbarSlot2 = not hotbarSlot2
            hotbarSlot1 = False
            hotbarSlot3 = False
            hotbarSlot4 = False
            hotbarSlot5 = False
            hotbarSlot6 = False
            playerHolster = False
            playerShoot = False
            stopRevolverReload()
            if ownSniperRifle == True:
                playerSniper = not playerSniper
                playerGrab = True
                griprevolver.stop()
                griprevolver.play()
                playerIdle = False
            if insideShop == True:
                interactText = False
    elif slot == 3:
        hotbarSlot1 = False
        hotbarSlot2 = False
        hotbarSlot3 = not hotbarSlot3
        hotbarSlot4 = False
        hotbarSlot5 = False
        hotbarSlot6 = False
        interactText = False
        playerHolster = False
        playerSniper = False
        stopRevolverReload()
    elif slot == 4:
        hotbarSlot1 = False
        hotbarSlot2 = False
        hotbarSlot3 = False
        hotbarSlot4 = not hotbarSlot4
        hotbarSlot5 = False
        hotbarSlot6 = False
        interactText = False
        playerSniper = False
        playerHolster = False
        stopRevolverReload()
    elif slot == 5:
        hotbarSlot5 = not hotbarSlot5
        hotbarSlot1 = False
        hotbarSlot2 = False
        hotbarSlot3 = False
        hotbarSlot4 = False
        hotbarSlot6 = False
        interactText = False
        playerSniper = False
        playerHolster = False
        stopRevolverReload()
    elif slot == 6:
        hotbarSlot6 = not hotbarSlot6
        hotbarSlot1 = False
        hotbarSlot2 = False
        hotbarSlot3 = False
        hotbarSlot4 = False
        hotbarSlot5 = False
        stopRevolverReload()
        interactText = False
        playerHolster = False
        playerSniper = False
        playerShoot = False


def stopRevolverReload():
    revolver_reload_timer.stop()
    reload.stop()
    revolverspin.stop()


def volumeButtonReset_timer_handler():
    global masterRightButtonClicked, musicRightButtonClicked, masterLeftButtonClicked, musicLeftButtonClicked, \
        masterIconButtonClicked, musicIconButtonClicked
    masterLeftButtonClicked = False
    musicLeftButtonClicked = False
    masterRightButtonClicked = False
    musicRightButtonClicked = False
    masterIconButtonClicked = False
    musicIconButtonClicked = False


def revolver_reload_timer_handler():
    global revRoundsMag, revRoundsTotal
    if revRoundsTotal > 0:
        revRoundsTotal -= 1
        revRoundsMag += 1
    if revRoundsMag == 6 or revRoundsTotal == 0:
        reloadEnded_timer.start()
        revolver_reload_timer.stop()


def sniper_reload_timer_handler():
    global sniperRoundsMag, sniperRoundsTotal
    if sniperRoundsTotal > 0:
        sniperRoundsTotal -= 1
        sniperRoundsMag += 1
    if sniperRoundsMag == 1:
        sniper_reload_timer.stop()


def music_timer_handler():
    global music
    music.play()
    music_timer.stop()


def startGame_timer_handler():
    global tumbleAuto, moveAbility, banMoveAbility, startGame, dead, restartButtonClicked,playButtonClicked
    tumbleAuto = 15
    startGame = True
    dead = False
    playButtonClicked = False
    restartButtonClicked = False
    moveAbility = True
    banMoveAbility = False
    music_timer.start()
    startGame_timer.stop()


def mainMenu_timer_handler():
    global startGame, dead, mainMenuButtonClicked, mainMenu2ButtonClicked, pause
    startGame = False
    dead = False
    resetValues()
    mainMenuButtonClicked = False
    mainMenu2ButtonClicked = False
    pause = False
    mainMenu()
    intromusic.play(-1)
    mainMenu_timer.stop()


def settingsMenu_timer_handler():
    global settingsButtonClicked, settings
    settings = True
    settingsButtonClicked = False
    settingsMenu_timer.stop()


def settingsDone_timer_handler():
    global settingsDoneButtonClicked, settings
    settings = False
    settingsDoneButtonClicked = False
    settingsDone_timer.stop()


def resumeGame_timer_handler():
    global pause, resumeButtonClicked, confirmationBox, settings
    pause = False
    settings = False
    confirmationBox = False
    resumeButtonClicked = False
    pygame.mixer.unpause()
    resumeGame_timer.stop()


def revolverFireDelay_timer_handler():
    global readyToFireRevolver
    readyToFireRevolver = True
    revolverFireDelay_timer.stop()


def drinkResetDelay_timer_handler():
    global playerDrink
    playerDrink = False
    drinkResetDelay_timer.stop()


def playerHitSound_timer_handler():
    global playerHP
    if playerHP > 0:
        playerhit.play()
        playerHitSound_timer.stop()
    else:
        playerHitSound_timer.stop()


def confirmationBox_timer_handler():
    global confirmationBox, mainMenu2ButtonClicked
    confirmationBox = True
    mainMenu2ButtonClicked = False
    confirmationBox_timer.stop()


def rollStart_timer_handler():
    global standing, rolling, playerRoll1Left, playerRoll2Left, playerRoll3Left, playerRoll1Right, interactText,\
        playerRoll2Right, playerRoll3Right,invincibility, rollReady, cooldown_sweat_y,playerShoot, scopeScreen, \
        insideShop, store1x,store2x, cactusx, banMoveAbility
    standing = False
    rolling = True
    invincibility = True
    playerShoot = False
    scopeScreen = False
    rollReady = False
    cooldown_sweat_y = 252
    disableText()
    combatroll.play()
    if lookingRight == True:
        playerRoll1Right = True
        if insideShop == True:
            if (store1x + 700) <= 0:
                worldRight(0)
            else:
                worldRight(1)
        else:
            worldRight(1)
    elif lookingLeft == True:
        if insideShop == True:
            if (store1x - 200) >= 0:
                insideShop = False
                store1x = 50
                store2x = 750
                cactusx = -200
                banMoveAbility = True
                door.stop()
                door.play()
        playerRoll1Left = True
        worldLeft(1)
    rollMid1_timer.start()
    rollStart_timer.stop()


def rollMid1_timer_handler():
    global standing, rolling, playerRoll1Left, playerRoll2Left, playerRoll1Right, playerRoll2Right, \
        playerRoll3Right,playerRoll3Left, insideShop, store1x,store2x, cactusx, banMoveAbility
    if lookingRight == True:
        playerRoll1Right = False
        playerRoll2Right = True
        if insideShop == True:
            if (store1x + 700) <= 0:
                worldRight(0)
            else:
                worldRight(1)
        else:
            worldRight(1)
    elif lookingLeft == True:
        if insideShop == True:
            if (store1x - 200) >= 0:
                insideShop = False
                store1x = 50
                store2x = 750
                cactusx = -200
                banMoveAbility = True
                door.stop()
                door.play()
        playerRoll1Left = False
        playerRoll2Left = True
        worldLeft(1)
    rollMid2_timer.start()
    rollMid1_timer.stop()


def rollMid2_timer_handler():
    global standing, rolling, playerRoll1Left, playerRoll2Left, playerRoll1Right, playerRoll2Right,\
        playerRoll3Right,playerRoll3Left
    if lookingRight == True:
        playerRoll2Right = False
        playerRoll3Right = True
        if insideShop == True:
            if (store1x + 700) <= 0:
                worldRight(0)
            else:
                worldRight(1)
        else:
            worldRight(1)
    elif lookingLeft == True:
        playerRoll2Left = False
        playerRoll3Left = True
        worldLeft(1)
    rollEnd_timer.start()
    rollMid2_timer.stop()


def rollEnd_timer_handler():
    global standing, rolling, playerRoll1Left, playerRoll2Left, playerRoll1Right, playerRoll2Right, \
        playerRoll3Right, invincibility,interactText,playerRoll3Left, moveAbility, insideShop, store1x,store2x,\
        cactusx, banMoveAbility
    if lookingRight == True:
        playerRoll1Right = False
        playerRoll2Right = False
        playerRoll3Right = False
        if insideShop == True:
            if (store1x + 700) <= 0:
                worldRight(0)
                moveAbility = False
            else:
                worldRight(1)
        else:
            worldRight(1)
    elif lookingLeft == True:
        if insideShop == True:
            if (store1x - 200) >= 0:
                insideShop = False
                store1x = 50
                store2x = 750
                cactusx = -200
                banMoveAbility = True
                door.stop()
                door.play()
        playerRoll1Left = False
        playerRoll2Left = False
        playerRoll3Left = False
        worldLeft(1)
    standing = True
    rolling = False
    invincibility = False
    rollCooldown_timer.start()
    rollEnd_timer.stop()


def rollCooldown_timer_handler():
    global rollReady
    rollReady = True
    rollCooldown_timer.stop()


def walk1_timer_handler():
    ## Continuous walking function, called when press A or D or by walk2_timer if player holds A or D

    # start walk2_timer
    walk2_timer.start()
    walk1_timer.stop()


def walk2_timer_handler():
    ## Continuous walking function, if A or D is still being held, walk again and loop back to walk1_timer
    ## Allows the player to continuously walk when holding down keys, loop breaks when player releases keys

    if lookingRight:
        # if player is still holding down walk right key
        # 'and not' prevents bug where player repeatedly walks left and right if both are held
        if walkingRight and not walkingLeft:
            walkRight()
            walk1_timer.start()
    elif lookingLeft:
        # if player is still holding down walk left key
        # 'and not' prevents bug where player repeatedly walks left and right if both are held
        if walkingLeft and not walkingRight:
            walkLeft()
            walk1_timer.start()
    walk2_timer.stop()


def reloadEnded_timer_handler():
    reload.stop()
    revolverspin.play()
    reloadEnded_timer.stop()


# timers (ms, timer_handler) (1000ms = 1sec)
revolver_reload_timer = simplegui.create_timer(revolverReloadSpeed, revolver_reload_timer_handler)
sniper_reload_timer = simplegui.create_timer(1000, sniper_reload_timer_handler)
music_timer = simplegui.create_timer(15000, music_timer_handler)
startGame_timer = simplegui.create_timer(50, startGame_timer_handler)
mainMenu_timer = simplegui.create_timer(50, mainMenu_timer_handler)
settingsMenu_timer = simplegui.create_timer(50, settingsMenu_timer_handler)
settingsDone_timer = simplegui.create_timer(50, settingsDone_timer_handler)
volumeButtonReset_timer = simplegui.create_timer(50, volumeButtonReset_timer_handler)
resumeGame_timer = simplegui.create_timer(50, resumeGame_timer_handler)
confirmationBox_timer = simplegui.create_timer(50, confirmationBox_timer_handler)
revolverFireDelay_timer = simplegui.create_timer(revolverFireRate, revolverFireDelay_timer_handler)
drinkResetDelay_timer = simplegui.create_timer(drinkTime, drinkResetDelay_timer_handler)
playerHitSound_timer = simplegui.create_timer(100, playerHitSound_timer_handler)
rollStart_timer = simplegui.create_timer(1, rollStart_timer_handler)
rollMid1_timer = simplegui.create_timer(75, rollMid1_timer_handler)
rollMid2_timer = simplegui.create_timer(75, rollMid2_timer_handler)
rollEnd_timer = simplegui.create_timer(75, rollEnd_timer_handler)
rollCooldown_timer = simplegui.create_timer(1500, rollCooldown_timer_handler)
walk1_timer = simplegui.create_timer(1, walk1_timer_handler)
walk2_timer = simplegui.create_timer(150, walk2_timer_handler)
reloadEnded_timer = simplegui.create_timer(125, reloadEnded_timer_handler)


# timers tuple
timerTuple = (revolver_reload_timer, sniper_reload_timer, music_timer, startGame_timer, revolverFireDelay_timer,
              drinkResetDelay_timer, resumeGame_timer, mainMenu_timer, playerHitSound_timer, confirmationBox_timer,
              volumeButtonReset_timer, settingsDone_timer, settingsMenu_timer, rollStart_timer, rollMid1_timer,
              rollEnd_timer, rollCooldown_timer, walk1_timer, walk2_timer, reloadEnded_timer)

# Main Menu Music
intromusic.play(-1)
resetValues()

# load highscore from file
try:
    pickle_in = open("savedata/highscore.txt","rb")
    highscore = pickle.load(pickle_in)
    pickle_in.close()
except:
    pickle_out = open("savedata/highscore.txt", "wb")
    pickle.dump(highscore, pickle_out)
    pickle_out.close()

b1 = Bandit()
b2 = Bandit()
b3 = Bandit()
b4 = Bandit()

# Game Loop (Screen Refresh Loop)
while True:
    b1.move()
    b2.move()
    b3.move()
    b4.move()

    # Event Handler ------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        # When game is closed
        if event.type == pygame.QUIT:
            # save highscore to file
            pickle_out = open("savedata/highscore.txt","wb")
            pickle.dump(highscore, pickle_out)
            pickle_out.close()
            # close game
            pygame.mixer.stop()
            music_timer.stop()
            stopAllTimers(timerTuple)
            pygame.quit()
            sys.exit()
        # Check Walk Both (Fixes bug where player gets stuck when switching directions)
        checkWalkBoth()
        # Key Down Handler
        if event.type == pygame.KEYDOWN:
            # Pause Game
            if event.key == pygame.K_ESCAPE and pause == False and startGame == True and dead == False:
                pygame.mixer.pause()
                screen.blit(asset_paused_darken, (0, 0))
                pause = True
            # Unpause Game
            elif event.key == pygame.K_ESCAPE and pause == True and settings == False:
                resumeGame_timer.start()
            # Exit settings
            elif event.key == pygame.K_ESCAPE and settings == True:
                settings = False
            if pause == False:
                # Walk left
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    walkLeft()
                    # stop timers to prevent walk timer stack bug
                    walk2_timer.stop()
                    walk1_timer.stop()
                    walkingLeft = True
                    walk1_timer.start()
                # Walk right
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    walkRight()
                    # stop timers to prevent walk timer stack bug
                    walk2_timer.stop()
                    walk1_timer.stop()
                    walkingRight = True
                    walk1_timer.start()
                # Roll
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    roll()
                # Reloading
                if event.key == pygame.K_r:
                    # Revolver
                    if hotbarSlot1 == True:
                        if revRoundsMag < 6:
                            playerHolster = True
                            playerShoot = False
                            if revRoundsTotal > 0:
                                reload.stop()
                                reload.play()
                                revolver_reload_timer.start()
                    # Sniper Rifle
                    if hotbarSlot2 == True or scopeScreen == True:
                        if sniperRoundsMag < 1:
                            scopeScreen = False
                            playerSniper = True
                            if sniperRoundsTotal > 0:
                                sniper_reload.stop()
                                sniper_reload.play()
                                sniper_reload_timer.start()
                # Use Item (Space)
                if event.key == pygame.K_SPACE:
                    # Revolver fire
                    if hotbarSlot1 == True:
                        if moveAbility == True and readyToFireRevolver == True:
                            fire()
                            readyToFireRevolver = False
                            revolverFireDelay_timer.start()
                    # Sniper Rifle fires
                    if hotbarSlot2 == True and ownSniperRifle == True and sniperRoundsMag >= 1:
                        fire()
                    # HP Potion is used
                    if hotbarSlot6 == True and hpPotionCount > 0:
                        hpPotion()
                        drinkResetDelay_timer.start()
                        playerIdle = False
                # Aim Sniper Rifle
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if hotbarSlot2 == True and playerSniper == True and ownSniperRifle == True \
                            and insideShop == False and rolling == False:
                        scopeScreen = not scopeScreen
                        if scopeScreen == True:
                            breath.stop()
                            breath.play()
                            heartbeat.stop()
                            heartbeat.play()
                            ban1InScope = False
                            ban2InScope = False
                            ban3InScope = False
                # Switch to hotbar slot 1
                if event.key == pygame.K_1 and moveAbility == True and scopeScreen == False:
                    switchSlots(1)
                # Switch to hotbar slot 2
                if event.key == pygame.K_2 and moveAbility == True:
                    switchSlots(2)
                # Switch to hotbar slot 3
                if event.key == pygame.K_3 and moveAbility == True and scopeScreen == False:
                    switchSlots(3)
                # Switch to hotbar slot 4
                if event.key == pygame.K_4 and moveAbility == True and scopeScreen == False:
                    switchSlots(4)
                # Switch to hotbar slot 5
                if event.key == pygame.K_5 and moveAbility == True and scopeScreen == False:
                    switchSlots(5)
                # Switch to hotbar slot Q (6)
                if event.key == pygame.K_q and moveAbility == True and scopeScreen == False:
                    switchSlots(6)
                # Enter Store
                if store1x <= 100 and store1x >= 0:
                    if playerShoot == False and scopeScreen == False and insideShop == False and playerSniper == False:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            insideShop = True
                            lookingRight = True
                            lookingLeft = False
                            interactText = False
                            banMoveAbility = False
                            store1x = 150
                            store2x = 850
                            cactusx = -100
                            door.stop()
                            door.play()
                            banHP = -50
                            ban2HP = -50
                            ban3HP = -50
                # Open Catalog
                if store1x + 420 <= 100 and store1x + 420 >= 0:
                    if playerHolster == False and playerShoot == False and insideShop == True and catalog == False\
                            and playerSniper == False:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            catalog = not catalog
                            catalogPage1 = True
                            interactText = False
                            moveAbility = False
                            disableText()
                            openbook.stop()
                            openbook.play()
                    elif playerHolster == False and playerShoot == False and insideShop == True and catalog == True\
                            and playerSniper == False:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            catalog = False
                            catalogPage1 = False
                            catalogPage2 = False
                            catalogPage3 = False
                            disableText()
                            moveAbility = True
                            openbook.stop()
                            openbook.play()
                # Turn Pages
                if catalog == True:
                    if catalogPage1 == True:
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            catalogPage1 = False
                            catalogPage2 = True
                            catalogPage3 = False
                            disableText()
                            turnpage.stop()
                            turnpage.play()
                    elif catalogPage2 == True:
                        # Purchase Sniper Rifle
                        if event.key == pygame.K_2:
                            if moneyCount >= 1000 and ownSniperRifle == False:
                                purchasedText = True
                                ownSniperRifle = True
                                hotbarSlot2 = False
                                moneyCount -= 1000
                                cashregister.stop()
                                cashregister.play()
                            elif moneyCount < 1000 and ownSniperRifle == False:
                                insufFundsText = True
                                error.stop()
                                error.play()
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            catalogPage1 = False
                            catalogPage2 = False
                            catalogPage3 = True
                            disableText()
                            turnpage.stop()
                            turnpage.play()
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            catalogPage1 = True
                            catalogPage2 = False
                            catalogPage3 = False
                            disableText()
                            turnpage.stop()
                            turnpage.play()
                    elif catalogPage3 == True:
                        # Purchase Revolver Rounds
                        if event.key == pygame.K_1:
                            if moneyCount >= 50:
                                insufFundsText = False
                                purchasedText = True
                                revRoundsTotal += 24
                                moneyCount -= 50
                                cashregister.stop()
                                cashregister.play()
                            elif moneyCount < 50:
                                purchasedText = False
                                insufFundsText = True
                                error.stop()
                                error.play()
                        # Purchase Sniper Rifle Rounds
                        if event.key == pygame.K_2:
                            if moneyCount >= 100:
                                insufFundsText = False
                                purchasedText = True
                                sniperRoundsTotal += 6
                                moneyCount -= 100
                                cashregister.stop()
                                cashregister.play()
                            elif moneyCount < 100:
                                purchasedText = False
                                insufFundsText = True
                                error.stop()
                                error.play()
                        # Purchase HP Potion
                        if event.key == pygame.K_4:
                            if moneyCount >= 100:
                                insufFundsText = False
                                purchasedText = True
                                hpPotionCount += 1
                                moneyCount -= 100
                                cashregister.stop()
                                cashregister.play()
                            elif moneyCount < 100:
                                purchasedText = False
                                insufFundsText = True
                                error.stop()
                                error.play()
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            catalogPage1 = False
                            catalogPage2 = True
                            catalogPage3 = False
                            disableText()
                            turnpage.stop()
                            turnpage.play()
        # Key Up Handler
        if event.type == pygame.KEYUP:
            # Let go of walk left
            if walkingBoth == False and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                walkingLeft = False
                walk2_timer.stop()
                walk1_timer.stop()
            # Let go of walk left while holding both
            elif walkingBoth == True and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                walk2_timer.stop()
                walk1_timer.stop()
                walkingLeft = False
                walkingRight = True
                walk1_timer.start()
            # Let go of walk right
            if walkingBoth == False and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                walkingRight = False
                walk2_timer.stop()
                walk1_timer.stop()
            # Let go of walk right while holding both
            elif walkingBoth == True and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                walk2_timer.stop()
                walk1_timer.stop()
                walkingRight = False
                walkingLeft = True
                walk1_timer.start()

        # Mouse Handler
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse Button 1
            if event.button == 1:
                # In Main Menu Screen
                # Play Button
                if startGame == False and settings == False and playButtonHover == True:
                    button.play()
                    intro.play()
                    startGame_timer.start()
                    playButtonHover = False
                    playButtonClicked = True
                if settings == False and settingsButtonHover == True:
                    button.play()
                    settingsMenu_timer.start()
                    settingsButtonHover = False
                    settingsButtonClicked = True

                # In Death Screen
                # Restart Game
                if startGame == False and dead == True and restartButtonHover == True:
                    button.play()
                    stopSounds()
                    intro.play()
                    startGame_timer.start()
                    restartButtonHover = False
                    restartButtonClicked = True
                    resetValues()
                # Main Menu Button
                if startGame == False and dead == True and mainMenuButtonHover == True:
                    button.play()
                    stopSounds()
                    mainMenu_timer.start()
                    mainMenuButtonHover = False
                    mainMenuButtonClicked = True

                # In Pause Screen
                # Resume Button
                if pause == True and confirmationBox == False and settings == False and resumeButtonHover == True:
                    button.play()
                    resumeGame_timer.start()
                    resumeButtonHover = False
                    resumeButtonClicked = True
                # Settings Button
                if confirmationBox == False and settings == False and settingsButtonHover == True:
                    button.play()
                    settingsMenu_timer.start()
                    settingsButtonHover = False
                    settingsButtonClicked = True
                # Main Menu Button
                if pause == True and confirmationBox == False and settings == False and mainMenu2ButtonHover == True:
                    button.play()
                    confirmationBox_timer.start()
                    mainMenu2ButtonHover = False
                    mainMenu2ButtonClicked = True
                # In Confirmation Box
                if pause == True and confirmationBox == True:
                    # Yes Button
                    if confirmYesButtonHover == True:
                        button.play()
                        stopSounds()
                        mainMenu_timer.start()
                        confirmYesButtonHover = False
                        confirmYesButtonClicked = True
                    # No Button
                    if confirmNoButtonHover == True:
                        button.play()
                        confirmationBox = False
                # In Settings
                if settings == True:
                    # Done Button
                    if settingsDoneButtonHover == True:
                        button.play()
                        settingsDone_timer.start()
                        settingsDoneButtonHover = False
                        settingsDoneButtonClicked = True
                    # Master Down Button
                    if masterLeftButtonHover == True:
                        button.play()
                        masterVolumeDown()
                        volumeButtonReset_timer.start()
                        masterLeftButtonHover = False
                        masterLeftButtonClicked = True
                    # Master Up Button
                    if masterRightButtonHover == True:
                        button.play()
                        masterVolumeUp()
                        volumeButtonReset_timer.start()
                        masterRightButtonHover = False
                        masterRightButtonClicked = True
                    # Master Icon Button
                    if masterIconButtonHover == True:
                        button.play()
                        if masterVolumeMuted == False:
                            masterVolumeStored = masterVolume
                        masterVolumeMute(masterVolumeStored)
                        volumeButtonReset_timer.start()
                        masterIconButtonHover = False
                        masterIconButtonClicked = True
                    # Music Down Button
                    if musicLeftButtonHover == True:
                        button.play()
                        musicVolumeDown()
                        volumeButtonReset_timer.start()
                        musicLeftButtonHover = False
                        musicLeftButtonClicked = True
                    # Music Up Button
                    if musicRightButtonHover == True:
                        button.play()
                        musicVolumeUp()
                        volumeButtonReset_timer.start()
                        musicRightButtonHover = False
                        musicRightButtonClicked = True
                    # Music Icon Button
                    if musicIconButtonHover == True:
                        button.play()
                        if musicVolumeMuted == False:
                            musicVolumeStored = musicVolume
                        musicVolumeMute(musicVolumeStored)
                        volumeButtonReset_timer.start()
                        musicIconButtonHover = False
                        musicIconButtonClicked = True


                # Use HP Beer
                if hotbarSlot6 == True and hpPotionCount > 0:
                    hpPotion()
                    drinkResetDelay_timer.start()
                    playerIdle = False
                # Fire Revolver
                if hotbarSlot1 == True:
                    if moveAbility == True and readyToFireRevolver == True:
                        fire()
                        readyToFireRevolver = False
                        revolverFireDelay_timer.start()
                # Fire Sniper Rifle
                if hotbarSlot2 == True and ownSniperRifle == True and sniperRoundsMag >= 1:
                    fire()

    # Mouse Position
    mouse_posx,mouse_posy = pygame.mouse.get_pos()
    # print(str(mouse_posx) + ", " + str(mouse_posy))

    # Death Buttons
    if dead == True:
        # Restart Button
        # Hover Button
        if (237 <= mouse_posx <= 363) and (313 <= mouse_posy <= 354) and restartButtonClicked == False:
            screen.blit(asset_restart_button_hover, (0, 0))
            restartButtonHover = True
        # Click Button
        elif (237 <= mouse_posx <= 363) and (313 <= mouse_posy <= 354) and restartButtonClicked == True:
            screen.blit(asset_restart_button_clicked, (0, 0))
            restartButtonHover = False
        # Normal Button
        else:
            screen.blit(asset_restart_button_normal, (0, 0))
            restartButtonHover = False

        # Main Menu Button
        # Hover Button
        if (238 <= mouse_posx <= 364) and (394 <= mouse_posy <= 438) and mainMenuButtonClicked == False:
            screen.blit(asset_main_menu_button_hover, (0, 0))
            mainMenuButtonHover = True
        # Click Button
        elif (238 <= mouse_posx <= 364) and (394 <= mouse_posy <= 438) and mainMenuButtonClicked == True:
            screen.blit(asset_main_menu_button_clicked, (0, 0))
            mainMenuButtonHover = False
        # Normal Button
        else:
            screen.blit(asset_main_menu_button_normal, (0, 0))
            mainMenuButtonHover = False

    # Main Menu -------------------------------------------------------------------------------------------------
    if startGame == False and dead == False:
        mainMenu()
    elif startGame == True:
        tumbleAuto = 15
        intromusic.stop()
    # Paused ----------------------------------------------------------------------------------------------------
    if pause == True:
        pauseGame()

    # Game Started ----------------------------------------------------------------------------------------------
    if startGame == True and pause == False:
        # sky
        screen.blit(asset_sky_day, (0, 0))
        # ground
        screen.blit(asset_ground_sand, (0, 403))
        # clouds
        screen.blit(asset_cloud1, (cloud1x-71, 37))
        screen.blit(asset_cloud2, (cloud2x-71, 121))
        # cactus
        screen.blit(asset_cactus, (cactusx, 209))
        screen.blit(asset_cactus, (cactusx+760, 209))
        # store
        screen.blit(asset_store, (store1x-97, 14))
        # saloon
        screen.blit(asset_saloon, (store2x-94, 13.5))
        # tumbleweed
        screen.blit(asset_tumbleweed, (tumweed1x-38, 331))

        b1.draw()
        b2.draw()
        b3.draw()
        b4.draw()
        # bandit #1 alive
        if banHP > 0:
            # bandit 1 text
            screen.blit(ban1Tag, (banx1-30,232))
            screen.blit(ban1HPTag, (banx1-6,246))
            if ban1left == False:
                screen.blit(asset_bandit1left, (banx1-39.5, 262))
            elif ban1left == True:
                screen.blit(asset_bandit1right, (banx1-7, 262))
        # bandit #2 alive
        if ban2HP > 0:
            screen.blit(ban2Tag, (banx2-25,222))
            screen.blit(ban2HPTag, (banx2-5,236))
            if ban2left == False:
                screen.blit(asset_bandit2left, (banx2-40, 252))
            elif ban2left == True:
                screen.blit(asset_bandit2right, (banx2+24-40, 252))
        # bandit #3 alive
        if ban3HP > 0:
            screen.blit(ban3Tag, (banx3-29,232))
            screen.blit(ban3HPTag, (banx3-5,246))
            if ban3left == False:
                screen.blit(asset_bandit3left, (banx3-40, 262))
            elif ban3left == True:
                screen.blit(asset_bandit3right, (banx3-10, 262))

        # shop interior
        if insideShop == True:
            screen.blit(asset_shop_interior, (store1x-250, 0))

        # character model
        if standing == True:
            if lookingRight == True:
                # drink potion right
                if playerDrink == True:
                    screen.blit(asset_player_drink_right, (204, 246))
                else:
                    # base player right
                    screen.blit(asset_player_right, (217, 253))
                # idle legs
                if playerLegsIdle == True:
                    screen.blit(asset_player_legs_idle_right, (217, 252))
                # sniper rifle on back
                if ownSniperRifle == True and playerSniper == False:
                    screen.blit(asset_sniper_rifle_right, (237, 302))
                # revolver on hip
                if playerShoot == False:
                    screen.blit(asset_revolver_vert_right, (236, 344))
                # holster
                screen.blit(asset_holster_right, (217, 259))
                # hp beer in hand right
                if hotbarSlot6 == True and hpPotionCount > 0 and playerIdle == True:
                    screen.blit(asset_hearty_beer_right, (231, 353))
                # holding sniper right
                if playerSniper == True and playerWalk == False:
                    screen.blit(asset_sniper_right, (207, 349))
                # idle arms
                if playerIdle == True:
                    screen.blit(asset_player_arms_idle, (216, 253))
                # hand on holster
                if playerHolster == True and playerWalk == False:
                    screen.blit(asset_player_holster_right, (217, 253))
                # grab sniper
                if playerGrab == True:
                    screen.blit(asset_player_holster_right, (217, 253))
                # walk right
                if playerWalk == True:
                    # drink walk
                    if playerDrink == True:
                        screen.blit(asset_player_legs_walk_right, (217, 252))
                    # hold sniper walk
                    elif playerSniper == True:
                        screen.blit(asset_sniper_right, (225, 349))
                        screen.blit(asset_player_legs_walk_right, (217, 252))
                        screen.blit(asset_player_arms_walk_right, (217, 253))
                    # holster walk
                    elif playerHolster == True:
                        screen.blit(asset_player_legs_walk_right, (217, 252))
                        if playerShoot == False:
                            screen.blit(asset_revolver_vert_right, (236, 344))
                        screen.blit(asset_holster_right, (217, 259))
                        screen.blit(asset_player_holsterwalk_right, (217, 253))

                    else:
                        # hp beer in hand right
                        if hotbarSlot6 == True and hpPotionCount > 0:
                            screen.blit(asset_hearty_beer_right, (249, 352))
                        # default walk
                        screen.blit(asset_player_arms_walk_right, (217, 253))
                        if ownSniperRifle == True and playerSniper == False:
                            screen.blit(asset_sniper_rifle_right, (237, 302))
                        screen.blit(asset_player_legs_walk_right, (217, 252))
                        if playerShoot == False:
                            screen.blit(asset_revolver_vert_right, (236, 344))
                        screen.blit(asset_holster_right, (217, 259))
                # bandana right
                screen.blit(asset_bandana_right, (217, 253))
                # extended arm right
                if playerShoot == True:
                    screen.blit(asset_revolver_right, (279, 311))
                    screen.blit(asset_player_shoot_right, (227, 252))
                    screen.blit(asset_muzzleflash_right, (bulletx-12, 307))
            if lookingLeft == True:
                # revolver on hip
                if playerShoot == False:
                    screen.blit(asset_revolver_vert_grip_left, (248, 342))
                # holding sniper left
                if playerSniper == True and playerWalk == False:
                    screen.blit(asset_sniper_left, (190, 349))
                # hp beer in hand right
                if hotbarSlot6 == True and hpPotionCount > 0 and playerIdle == True:
                    screen.blit(asset_hearty_beer_left, (240, 353))
                # drink potion left
                if playerDrink == True:
                    screen.blit(asset_player_drink_left, (199, 247))
                else:
                    # base player left
                    screen.blit(asset_player_left, (217, 253))
                # idle legs
                if playerLegsIdle == True:
                    screen.blit(asset_player_legs_idle_left, (217, 252))
                # idle arms
                if playerIdle == True:
                    screen.blit(asset_player_arms_idle, (217, 253))
                # hand on holster
                if playerHolster == True and playerWalk == False:
                    screen.blit(asset_player_holster_left, (217, 253))
                # grab sniper
                if playerGrab == True:
                    screen.blit(asset_player_holster_left, (217, 253))
                # sniper rifle on back
                if ownSniperRifle == True and playerSniper == False:
                    screen.blit(asset_sniper_rifle_left, (253, 302))
                    # walk left
                if playerWalk == True:
                    # drink walk
                    if playerDrink == True:
                        screen.blit(asset_player_legs_walk_left, (217, 252))
                    # hold sniper walk
                    elif playerSniper == True:
                        screen.blit(asset_sniper_left, (207, 348))
                        screen.blit(asset_player_left, (217, 253))
                        screen.blit(asset_player_arms_walk_left, (217, 253))
                        screen.blit(asset_player_legs_walk_left, (217, 252))
                    # holster walk
                    elif playerHolster == True:
                        screen.blit(asset_player_holsterwalk_left, (217, 253))
                        if ownSniperRifle == True and playerSniper == False:
                            screen.blit(asset_sniper_rifle_left, (253, 302))
                        screen.blit(asset_player_legs_walk_left, (217, 252))
                    else:
                        # hp beer in hand left
                        if hotbarSlot6 == True and hpPotionCount > 0:
                            screen.blit(asset_hearty_beer_left, (262, 352))
                        # default walk
                        screen.blit(asset_player_arms_walk_left, (217, 253))
                        if ownSniperRifle == True and playerSniper == False:
                            screen.blit(asset_sniper_rifle_left, (253, 302))
                        screen.blit(asset_player_legs_walk_left, (217, 252))
                # extended arm left
                if playerShoot == True:
                    screen.blit(asset_player_shoot_left, (207, 252))
                    screen.blit(asset_player_arms_idle, (217, 252))
                    screen.blit(asset_revolver_left, (182, 311))
                    screen.blit(asset_muzzleflash_left, (bulletx-250, 307))
                # bandana left
                screen.blit(asset_bandana_left, (217, 253))
        # Roll
        if rolling == True:
            if lookingRight == True:
                if playerRoll1Right == True:
                    screen.blit(asset_player_roll1_right, (150, 265))
                if playerRoll2Right == True:
                    screen.blit(asset_player_roll2_right, (150, 265))
                if playerRoll3Right == True:
                    screen.blit(asset_player_roll3_right, (150, 265))
            if lookingLeft == True:
                if playerRoll1Left == True:
                    screen.blit(asset_player_roll1_left, (150, 265))
                if playerRoll2Left == True:
                    screen.blit(asset_player_roll2_left, (150, 265))
                if playerRoll3Left == True:
                    screen.blit(asset_player_roll3_left, (150, 265))
        # Cooldown sweat
        if standing == True and rollReady == False:
            if lookingRight:
                screen.blit(asset_player_cooldown_sweat_right, (212, cooldown_sweat_y))
            if lookingLeft:
                screen.blit(asset_player_cooldown_sweat_left, (222, cooldown_sweat_y))


        # catalog pages
        if insideShop == True:
            if catalog == True:
                if catalogPage1 == True:
                    screen.blit(asset_catalog_1, (0, 0))
                elif catalogPage2 == True:
                    screen.blit(asset_catalog_2, (0, 0))
                elif catalogPage3 == True:
                    screen.blit(asset_catalog_3, (0, 0))

        # catalog weapon prices
        if catalogPage2 == True:
            screen.blit(asset_text_owned, (220, 203))
            if ownSniperRifle == True:
                screen.blit(asset_text_owned, (220, 294))
            if ownSniperRifle == False:
                if moneyCount < 1000:
                    screen.blit(asset_text_1000_red, (226, 293))
                elif moneyCount >= 1000:
                    screen.blit(asset_text_1000_green, (226, 293))
        if catalogPage3 == True:
            if moneyCount < 100:
                # hearty beer
                screen.blit(asset_text_100_red, (505, 202))
                # 30-50 rounds
                screen.blit(asset_text_100_red, (235, 293))
            elif moneyCount >= 100:
                # hearty beer
                screen.blit(asset_text_100_green, (505, 202))
                # 30-50 rounds
                screen.blit(asset_text_100_green, (235, 293))
            if moneyCount < 50:
                # .45 rounds
                screen.blit(asset_text_50_red, (240, 200))
            elif moneyCount >= 50:
                # .45 rounds
                screen.blit(asset_text_50_green, (240, 200))

        if insideShop == False:
            # ban #1 dead
            if banHP <= 0:
                if ban1left == False:
                    screen.blit(asset_bandit1left_dead, (banx1-23, 377))
                elif ban1left == True:
                    screen.blit(asset_bandit1right_dead, (banx1-123, 377))
            # ban #2 dead
            if ban2HP <= 0:
                if ban2left == False:
                    screen.blit(asset_bandit2left_dead, (banx2-28, 377))
                elif ban2left == True:
                    screen.blit(asset_bandit2right_dead, (banx2-128, 377))
            # ban #3 dead
            if ban3HP <= 0:
                if ban3left == False:
                    screen.blit(asset_bandit3left_dead, (banx3-23, 376))
                elif ban3left == True:
                    screen.blit(asset_bandit3right_dead, (banx3-123, 376))
        # ban 1 damage range
        if banHP > 0:
            if banx1 <= 290 and banx1 >= 210 and insideShop == False:
                playerHit(4)
        elif banHP == -50:
            banHP = 100
            banx1 = getBanditRespawn()
        # ban 2 damage range
        if ban2HP > 0:
            if banx2 <= 290 and banx2 >= 210 and insideShop == False:
                playerHit(4)
        elif ban2HP == -50:
            ban2HP = 100
            banx2 = getBanditRespawn()
        # ban 3 damage range
        if ban3HP > 0:
            if banx3 <= 290 and banx3 >= 210 and insideShop == False:
                playerHit(4)
        elif ban3HP == -50:
            ban3HP = 100
            banx3 = getBanditRespawn()

        # sniper scope
        if ownSniperRifle == True:
            if scopeScreen == True:
                # update bandit scale
                asset_ban1_fp = pygame.transform.scale(asset_bandit1_fp, (ban1W+(scopeWalk*0.7), ban1H+scopeWalk))
                asset_ban1_fp_rect = asset_ban1_fp.get_rect(center=[300,330])
                asset_ban2_fp = pygame.transform.scale(asset_bandit2_fp, (ban2W+(scope2Walk*0.7), ban2H+scope2Walk))
                asset_ban2_fp_rect = asset_ban2_fp.get_rect(center=[300,330])
                asset_ban3_fp = pygame.transform.scale(asset_bandit3_fp, (ban3W+(scope3Walk*0.7), ban3H+scope3Walk))
                asset_ban3_fp_rect = asset_ban3_fp.get_rect(center=[300,330])
                # backdrop
                if lookingRight == True:
                    screen.blit(asset_scope_back_right, (0, 0))
                if lookingLeft == True:
                    screen.blit(asset_scope_back_left, (0, 0))

                # fp bandits
                if banHP > 0 and ban2InScope == False and ban3InScope == False:
                    if banx1 <= 700 and banx1 >= 250 and lookingRight == True\
                            or banx1 >= -100 and banx1 <= 250 and lookingLeft == True:
                        ban1InScope = True
                        screen.blit(asset_ban1_fp, asset_ban1_fp_rect)

                if ban2HP > 0 and ban1InScope == False and ban3InScope == False:
                    if banx2 <= 700 and banx2 >= 250 and lookingRight == True\
                            or banx2 >= -100 and banx2 <= 250 and lookingLeft == True:
                        ban2InScope = True
                        screen.blit(asset_ban2_fp, asset_ban2_fp_rect)

                if ban3HP > 0 and ban1InScope == False and ban2InScope == False:
                    if banx3 <= 700 and banx3 >= 250 and lookingRight == True\
                            or banx3 >= -100 and banx3 <= 250 and lookingLeft == True:
                        ban3InScope = True
                        screen.blit(asset_ban3_fp, asset_ban3_fp_rect)

                # scope
                screen.blit(asset_sniperscope, (0, 0))
                screen.blit(asset_ammo_icon, (25-12.5, 583-10))
                screen.blit(sniperAmmo_text, (41, 571))
            else:
                breath.stop()
                heartbeat.stop()



        # Constant Refresh -------------------------------------------------------------------------------------

        # HUD
        if startGame == True and scopeScreen == False:
            showHUD()

        # Player Model Refresh
        playerLegsIdle = True
        playerWalk = False

        playerGrab = False
        if playerHolster == False and playerShoot == False and playerDrink == False:
            playerIdle = True
        if (playerHolster == True or playerSniper == True) and insideShop == True:
            screen.blit(shopWarning_text, (store1x + 527, 207))

        # If trying to walk both left and right
        if walkingLeft and walkingRight:
            walkingBoth = True
        else:
            walkingBoth = False

        # Check if dead
        if playerHP <= 0:
            playerDead()

        # check for interact
        interactCheck()

        # check for highscore
        if score > highscore:
            highscore = score

        # check for out of ammo or needed reload
        # revolver --------------------
        if revRoundsMag <= 0 and revRoundsTotal > 0:
            revolverOutMag = True
        else:
            revolverOutMag = False

        if revRoundsTotal <= 0 and revRoundsMag <= 0:
            revolverOutAmmo = True
            revolverOutMag = False
        else:
            revolverOutAmmo = False
        # sniper rifle ----------------
        if sniperRoundsMag <= 0 and sniperRoundsTotal > 0:
            sniperOutMag = True
        else:
            sniperOutMag = False

        if sniperRoundsTotal <= 0 and sniperRoundsMag <= 0:
            sniperOutAmmo = True
            sniperOutMag = False
        else:
            sniperOutAmmo = False

        # check for whether or not to show reload/outammo UI
        if (revolverOutMag and hotbarSlot1) or (sniperOutMag and hotbarSlot2):
            reloadUI = True
            interactText = False
        else:
            reloadUI = False
        if (revolverOutAmmo and hotbarSlot1) or (sniperOutAmmo and hotbarSlot2):
            reloadUI = False
            outAmmoUI = True
            interactText = False
        else:
            outAmmoUI = False


        # text refresh
        ban1HPTag = font1.render(("HP: " + str(banHP)), True, (255, 255, 255))
        ban2HPTag = font1.render(("HP: " + str(ban2HP)), True, (255, 255, 255))
        ban3HPTag = font1.render(("HP: " + str(ban3HP)), True, (255, 255, 255))
        playerHP_text = font2.render((str(playerHP)), True, (255, 255, 255))
        playerScore_text = font2.render((str(score)), True, (255, 255, 255))
        playerMoney_text = font2.render((str(moneyCount)), True, (255, 255, 255))
        revolverAmmo_text = font2.render((str(revRoundsMag) + "/" + str(revRoundsTotal)), True, (255, 255, 255))
        sniperAmmo_text = font2.render((str(sniperRoundsMag) + "/" + str(sniperRoundsTotal)), True, (255, 255, 255))
        potionCount_text = font1.render((str(hpPotionCount)), True, (255, 255, 255))
        deathScore_text = font1.render(("Score: " + str(score)), True, (255, 255, 255))
        masterVolume_text = font1.render((str(masterVolume)), True, (255, 255, 255))
        musicVolume_text = font1.render((str(musicVolume)), True, (255, 255, 255))
        playerHighscore_text = font1.render("Highscore: " + (str(highscore)), True, (255, 255, 255))

        # volume refresh
        step.set_volume(masterVolume)
        woodstep.set_volume(masterVolume)
        button.set_volume(masterVolume)
        griprevolver.set_volume(masterVolume)
        shot.set_volume(masterVolume)
        empty.set_volume(masterVolume)
        reload.set_volume(masterVolume)
        revolverspin.set_volume(masterVolume)
        death.set_volume(masterVolume)
        playerhit.set_volume(masterVolume)
        banpain.set_volume(masterVolume)
        snipershot.set_volume(masterVolume)
        heartbeat.set_volume(masterVolume)
        breath.set_volume(masterVolume)
        door.set_volume(masterVolume)
        openbook.set_volume(masterVolume)
        turnpage.set_volume(masterVolume)
        cashregister.set_volume(masterVolume)
        error.set_volume(masterVolume)
        potion.set_volume(masterVolume)
        sniper_reload.set_volume(masterVolume)
        combatroll.set_volume(masterVolume)
        intromusic.set_volume(musicVolume * masterVolume)
        intro.set_volume(musicVolume * masterVolume)
        music.set_volume(musicVolume * masterVolume)

        # building loop
        if store2x <= -500:
            store1x += 1900
            store2x += 1900
        elif store2x >= 1400:
            store1x -= 1900
            store2x -= 1900
            cactusx -= 1900
        if cactusx <= -1000:
            cactusx += 1900
        elif cactusx >= 900:
            cactusx -= 1900

        # active hotbar slot position
        if hotbarSlot1 == True:
            activeSlotx1 = 150
            activeSlotx2 = 200
        elif hotbarSlot2 == True:
            activeSlotx1 = 200
            activeSlotx2 = 250
        elif hotbarSlot3 == True:
            activeSlotx1 = 250
            activeSlotx2 = 300
        elif hotbarSlot4 == True:
            activeSlotx1 = 300
            activeSlotx2 = 350
        elif hotbarSlot5 == True:
            activeSlotx1 = 350
            activeSlotx2 = 400
        elif hotbarSlot6 == True:
            activeSlotx1 = 400
            activeSlotx2 = 450
        else:
            activeSlotx1 = -500
            activeSlotx2 = -500

        # cloud pos
        cloud1x -= cloudAuto
        if cloud1x + 85 <= -100:
            cloud1x = 800
        cloud2x -= cloudAuto
        if cloud2x + 85 <= -100:
            cloud2x = 1100

        # tumweed pos
        tumweed1x -= tumbleAuto
        if tumweed1x <= - 2000:
            tumweed1x = 1100

        # bullet reset
        bulletx = -330

        # cooldown sweat pos
        if rollReady == False:
            cooldown_sweat_y += 1
        if cooldown_sweat_y > 273:
            cooldown_sweat_y = 252

        if banMoveAbility == True:
            banMove = 8
        elif banMoveAbility == False:
            banMove = 0

        if banMoveAbility == True:
            # ban 1 position
            if banHP > 0:
                # if out of scope range
                if banx1 > 700 or banx1 < -100:
                    scopeWalk = 0
                # if in melee range of player
                elif banx1 <= 290 and banx1 >= 210:
                    scopeWalk += 0
                # if in scope range
                elif banx1 <= 700 or banx1 >= -100:
                    scopeWalk += 15
                if banx1 >= 280:
                    banx1 -= banMove
                    ban1left = False
                if banx1 <= 220:
                    banx1 += banMove
                    ban1left = True
            elif banHP <= 0:
                banHP -= 1
                # ban 2 position
            if ban2HP > 0:
                # if out of scope range
                if banx2 > 700 or banx2 < -100:
                    scope2Walk = 0
                # if in melee range of player
                elif banx2 <= 290 and banx2 >= 210:
                    scope2Walk += 0
                # if in scope range
                elif banx2 <= 700 or banx2 >= -100:
                    scope2Walk += 15
                if banx2 >= 280:
                    banx2 -= banMove
                    ban2left = False
                if banx2 <= 220:
                    banx2 += banMove
                    ban2left = True
            elif ban2HP <= 0:
                ban2HP -= 1
            # ban 3 position
            if ban3HP > 0:
                # if out of scope range
                if banx3 > 700 or banx3 < -100:
                    scope3Walk = 0
                # if in melee range of player
                elif banx3 <= 290 and banx3 >= 210:
                    scope3Walk += 0
                # if in scope range
                elif banx3 <= 700 or banx3 >= -100:
                    scope3Walk += 15
                if banx3 >= 280:
                    banx3 -= banMove
                    ban3left = False
                if banx3 <= 220:
                    banx3 += banMove
                    ban3left = True
            elif ban3HP <= 0:
                ban3HP -= 1



    pygame.display.update()
    clock.tick(25)

# End
